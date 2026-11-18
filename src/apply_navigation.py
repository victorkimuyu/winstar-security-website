"""Apply the shared navigation to agreed root pages; preserve their main content."""
from pathlib import Path
import re
from html import escape
from scaffold_pages import PAGES

ROOT = Path(__file__).resolve().parent.parent
groups = {
    'Manned Security': [('manned-guarding.html','Security Guards'),('canine-security.html','K9 Security Dogs'),('event-security.html','Event Security'),('vip-cargo-escorts.html','VIP & Cargo Escorts'),('aviation-security.html','Aviation Security')],
    'Electronic Security': [('cctv-surveillance.html','CCTV Cameras & Surveillance'),('biometric-card-access.html','Biometric & Card-Based Access'),('security-alarm-systems.html','Security Alarm Systems')],
    'Access Control': [('access-control.html','Turnstiles, Bollards & Barriers'),('electric-fencing.html','Electric Fencing')],
}
sectors = [
    ('banking-financial.html','Banking & Financial','Security for financial institutions.'),
    ('hotel-recreation.html','Hotel & Recreation','Protection with a welcoming presence.'),
    ('real-estate-domestic.html','Real Estate & Domestic','Security for properties and homes.'),
    ('education.html','Education','Safer learning environments.'),
    ('aviation-travel.html','Aviation & Travel','Security for aviation and travel operations.'),
    ('logistics-warehousing.html','Logistics & Warehousing','Protection for goods, sites and movements.'),
]
company = [('about_us.html','About Winstar'),('social-responsibility.html','Social Responsibility'),('policies-commitments.html','Policies & Commitments')]
service_files = {file for items in groups.values() for file,_ in items} | {'services.html','electric-fencing.html','aviation-security.html'}
sector_files = {file for file,_,_ in sectors} | {'sectors.html'}

def link(file, label, current, cls=''):
    active = ' aria-current="page"' if file == current else ''
    return f'<a href="{file}" class="{cls}"{active}>{escape(label)}</a>'

def arrow():
    return '<img class="hover-arrow" src="static/images/icons/arrow-right.svg" width="18" height="18" alt="" aria-hidden="true">'

def service_link(file, label, current):
    active = ' aria-current="page"' if file == current else ''
    return f'<a class="service-link" href="{file}"{active}>{arrow()}<span>{escape(label)}</span></a>'

def header(current):
    columns = ''.join('<section class="menu-group"><div class="solution-image-placeholder" aria-hidden="true"></div><h2>'+escape(title)+'</h2><ul>'+''.join('<li>'+service_link(file,label,current)+'</li>' for file,label in items)+'</ul></section>' for title,items in groups.items())
    sector_links = ''.join(f'<a class="sector-link" href="{file}"'+(' aria-current="page"' if file==current else '')+f'><span class="sector-icon-placeholder" aria-hidden="true"></span><div class="sector-copy"><strong><span>{escape(title)}</span>{arrow()}</strong><span>{escape(description)}</span></div></a>' for file,title,description in sectors)
    company_links = ''.join('<li>'+link(file,label,current)+'</li>' for file,label in company)
    return f'''  <header class="site-header">

    <div class="navigation-row"><div class="nav-shell">
      <a class="brand" href="index.html" aria-label="Winstar Security Solutions home"><img src="winstar-logo.svg" width="320" height="180" alt="Winstar Security"></a>
      <button class="mobile-toggle" type="button" aria-label="Toggle navigation" aria-controls="site-navigation" aria-expanded="false"><span aria-hidden="true">☰</span></button>
      <nav class="site-nav" id="site-navigation" aria-label="Main navigation">
        {link('index.html','HOME',current,'nav-link')}
        <details class="menu{' is-current' if current in service_files else ''}">
          <summary>OUR SOLUTIONS <span class="chevron" aria-hidden="true"></span></summary>
          <div class="menu-panel">
            <div class="panel-heading"><span>Security solutions for your people, property and operations.</span>{link('services.html','Explore All Services →',current,'overview-link')}</div>
            <div class="menu-columns">{columns}</div>
          </div>
        </details>
        <details class="menu{' is-current' if current in sector_files else ''}">
          <summary>WHO WE SERVE <span class="chevron" aria-hidden="true"></span></summary>
          <div class="menu-panel">
            <div class="panel-heading"><span>Protection shaped around your environment.</span>{link('sectors.html','Explore All Sectors →',current,'overview-link')}</div>
            <div class="sector-grid">{sector_links}</div>
          </div>
        </details>
        <details class="menu{' is-current' if current in dict(company) else ''}">
          <summary>COMPANY <span class="chevron" aria-hidden="true"></span></summary>
          <div class="menu-panel company-panel"><ul>{company_links}</ul></div>
        </details>
        {link('contact_us.html','CONTACT US',current,'nav-link')}
        <a class="quote-button" href="contact_us.html?enquiry=quote">REQUEST FOR QUOTE</a>

      </nav>
    </div></div>
  </header>'''

for filename in PAGES:
    path = ROOT / filename
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'  <header(?: class="site-header")?>.*?</header>', lambda _: header(filename), text, flags=re.S)
    text = text.replace('<a href="#main-content">', '<a class="skip-link" href="#main-content">')
    if 'static/navigation.css' not in text:
        text = text.replace('</head>', '  <link rel="icon" href="favicon.svg" type="image/svg+xml">\n  <link rel="stylesheet" href="static/navigation.css">\n  <script src="static/navigation.js" defer></script>\n</head>')
    if 'static/typography.css' not in text:
        text = text.replace('</head>', '  <link rel="stylesheet" href="static/typography.css">\n</head>')
    path.write_text(text, encoding='utf-8')
print(f'Applied shared navigation to {len(PAGES)} pages.')
