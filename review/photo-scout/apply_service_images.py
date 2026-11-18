from pathlib import Path
from PIL import Image,ImageOps
import re
r=Path('D:/Winstar website');out=r/'static/images/services';g=Path('C:/Users/Victor/.codex/generated_images/01a13352-b047-7881-bcec-6b1997725f55')
for src,name in [('exec-c97e8c4e-edc7-4925-b220-2d473fcbd911.png','cctv-technician-remix'),('exec-dadd3f66-2c81-4c4c-8d08-2b6f19f6183c.png','k9-search-remix'),('exec-fe2dd7a3-8b5a-4e7a-a6e2-b68683818bb1.png','control-room-refined')]:
    with Image.open(g/src) as im:
        im.convert('RGB').save(out/f'{name}.jpg',quality=91,optimize=True)
        im.thumbnail((1100,700));im.convert('RGB').save(r/f'review/photo-scout/{name}-preview.jpg',quality=88)
sources=[('Photo Gallery/WINSTAR PHOTOS/Resized/Winstar Security (168).jpg','team-briefing'),('Photo Gallery/WINSTAR PHOTOS 2/Resized/Winstar Security (98).jpg','response-deployment'),('Photo Gallery/WINSTAR PHOTOS 2/Resized/Winstar Security (175).jpg','response-fleet')]
for src,name in sources:
    with Image.open(r/src) as im:
        im=ImageOps.exif_transpose(im);im.thumbnail((1800,1400));im.convert('RGB').save(out/f'{name}.jpg',quality=90,optimize=True)
def replace_image(page,old,new,alt):
    p=r/page;s=p.read_text(encoding='utf-8')
    with Image.open(r/new) as im:w,h=im.size
    pattern=r'<img\b[^>]*src="'+re.escape(old)+r'"[^>]*>'
    found=re.search(pattern,s)
    if not found and new in s:return
    assert found,(page,old)
    tag=found[0];tag=tag.replace(old,new);tag=re.sub(r' width="\d+"','',tag);tag=re.sub(r' height="\d+"','',tag);tag=re.sub(r' alt="[^"]*"',f' alt="{alt}" width="{w}" height="{h}"',tag)
    s=s[:found.start()]+tag+s[found.end():];p.write_text(s,encoding='utf-8')
replace_image('manned-guarding.html','static/images/services/guard-team-hero-expanded.png','static/images/slider/winstar-guarding.jpg','Winstar guard at a building entrance, photograph remixed for the hero')
replace_image('manned-guarding.html','static/images/services/guard-at-entry.jpg','static/images/services/visitor-reception.jpg','Winstar reception officer assisting a visitor')
replace_image('canine-security.html','static/images/services/k9-hero-expanded.png','static/images/services/k9-search-remix.jpg','Winstar handler and dog checking a vehicle, photograph reframed for the hero')
replace_image('cctv-surveillance.html','static/images/services/cctv-installation.jpg','static/images/services/cctv-technician-remix.jpg','Winstar technician adjusting a CCTV camera, photograph remixed for the hero')
replace_image('security-alarm-systems.html','static/images/services/winstar-patrol-vehicle.jpg','static/images/services/control-room-refined.jpg','Winstar control-room operators handling communications, photograph refined for presentation')
replace_image('vip-cargo-escorts.html','static/images/services/winstar-patrol-vehicle.jpg','static/images/slider/winstar-response.jpg','Winstar personnel beside a branded vehicle, photograph remixed for presentation')
replace_image('services.html','static/images/services/guard-at-entry.jpg','static/images/services/team-briefing.jpg','Winstar supervisor briefing security personnel')
replace_image('services.html','static/images/services/cctv-installation.jpg','static/images/services/cctv-technician-remix.jpg','Winstar technician adjusting a camera, remixed photograph')
# Keep existing perimeter image unless explicitly selected: it is not verified electric-fence equipment.
p=r/'static/service-heroes.css';s=p.read_text(encoding='utf-8')
old=':is(.guarding-page,.k9-page,.access-hero-page,.aviation-page,.credential-page,.alarms-page,.events-page)'
s=s.replace(old,old[:-1]+',.cctv-page,.escorts-page)')
s+='\n/* Focal points for the November photographic replacements. */\n.guarding-page .guarding-hero figure img{object-position:74% 18%}\n.cctv-page .guarding-hero figure img{object-position:76% 35%}\n.k9-page .guarding-hero figure img{object-position:78% 40%}\n.escorts-page .guarding-hero figure img{object-position:66% 30%}\n@media(max-width:760px){.guarding-page .guarding-hero figure img{object-position:76% 20%}.cctv-page .guarding-hero figure img{object-position:77% center}.k9-page .guarding-hero figure img{object-position:80% center}.escorts-page .guarding-hero figure img{object-position:56% center}}\n'
p.write_text(s,encoding='utf-8')
p=r/'static/home.css';s=p.read_text(encoding='utf-8');s+='\n/* Winstar photographic slider: retain subject placement through the zoom. */\n.hero-slide:nth-child(1) .hero-image{object-position:74% 42%;transform-origin:74% 42%}\n.hero-slide:nth-child(2) .hero-image{object-position:66% 55%;transform-origin:66% 55%}\n.hero-slide:nth-child(3) .hero-image{object-position:65% 54%;transform-origin:65% 54%}\n@media(max-width:600px){.hero-slide:nth-child(1) .hero-image{object-position:75% center}.hero-slide:nth-child(2) .hero-image{object-position:59% center}.hero-slide:nth-child(3) .hero-image{object-position:49% center}}\n';p.write_text(s,encoding='utf-8')
print('Service and supporting photographs applied; focal points configured.')
