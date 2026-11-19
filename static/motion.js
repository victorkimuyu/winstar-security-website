// Start each reveal on entry. Content is visible before the observer runs.
if ('IntersectionObserver' in window && typeof Element.prototype.animate === 'function') {
  const motion = window.matchMedia('(prefers-reduced-motion: no-preference)');
  const active = new Set();
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      const element = entry.target;
      observer.unobserve(element);
      if (!motion.matches || element.matches(':focus-within')) continue;
      const animation = element.animate([
        { opacity: 0.45, transform: 'translateY(26px)' },
        { opacity: 1, transform: 'translateY(0)' }
      ], { duration: 520, easing: 'ease-out' });
      active.add(animation);
      animation.finished.then(() => active.delete(animation), () => active.delete(animation));
    }
  }, { threshold: 0.05, rootMargin: '0px 0px -6% 0px' });

  const selector = [
    'h2', 'h2 + p', 'article', '.solutions-questions details', '.solutions-enquiry',
    '.k9-roles-intro', '.k9-handler-grid', '.k9-deployment-steps li',
    '.alarms-response-steps li', '.sector-summary', '.sector-photo', '.sector-priorities > div',
    '.company-facts dl > div', '.company-credentials dl > div', '.office-addresses'
  ].join(', ');
  const blocks = document.querySelectorAll('main :is(' + selector + ')');
  for (const block of blocks) {
    if (block.closest('.hero-slider, form, dialog') || block.parentElement.closest(selector)) continue;
    observer.observe(block);
  }
  motion.addEventListener('change', () => {
    if (!motion.matches) for (const animation of active) animation.cancel();
  });
}
