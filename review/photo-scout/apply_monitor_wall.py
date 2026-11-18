from pathlib import Path
from PIL import Image,ImageOps
import re
r=Path('D:/Winstar website')
src=r/'Photo Gallery/WINSTAR PHOTOS 2/Resized/Winstar Security (105).JPG'
with Image.open(src) as im:
    im=ImageOps.exif_transpose(im).convert('RGB')
    im=ImageOps.fit(im,(1600,914),centering=(.5,.48))
    im.save(r/'static/images/services/control-room-monitor-wall.jpg',quality=92,optimize=True)
    im.thumbnail((1000,700));im.save(r/'review/photo-scout/monitor-wall-preview.jpg',quality=90)
p=r/'security-alarm-systems.html';s=p.read_text(encoding='utf-8')
pattern=r'(<figure class="alarms-response-photo">)<img[^>]+>'
assert re.search(pattern,s)
s=re.sub(pattern,r'\1<img src="static/images/services/control-room-monitor-wall.jpg" width="1600" height="914" alt="Winstar control-room operators reviewing surveillance feeds on wall-mounted monitors" loading="lazy">',s,count=1)
p.write_text(s,encoding='utf-8')
print('Applied monitor-wall photograph; landscape crop 1600 by 914.')
