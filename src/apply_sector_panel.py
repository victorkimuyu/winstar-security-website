from pathlib import Path
root = Path(__file__).resolve().parent.parent
sectors = [
 ('banking-financial.html','Banking &amp; Financial','bank.svg','Professional protection for people, premises and financial operations.'),
 ('hotel-recreation.html','Hotel &amp; Recreation','hospitality.svg','A reassuring security presence that supports the guest experience.'),
 ('real-estate-domestic.html','Real Estate &amp; Domestic','property.svg','Controlled access and protection for properties, residents and visitors.'),
 ('education.html','Education','school.svg','A vigilant, welcoming presence for students, staff and visitors.'),
 ('aviation-travel.html','Aviation &amp; Travel','aeroplane.svg','Professional security for busy terminals and sensitive environments.'),
 ('logistics-warehousing.html','Logistics &amp; Warehousing','warehouse.svg','Protection for goods, facilities and movements through your operation.'),
]
cards = '\n'.join(f'''        <a class="sector-card" href="{url}">
          <img class="sector-card-icon" src="static/images/icons/{icon}" width="36" height="36" alt="">
          <h3>{title}</h3><p>{copy}</p>
          <span class="sector-card-action">Explore sector <img src="static/images/icons/chevron-right.svg" width="16" height="16" alt="" aria-hidden="true"></span>
        </a>''' for url,title,icon,copy in sectors)
panel = '''    <section class="experience-panel" aria-labelledby="experience-title">
      <div class="experience-inner">
        <div class="experience-intro">
          <div class="experience-image"><img src="static/images/slider/corporate-building.jpg" alt="" loading="lazy"></div>
          <div class="experience-text">
          <div>
          <h2 id="experience-title">Diverse environments.<br>One commitment to protection.</h2></div>
          <div class="experience-copy"><p>Providing professional security solutions since 2001, Winstar understands that each environment brings its own priorities. We shape protection around the people, premises and daily activities that make your operation unique.</p>
          <a class="overview-cta" href="sectors.html">Who We Serve <img src="static/images/icons/chevron-right.svg" width="18" height="18" alt="" aria-hidden="true"></a></div>
          </div>
        </div>

      </div>
    </section>
    <!-- Next: Client Logos. -->'''
p=root/'index.html'
t=p.read_text(encoding='utf-8')
marker='    <!-- Next: Experience & Sector Expertise, Client Logos. -->'
assert marker in t
p.write_text(t.replace(marker,panel),encoding='utf-8')
print('Added Experience & Sector Expertise panel.')
