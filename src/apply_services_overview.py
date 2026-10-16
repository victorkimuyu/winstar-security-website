from pathlib import Path
root = Path(__file__).resolve().parent.parent
p = root / 'index.html'
text = p.read_text(encoding='utf-8')
section = '''    <section class="services-overview" aria-labelledby="services-overview-title">
      <h2 id="services-overview-title">PROACTIVE PROTECTION <span class="overview-title-secondary">TAILORED FOR YOUR BUSINESS AND OPERATIONS</span></h2>
      <div class="services-overview-copy">
        <p>Protecting your business and property takes a combination of personnel, technology and strategy. Winstar brings together trained guards, surveillance, access control and alarm response to provide security shaped around your premises and daily operations.</p>
        <a class="overview-cta" href="services.html">Explore Our Solutions <img src="static/images/icons/chevron-right.svg" width="18" height="18" alt="" aria-hidden="true"></a>
      </div>
    </section>
    <!-- Next: Experience & Sector Expertise, Client Logos. -->'''
marker = '    <!-- Next: Services overview, Experience & Sector Expertise, Client Logos. -->'
assert marker in text
p.write_text(text.replace(marker, section), encoding='utf-8')
