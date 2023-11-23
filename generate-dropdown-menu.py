import re
from bs4 import BeautifulSoup

def extract_toc_and_generate_navbar(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the TOC container
    toc_container = soup.find('div', class_='kazalo')

    toc_ul = toc_container.find('ul')  # Find the first ul within the TOC container
    if not toc_ul:
        return

    html_content = re.sub(r'<div class="kazalo">.*?</div>', '', html_content, flags=re.DOTALL)

    navbar_html = '<ul class="navbar-nav mr-auto">\n'

    # Loop through each main section in the TOC
    for main_section in toc_ul.find_all('li', recursive=False):
        section_title = main_section.find('a').text.strip()
        section_id = main_section.find('a')['href']

        navbar_html += f'<li class="nav-item dropdown">\n<a class="nav-link dropdown-toggle" href="#" id="{section_id}" role="button" data-bs-toggle="dropdown" aria-expanded="false">{section_title}</a>\n'
        navbar_html += f'<ul class="dropdown-menu" aria-labelledby="{section_id}">\n'

        # Add submenu items if they exist
        if main_section.find('ul'):
            for sub_section in main_section.find('ul').find_all('li'):
                sub_section_title = sub_section.find('a').text.strip()
                sub_section_id = sub_section.find('a')['href']
                navbar_html += f'<li><a class="dropdown-item" href="{sub_section_id}">{sub_section_title}</a></li>\n'

        navbar_html += '</ul>\n</li>\n'

    navbar_html += '</ul>'

    html_content = html_content.replace('<ul class="navbar-nav mr-auto" id="dynamic-toc">', navbar_html)

    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Example usage
html_file = 'index.html'
extract_toc_and_generate_navbar(html_file)
