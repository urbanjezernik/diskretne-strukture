#!/usr/bin/env python3
"""
Split a monolithic LaTeX “book” into per-chapter MyST-Markdown files
and write a valid _toc.yml for Jupyter-Book.
"""
import pathlib, re, textwrap, ruamel.yaml, pypandoc, shutil, os, sys
from datetime import date

from textwrap import dedent   # already imported earlier


import json, html  # add to your imports

_DOLLAR_INLINE = re.compile(r"\$(.+?)\$")
_DOLLAR_DISPLAY = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
import json

def render_quiz_block(idx: int, quiz_dir: pathlib.Path) -> str:
    """
    If mybook/content/quizzes/chapterNN.json exists, append a section:
      ## Vprašanja za ponovitev
      (for each question)
        ```{raw} html
        <div class="quiz-item" data-correct="true|false">
        ```
        …question text as normal Markdown (so $math$ renders)…
        </div>
    """
    path = quiz_dir / f"chapter{idx:02}.json"
    if not path.exists():
        return ""

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return (
            "```{admonition} Pozor\n"
            ":class: warning\n"
            f"Neveljaven JSON v `{path.as_posix()}`: {e}\n"
            "```\n"
        )

    blocks = ["## Kviz\n"]
    for q in data:
        text = str(q.get("question", "")).strip()
        answers = q.get("answers", [])
        correct = None
        for ans in answers:
            if ans.get("correct"):
                correct = str(ans.get("answer", ""))
                break

        # true/false → data-correct, otherwise stash label (if you ever need it later)
        if isinstance(correct, str) and correct.lower() in ("true", "false"):
            open_tag = f'<div class="quiz-item" data-correct="{correct.lower()}">'
        elif correct:
            open_tag = f'<div class="quiz-item" data-correct-label="{correct}">'
        else:
            open_tag = '<div class="quiz-item">'

        blocks.append(
            "```{raw} html\n" + open_tag + "\n```\n\n" +  # OPEN (raw HTML)
            text + "\n\n" +                                 # QUESTION (Markdown → MathJax works)
            "```{raw} html\n</div>\n```\n"                  # CLOSE (raw HTML)
        )

    return "\n".join(blocks)




# --- 0. helper -----------------------------------------------------------
def strip_preamble(tex_src: str) -> str:
    """
    Keep only the lines that come *after* \maketitle (inclusive).
    Everything before that is LaTeX boiler-plate we don’t need.
    """
    m = re.search(r'\\maketitle', tex_src)
    if not m:                        # safety-net: nothing to strip
        return tex_src
    return tex_src[m.end():]         # drop everything up to \maketitle

def make_title_block(today=None):
    """Return the HTML (or MyST-container) that should appear at the very top
    of intro.md.  The date is filled-in automatically unless you pass one in."""
    if today is None:
        today = date.today().strftime("%d. %m. %Y")   # 10. 11. 2022 → SLO style

    return dedent(f"""\
    ```{{raw}} html
    <div class="naslov">
    ```

    # Diskretne strukture
                  
    ```{{raw}} html
      <strong>Urban Jezernik<br>
      Univerza v Ljubljani, Fakulteta za matematiko in fiziko</strong><br>

      Zadnja posodobitev: {today}
    </div>
    ```
    """)                       # <-- triple-quoted string ends here

def style_block(chapter_idx: int) -> str:
    """
    Return a raw-HTML block that sets body {counter-reset: chapter N …}
    so that after h1 increments we end up with Chapter = chapter_idx.
    """
    # chapter counter starts at (idx-1) so h1 raises it to idx
    n = chapter_idx - 1
    return dedent(f"""\
        ```{{raw}} html
        <style>
          body {{ counter-reset: chapter {n} izrek 0 zgled 0 domacanaloga 0
                         lema 0 trditev 0 definicija 0 dokaz 0; }}
        </style>
        ```
    """)

def mark_definicija(tex_src: str) -> str:
    """
    Turn  {\definicija Besedilo}  or  \definicija{Besedilo}
    into a unique placeholder  @@DEF{Besedilo}@@  that Pandoc
    will copy verbatim.
    """
    tex_src = re.sub(
        r'\{\\definicija\s+([^{}]+?)\}',
        r'@@DEF{\1}@@',
        tex_src)
    tex_src = re.sub(
        r'\\definicija\{([^{}]+?)\}',
        r'@@DEF{\1}@@',
        tex_src)
    return tex_src

TEX_FILE   = pathlib.Path("ds.tex")       # <— adjust if needed
BOOK_DIR   = pathlib.Path("mybook")               # created earlier
CONTENT_DIR = BOOK_DIR / "content"                # keep Markdown here
CONTENT_DIR.mkdir(parents=True, exist_ok=True)

# Where to keep per-chapter quiz JSON files:
QUIZ_DIR = (BOOK_DIR / "content" / "quizzes")
QUIZ_DIR.mkdir(parents=True, exist_ok=True)

