from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter,ImageChops,ImageOps
import re
r=Path('D:/Winstar website')
src=r/'Photo Gallery/WINSTAR PHOTOS 2/Resized/Winstar Security (6).jpg'
gen=Path('C:/Users/Victor/.codex/generated_images/01a13352-b047-7881-bcec-6b1997725f55/exec-154a08d5-5599-44d1-af44-82098037fc5f.png')
original=ImageOps.exif_transpose(Image.open(src)).convert('RGB');original.thumbnail((1800,1200));w,h=original.size
edit=Image.open(gen).convert('RGB').resize(original.size,Image.Resampling.LANCZOS)
mask=Image.new('L',original.size);d=ImageDraw.Draw(mask)
for a,b,c,e in [(0.607,.273,.837,.638),(.291,.297,.414,.451)]:d.rounded_rectangle((int(a*w),int(b*h),int(c*w),int(e*h)),radius=8,fill=255)
mask=mask.filter(ImageFilter.GaussianBlur(3));result=Image.composite(edit,original,mask)
outside=Image.composite(Image.new('RGB',original.size),ImageChops.difference(result,original),mask.point(lambda v:255 if v else 0));assert outside.getbbox() is None
dest=r/'static/images/services/alarm-response-radio-anonymous.webp';result.save(dest,lossless=True,method=6)
p=r/'security-alarm-systems.html';s=p.read_text(encoding='utf-8');pattern=r'<img src="static/images/services/alarm-siren-hero.png"[^>]+>';assert re.search(pattern,s)
s=re.sub(pattern,f'<img src="static/images/services/alarm-response-radio-anonymous.webp" width="{w}" height="{h}" alt="Winstar response personnel inside a vehicle, communicating by radio; faces anonymised" fetchpriority="high">',s,count=1);p.write_text(s,encoding='utf-8')
preview=ImageOps.fit(result,(1100,336),centering=(.65,.49));preview.save(r/'review/photo-scout/alarm-radio-crop.jpg',quality=90)
print('Applied radio-response hero. Outside-face pixels preserved. Image:',w,h)
