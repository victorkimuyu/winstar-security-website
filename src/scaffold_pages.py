"""Create the agreed buildless HTML page shells without replacing authored pages."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
PAGES = {
    'index.html': ('Home', ['Hero: Main Introduction, Capacity, Differentiator', 'Services Overview', 'Experience & Sector Expertise', 'Client Logos']),
    'services.html': ('Services', ['Manned Security', 'Electronic Security', 'Access Control', 'Featured: Electric Fencing and Aviation Security']),
    'manned-guarding.html': ('Security Guards', []),
    'canine-security.html': ('K9 Security Dogs', []),
    'event-security.html': ('Event Security', []),
    'vip-cargo-escorts.html': ('VIP & Cargo Escorts', []),
    'cctv-surveillance.html': ('CCTV Cameras & Surveillance', []),
    'biometric-card-access.html': ('Biometric & Card-Based Access', []),
    'security-alarm-systems.html': ('Security Alarm Systems', []),
    'access-control.html': ('Access Control', ['Turnstiles, Bollards, Vehicle Barriers and Related Equipment']),
    'electric-fencing.html': ('Electric Fencing', []),
    'aviation-security.html': ('Aviation Security', []),
    'sectors.html': ('Who We Serve', []),
    'about_us.html': ('About Winstar', []),
    'social-responsibility.html': ('Social Responsibility', []),
    'policies-commitments.html': ('Policies & Commitments', ['Ethical Business Conduct', 'Human Rights & Workplace Respect', 'Health & Safety', 'Service Quality & Continuity']),
    'contact_us.html': ('Contact Us', []),
    'data-protection-policy.html': ('Data Protection Policy', []),
    'privacy-notice.html': ('Privacy Notice', []),
    'terms-of-use.html': ('Terms of Use', []),
}

for filename, (title, sections) in PAGES.items():
    target = ROOT / filename
    if target.exists() and target.stat().st_size:
        continue
    section_html = '\n'.join(
        f'    <!-- Planned section: {escape(section)} -->' for section in sections
    ) or '    <!-- Page sections and copy to be agreed. -->'
    target.write_text(f'''<!doctype html>
<html lang="en-KE">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} | Winstar Security Solutions</title>
</head>
<body>
  <a href="#main-content">Skip to content</a>
  <header>
    <!-- Shared navigation and mega menus to be implemented. -->
  </header>
  <main id="main-content">
    <h1>{escape(title)}</h1>
{section_html}
  </main>
  <footer>
    <!-- Shared footer to be implemented. -->
  </footer>
</body>
</html>
''', encoding='utf-8')

print(f'Checked {len(PAGES)} page scaffolds.')