tex = TEX_FILE.read_text(encoding="utf-8")
# remove \begin{document} … \end{document}
tex = re.sub(r'\\begin{document}|\\end{document}', '', tex)

# 1️⃣  Split on \chapter{...}
parts = re.split(r'(?m)^(?=\\chapter)', tex)
# optional: drop anything before first \chapter — put it in intro later
front_matter, chapters_tex = parts[0], parts[1:]

# print(front_matter)  # debug: show first 1000 chars of front matter

# 2️⃣  Convert each chapter to MyST
chapter_entries = []
for idx, ch_tex in enumerate(chapters_tex, 1):
    # grab the chapter title between braces
    m = re.match(r'\\chapter\*?{([^}]*)}', ch_tex)
    title = m.group(1).strip() if m else f"Chapter {idx}"
    out_md = CONTENT_DIR / f"chapter{idx:02}.md"

    ch_tex = mark_definicija(ch_tex)
    # Pandoc ➜ MyST-Markdown
    md = pypandoc.convert_text(
        ch_tex,                       # (or front_matter)
        to="gfm+tex_math_dollars",    # keep rest of the pipeline the same
        format="latex",                    # ← run our dual-catch filter
        extra_args=["--wrap=none"]
    )
    out_md.write_text(md)          # <-- create chapterXX.md

    md = out_md.read_text()
    md = re.sub(r'\$`([^`]+)`\$', r'$\1$', md)   # kill back-ticks in inline math
    out_md.write_text(md)
    md = out_md.read_text()
    md = re.sub(
        r'@@DEF([^@]+?)@@',
        r'<span class="definicija">\1</span>',
        md)
    out_md.write_text(md)
    # --- post-process math fences → MyST {math} --------------------
    md = out_md.read_text()                             # read file just written
    # md = re.sub(r'^```math\b', '```{math}', md, flags=re.M)
    # md = re.sub(
    #     r'^```math\n([\\s\\S]+?)\n```',   # whole fence
    #     r'```{math}\n\\1\n```',           # MyST directive
    #     md, flags=re.M)
    md = re.sub(
        r'^(\s*)``` *math\s*\n'      # capture indent + ``` math
        r'([\s\S]+?)\n'              #   block contents (non-greedy)
        r'\s*```',                   #   closing fence
        r'\1```{math}\n\2\n\1```',   # same indent, MyST directive
        md, flags=re.M)
    out_md.write_text(md)                               # overwrite in place
        
    # Prepend YAML front matter first, then your style block and body
    md = style_block(idx) + "\n" + md

    quiz_block = render_quiz_block(idx, QUIZ_DIR)
    if quiz_block:
        md += "\n\n" + quiz_block

    out_md.write_text(md)


    chapter_entries.append({"file": str(out_md.relative_to(BOOK_DIR))})



# 3️⃣  Handle the pre-chapter material as “intro”
intro_md = BOOK_DIR / "intro.md"

front_body = strip_preamble(front_matter)

pypandoc.convert_text(
    front_body,
    to     = "gfm+tex_math_dollars",   # or "myst" if you prefer
    format = "latex",
    outputfile = str(intro_md),
    extra_args = ["--wrap=none"]
)

md = intro_md.read_text()

jsblock = """```{raw} html
<script defer>
  document.addEventListener('DOMContentLoaded', () => {
    if (!/intro\.html$/.test(window.location.pathname)) return;
    document
      .querySelectorAll('a.headerlink[href="#teorija-upodobitev"][title="Link to this heading"]')
      .forEach(el => el.remove());
    document.querySelectorAll('h2').forEach(h2 => {
      const h3 = document.createElement('h3');
      Array.from(h2.attributes).forEach(({name, value}) =>
        h3.setAttribute(name, value)
      );
      h3.innerHTML = h2.innerHTML;
      h2.replaceWith(h3);
    });
  });
</script>
```
"""

full_intro = make_title_block() + "\n" + md + "\n" + jsblock
intro_md.write_text(full_intro)

# --- apply the same post-processing we used for chapters -------------
md = intro_md.read_text()

# kill `$` \`code\` `$` that Pandoc inserts in inline math
md = re.sub(r'\$`([^`]+?)`\$', r'$\1$', md)

# restore coloured "definicija" spans
md = re.sub(r'@@DEF([^@]+?)@@', r'<span class="definicija">\1</span>', md)

# convert fenced blocks  ```math``` → ```{math}
md = re.sub(
    r'^(\s*)``` *math\s*\n'      # opening fence
    r'([\s\S]+?)\n'              # contents
    r'\s*```',                   # closing fence
    r'\1```{math}\n\2\n\1```',
    md, flags=re.M,
)

intro_md.write_text(md)

# 4️⃣  Write _toc.yml
toc = {
    "format": "jb-book",
    "root"  : "intro",
    "chapters": chapter_entries
}
yaml = ruamel.yaml.YAML()
with (BOOK_DIR / "_toc.yml").open("w") as f:
    yaml.dump(toc, f)

print("✅  Chapters written:", len(chapter_entries))
print("   Run  jupyter-book build mybook/  to test-build the site.")
