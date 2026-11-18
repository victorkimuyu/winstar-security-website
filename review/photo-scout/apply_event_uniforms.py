from pathlib import Path
from PIL import Image
import re
r=Path('D:/Winstar website')
g=Path('C:/Users/Victor/.codex/generated_images/01a13352-b047-7881-bcec-6b1997725f55/exec-a7ab8ace-07a3-4f8c-a0a9-f86879e8b072.png')
with Image.open(g) as im:
    w,h=im.size;im.convert('RGB').save(r/'static/images/services/event-winstar-guards.jpg',quality=93,optimize=True)
p=r/'event-security.html';s=p.read_text(encoding='utf-8')
s=re.sub(r'<img src="static/images/services/(?:event-golf-banner.jpg|event-security-hero.png|event-winstar-guards.jpg)"[^>]*>',f'<img src="static/images/services/event-winstar-guards.jpg" width="{w}" height="{h}" alt="Illustration of Winstar-uniformed guards welcoming guests at an event entrance" fetchpriority="high">',s,count=1)
assert 'event-winstar-guards.jpg' in s;p.write_text(s,encoding='utf-8')
p=r/'static/service-heroes.css';s=p.read_text(encoding='utf-8')
# Restore original text alignment and dark overlay direction for the event scene.
s+='\n/* Event entrance: text left, staff and guest interaction right. */\n.events-page .guarding-hero figure img{object-position:75% center}\n.events-page .guarding-hero .guarding-hero-copy{margin-left:0}\n.events-page .guarding-hero .page-breadcrumb{justify-content:flex-start}\n.events-page .guarding-hero:after{background:linear-gradient(90deg,rgba(25,28,64,.88),rgba(25,28,64,.6) 42%,rgba(25,28,64,.08) 75%)}\n@media(max-width:760px){.events-page .guarding-hero figure img{object-position:80% center}.events-page .guarding-hero:after{background:linear-gradient(90deg,rgba(25,28,64,.9),rgba(25,28,64,.65))}}\n'
p.write_text(s,encoding='utf-8');print('Revised event entrance saved and applied.',w,h)
