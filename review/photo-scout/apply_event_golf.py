from pathlib import Path
from PIL import Image
import re
r=Path('D:/Winstar website')
src=r/'Photo Gallery/WINSTAR PHOTOS/Resized/_CBM0052.jpg'
dest=r/'static/images/services/event-golf-banner.jpg'
with Image.open(src) as im:
    w,h=im.size
    im.convert('RGB').save(dest,quality=94,optimize=True)
p=r/'event-security.html';s=p.read_text(encoding='utf-8')
pattern=r'<img src="static/images/services/event-security-hero.png"[^>]+>'
assert re.search(pattern,s)
s=re.sub(pattern,f'<img src="static/images/services/event-golf-banner.jpg" width="{w}" height="{h}" alt="Winstar blade banner beside the course at a golfing event" fetchpriority="high">',s,count=1)
p.write_text(s,encoding='utf-8')
print('Applied golfing-event photograph:',w,h)
