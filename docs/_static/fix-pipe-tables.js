//  _static/fix-pipe-tables.js
window.addEventListener('DOMContentLoaded', () => {

    /* helper – split a line on un-escaped pipes */
    const split = line =>
      line
        .replace(/\\\|/g, '§ESC§')      // protect “\|”
        .slice(1, -1)                   // trim leading / trailing |
        .split('|')
        .map(c => c.replace(/§ESC§/g, '|').trim());
  
    [...document.querySelectorAll('p')].forEach(p => {
      const raw = p.textContent.trim();
      const lines = raw.split('\n').map(l => l.trim());
  
      /* not a pipe table? */
      if (!raw.startsWith('|') ||
          lines.length < 2          ||
          !/^[:\-| ]+$/.test(lines[1])) return;
  
      /* ───── build the table ───── */
      const [headerLine, sepLine, ...bodyLines] = lines;
      const header = split(headerLine);
      const align  = split(sepLine).map(c =>
        c.startsWith(':') && c.endsWith(':') ? 'text-center' :
        c.endsWith(':')                      ? 'text-right'  : 'text-left');
  
      const wrapper = document.createElement('div');
      wrapper.className = 'table-responsive';         /* Bootstrappy scroll */
  
      const table = document.createElement('table');
      table.className = 'table table-striped table-hover table-sm';
      wrapper.append(table);
  
      /* THEAD */
      const thead = table.createTHead();
      const hrow  = thead.insertRow();
      header.forEach((h,i) => {
        const th = document.createElement('th');
        th.className = 'head ' + align[i];
        th.innerHTML = h;                 // ← keep TeX, lose nothing
        hrow.append(th);
      });
  
      /* TBODY */
      const tbody = table.createTBody();
      bodyLines.forEach((ln, r) => {
        if (!ln.trim()) return;
        const row = tbody.insertRow();
        split(ln).forEach((cell,i) => {
          const td = row.insertCell();
          td.className = align[i];
          td.innerHTML = cell;
        });
        row.className = r % 2 ? 'row-even' : 'row-odd';
      });
  
      p.replaceWith(wrapper);
  
      /* ask MathJax to render new cells */
      MathJax?.typesetPromise?.([wrapper]);
    });
  });
  