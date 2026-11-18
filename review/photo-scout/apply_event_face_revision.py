from pathlib import Path
from PIL import Image
r=Path('D:/Winstar website')
src=Path('C:/Users/Victor/.codex/generated_images/01a13352-b047-7881-bcec-6b1997725f55/exec-2cefda35-b4bb-45ae-a443-f1431324e73f.png')
with Image.open(src) as im:
    assert im.size==(2172,724)
    im.convert('RGB').save(r/'static/images/services/event-winstar-guards-v2.jpg',quality=93,optimize=True)
p=r/'event-security.html';s=p.read_text(encoding='utf-8');assert 'event-winstar-guards.jpg' in s;s=s.replace('event-winstar-guards.jpg','event-winstar-guards-v2.jpg');p.write_text(s,encoding='utf-8')
print('Revised event guard image saved and applied.')
