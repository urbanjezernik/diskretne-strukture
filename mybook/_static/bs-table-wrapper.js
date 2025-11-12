window.addEventListener('DOMContentLoaded', () => {
  document
    .querySelectorAll('div.pst-scrollable-table-container')
    .forEach(old => {
      const table = old.querySelector('table');
      if (!table) return;                      // defensive
      
      const wrapper = document.createElement('div');
      wrapper.className = 'table-responsive';  // Bootstrap class
      wrapper.appendChild(table);              // move <table> inside

      old.replaceWith(wrapper);                // drop the old div
    });
});