from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
slides = [
    ('corporate-building.jpg', 'Winstar Security Solutions', 'For all your corporate &amp; Private Security needs', 'Professional guarding and connected security solutions for your people, property and operations.', 'services.html', 'Explore Our Solutions'),
    ('workplace.jpg', 'Experience across sectors', 'Protection shaped around your world', 'From businesses and learning institutions to homes, hospitality and logistics, every environment has its own security needs.', 'sectors.html', 'Who We Serve'),
    ('office.jpg', 'Professional security since 2001', 'People. Systems. Dependable protection.', 'Trained personnel, operational supervision and coordinated support form the foundation of Winstar’s approach to security.', 'about_us.html', 'About Winstar'),
]
parts = []
for i, (image, eyebrow, title, description, target, cta) in enumerate(slides):
    tag = 'h1' if i == 0 else 'h2'
    parts.append(f'''      <section class="hero-slide" role="group" aria-roledescription="slide" aria-label="{i+1} of 3"{'' if i == 0 else ' hidden'}>
        <img class="hero-image" src="static/images/slider/{image}" alt="" {'fetchpriority="high"' if i == 0 else 'loading="lazy"'}>
        <div class="hero-content">

          <{tag}>{title}</{tag}>
          <p class="hero-description">{description}</p>
          <a class="hero-cta" href="{target}">{cta} <img class="hero-cta-chevron" src="static/images/icons/chevron-right.svg" width="18" height="18" alt="" aria-hidden="true"></a>
        </div>
      </section>''')
hero = '''  <main id="main-content" class="home-main">
    <div class="hero-slider" role="region" aria-roledescription="carousel" aria-label="Discover Winstar">
''' + '\n'.join(parts) + '''
      <div class="slider-controls">


        <div class="slider-dots" aria-label="Choose slide">
          <button type="button" data-slide="0" aria-label="Show slide 1" aria-current="true"></button>
          <button type="button" data-slide="1" aria-label="Show slide 2" aria-current="false"></button>
          <button type="button" data-slide="2" aria-label="Show slide 3" aria-current="false"></button>
        </div>

      </div>
    </div>
    <!-- Next: Services overview, Experience & Sector Expertise, Client Logos. -->
  </main>'''
p = root / 'index.html'
text = p.read_text(encoding='utf-8')
text = re.sub(r'  <main\b.*?</main>', lambda _: hero, text, flags=re.S)
if 'static/home.css' not in text:
    text = text.replace('</head>', '  <link rel="stylesheet" href="static/home.css">\n  <script src="static/home.js" defer></script>\n</head>')
p.write_text(text, encoding='utf-8')
print('Homepage hero applied.')
