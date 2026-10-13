(() => {
  const nav = document.querySelector('.site-nav');
  const toggle = document.querySelector('.mobile-toggle');
  const menus = [...document.querySelectorAll('.menu')];
  const mobile = window.matchMedia('(max-width: 1050px)');
  const closeMenus = () => menus.forEach(menu => { menu.open = false; });
  const syncLayout = () => {
    closeMenus();
    nav.hidden = mobile.matches;
    toggle.setAttribute('aria-expanded', 'false');
  };
  syncLayout();
  mobile.addEventListener('change', syncLayout);
  toggle.addEventListener('click', () => {
    nav.hidden = !nav.hidden;
    toggle.setAttribute('aria-expanded', String(!nav.hidden));
    if (nav.hidden) closeMenus();
  });
  menus.forEach(menu => {
    const panel = menu.querySelector('.menu-panel');
    let reveal;
    menu.querySelector('summary').addEventListener('click', event => {
      menus.forEach(other => { if (other !== menu) other.open = false; });
      if (!panel) return;
      event.preventDefault();
      reveal?.cancel();
      if (menu.open) {
        menu.open = false;
        return;
      }
      // Start the fade in the same task as opening, before the first paint.
      // An asynchronous toggle handler can briefly expose the panel first.
      menu.open = true;
      if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        reveal = panel.animate(
          [{ opacity: 0, transform: 'translateY(-6px)' },
           { opacity: 1, transform: 'translateY(0)' }],
          { duration: 160, easing: 'ease-out' }
        );
      }
    });
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.menu')) closeMenus();
  });
  document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    const openMenu = menus.find(menu => menu.open);
    if (openMenu) {
      openMenu.open = false;
      openMenu.querySelector('summary').focus();
    } else if (mobile.matches && !nav.hidden) {
      nav.hidden = true;
      toggle.setAttribute('aria-expanded', 'false');
      toggle.focus();
    }
  });
})();
