"""Apply the shared footer, preserving other page content."""
from pathlib import Path
import re
from datetime import date
from scaffold_pages import PAGES

ROOT = Path(__file__).resolve().parent.parent
logo = (ROOT / 'winstar-logo.svg').read_text(encoding='utf-8')
logo = re.sub(r'fill="#[0-9a-fA-F]+"', 'fill="#ffffff"', logo)
(ROOT / 'static/images/winstar-logo-white.svg').write_text(logo, encoding='utf-8')

footer = f'''  <footer class="site-footer">
    <div class="footer-main">
      <div class="footer-brand">
        <a href="index.html" aria-label="Winstar Security Solutions home"><img src="static/images/winstar-logo-white.svg" width="320" height="180" alt="Winstar Security"></a>
        <p class="footer-tagline">For all your corporate &amp; private security needs</p>
        <p>Professional security solutions since 2001. People, technology and coordinated operations supporting protection for businesses, institutions and homes.</p>
      </div>
      <nav aria-label="Footer solutions">
        <h2>Our Solutions</h2>
        <ul>
          <li><a href="manned-guarding.html">Security Guards</a></li>
          <li><a href="cctv-surveillance.html">CCTV &amp; Surveillance</a></li>
          <li><a href="security-alarm-systems.html">Security Alarm Systems</a></li>
          <li><a href="access-control.html">Access Control</a></li>
          <li><a href="electric-fencing.html">Electric Fencing</a></li>
          <li><a href="aviation-security.html">Aviation Security</a></li>
          <li><a href="services.html">Explore All Solutions</a></li>
        </ul>
      </nav>
      <nav aria-label="Footer company">
        <h2>Company</h2>
        <ul>
          <li><a href="about_us.html">About Winstar</a></li>
          <li><a href="sectors.html">Who We Serve</a></li>
          <li><a href="contact_us.html">Contact Us</a></li>
        </ul>
      </nav>
      <section class="footer-contact" aria-labelledby="footer-contact-heading">
        <h2 id="footer-contact-heading">Contact</h2>
        <a class="footer-phone" href="tel:+254722535066">0722 535066</a>
        <a class="footer-phone" href="tel:+254734535066">0734 535066</a>
        <a class="footer-email" href="mailto:info@winstarsecurity.co.ke">info@winstarsecurity.co.ke</a>
        <address><strong>Mombasa Head Office</strong>Rozina House, Moi Avenue<br>Mombasa, Kenya</address>
        <address><strong>Nairobi Office</strong>Liberty Plaza, 4th Floor<br>Mombasa Road, Nairobi</address>
      </section>
    </div>
    <div class="footer-bottom">
      <p>&copy; {date.today().year} Winstar Security Solutions. All rights reserved.</p>
    </div>
  </footer>'''

for filename in PAGES:
    path = ROOT / filename
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'  <footer(?: class="site-footer")?>.*?</footer>', lambda _: footer, text, flags=re.S)
    if 'static/footer.css' not in text:
        text = text.replace('</head>', '  <link rel="stylesheet" href="static/footer.css">\n</head>')
    path.write_text(text, encoding='utf-8')
print(f'Applied footer to {len(PAGES)} pages; created white logo copy.')
