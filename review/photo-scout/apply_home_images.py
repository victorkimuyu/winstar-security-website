from pathlib import Path
from PIL import Image,ImageOps
r=Path('D:/Winstar website');g=Path('C:/Users/Victor/.codex/generated_images/01a13352-b047-7881-bcec-6b1997725f55')
items=[('exec-71f0de39-7c33-4711-98b0-6b3d13f692e6.png','winstar-guarding'),('exec-9f1a0bcb-299c-4392-8a59-24097079db30.png','winstar-site-security'),('exec-90f6238f-bdfb-48e4-b9e3-e392d3e1bdd6.png','winstar-response')]
for src,name in items:
    with Image.open(g/src) as im:
        im.convert('RGB').save(r/f'static/images/slider/{name}.jpg',quality=91,optimize=True)
        im.thumbnail((1100,600));im.convert('RGB').save(r/f'review/photo-scout/{name}-preview.jpg',quality=88)
p=r/'index.html';s=p.read_text(encoding='utf-8')
for old,new in [('corporate-building','winstar-guarding'),('workplace','winstar-site-security'),('office','winstar-response')]:
    target=f'class="hero-image" src="static/images/slider/{old}.jpg"'
    assert target in s
    s=s.replace(target,f'class="hero-image" src="static/images/slider/{new}.jpg"',1)
# Use an authentic visitor interaction for sector content below the hero.
src=r/'Photo Gallery/WINSTAR PHOTOS 2/Resized/Winstar Security (148).jpg'
with Image.open(src) as im:
    im=ImageOps.exif_transpose(im);im.thumbnail((1600,1200));im.convert('RGB').save(r/'static/images/services/visitor-reception.jpg',quality=90,optimize=True)
s=s.replace('class="experience-image"><img src="static/images/slider/corporate-building.jpg" alt=""','class="experience-image"><img src="static/images/services/visitor-reception.jpg" alt="Winstar reception officer assisting a visitor"',1)
p.write_text(s,encoding='utf-8')
print('Homepage slider and experience photograph replaced.')
