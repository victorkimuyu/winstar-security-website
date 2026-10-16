(() => {
  const slider = document.querySelector('.hero-slider');
  if (!slider) return;
  const header = document.querySelector('.site-header');
  const syncHeaderHeight = () => {
    slider.style.setProperty('--header-height', `${header?.getBoundingClientRect().height || 0}px`);
  };
  syncHeaderHeight();
  if (header) new ResizeObserver(syncHeaderHeight).observe(header);
  const slides = [...slider.querySelectorAll('.hero-slide')];
  const dots = [...slider.querySelectorAll('[data-slide]')];
  let current = 0;
  let timer;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  let contentAnimations = [];
  const show = index => {
    contentAnimations.forEach(animation => animation.cancel());
    contentAnimations = [];
    current = (index + slides.length) % slides.length;
    slides.forEach((slide, i) => { slide.hidden = i !== current; });
    dots.forEach((dot, i) => dot.setAttribute('aria-current', String(i === current)));
    if (!reduced.matches) {
      const slide = slides[current];
      const image = slide.querySelector('.hero-image');
      if (image) contentAnimations.push(image.animate(
        [{ transform: 'scale(1)' }, { transform: 'scale(1.10)' }],
        { duration: 15000, easing: 'linear', fill: 'both' }
      ));
      const elements = [slide.querySelector('h1, h2'), slide.querySelector('.hero-description'), slide.querySelector('.hero-cta')];
      elements.forEach((element, i) => {
        if (!element) return;
        contentAnimations.push(element.animate(
          [{ opacity: 0, transform: 'translateY(16px)' },
           { opacity: 1, transform: 'translateY(0)' }],
          { duration: 1000, delay: i * 500, easing: 'ease-out', fill: 'both' }
        ));
      });
    }
  };
  const stop = () => clearInterval(timer);
  const start = () => {
    stop();
    if (!document.hidden) {
      timer = setInterval(() => show(current + 1), 15000);
    }
  };
  dots.forEach(dot => dot.addEventListener('click', () => {
    show(Number(dot.dataset.slide));
    start();
  }));
  document.addEventListener('visibilitychange', start);
  show(0);
  start();
})();
