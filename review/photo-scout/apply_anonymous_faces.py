from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter,ImageChops,ImageOps
import json
r=Path('D:/Winstar website');g=Path('C:/Users/Victor/.codex/generated_images/01a13352-b047-7881-bcec-6b1997725f55')
# Integrate tool-generated face regions into source pixels, preserving the rest.
items=[
('static/images/slider/winstar-guarding.jpg','exec-c3fb8d51-b93e-4f3e-963d-601b3a83b5eb.png',[(.714,.18,.769,.292)]),
('static/images/slider/winstar-site-security.jpg','exec-3596fdf2-1221-42e8-8b74-ea89e267ba71.png',None),
('static/images/slider/winstar-response.jpg','exec-1fe03e79-5ffc-458d-b52f-d3e2a8c8daa2.png',[(.389,.325,.441,.416),(.508,.302,.558,.408)]),
('static/images/services/cctv-technician-remix.jpg','exec-66035533-6b04-4557-bf9c-6f4ee2e75a7d.png',[(.797,.239,.943,.60)]),
('static/images/services/k9-search-remix.jpg','exec-d956b0ec-a341-4eb3-a029-3eae25f87b46.png',[(.71,.164,.768,.307)]),
('static/images/services/control-room-refined.jpg','exec-4d67804a-d92d-43ca-b5cb-46f9ae65c2fd.png',[(.524,.155,.642,.397),(.638,.194,.747,.431)]),
('static/images/services/visitor-reception.jpg','exec-c0110485-8e41-4fcd-a7fe-5e4f66c73b6e.png',[(.201,.169,.357,.418),(.695,.283,.839,.511)]),
('static/images/services/team-briefing.jpg','exec-20543095-ae65-4cd6-b48b-1da8ba9c3c88.png',[(.116,.054,.267,.29),(.283,.246,.369,.382),(.413,.219,.512,.393),(.559,.218,.68,.383),(.785,.075,.961,.351)])
]
replacements={};audit=[]
for src,generated,boxes in items:
    original=Image.open(r/src).convert('RGB');edit=Image.open(g/generated).convert('RGB').resize(original.size,Image.Resampling.LANCZOS)
    w,h=original.size
    if boxes is None:
        result=edit;outside_verified=False
    else:
        mask=Image.new('L',original.size);draw=ImageDraw.Draw(mask)
        for a,b,c,d in boxes:draw.rounded_rectangle((round(a*w),round(b*h),round(c*w),round(d*h)),radius=8,fill=255)
        mask=mask.filter(ImageFilter.GaussianBlur(3))
        result=Image.composite(edit,original,mask)
        # All pixels beyond the bounded face-mask support must match source.
        support=mask.point(lambda p:255 if p else 0)
        diff=ImageChops.difference(result,original)
        outside=Image.composite(Image.new('RGB',original.size),diff,support)
        assert outside.getbbox() is None
        outside_verified=True
    dest=Path(src).with_name(Path(src).stem+'-anonymous.webp')
    result.save(r/dest,'WEBP',lossless=True,method=6)
    if 'winstar-response' in src:
        # Entire vehicle body below the faces remains pixel-identical.
        reopened=Image.open(r/dest).convert('RGB')
        assert ImageChops.difference(reopened.crop((0,int(.45*h),w,h)),original.crop((0,int(.45*h),w,h))).getbbox() is None
    replacements[src]=dest.as_posix()
    audit.append(dict(source=src,output=dest.as_posix(),face_regions=boxes,outside_faces_pixel_identical=outside_verified,exception='Slide 2: car paint, face complexion, glasses and hair' if boxes is None else None))
for p in r.glob('*.html'):
    s=p.read_text(encoding='utf-8');old=s
    for a,b in replacements.items():s=s.replace(a,b)
    if s!=old:p.write_text(s,encoding='utf-8')
(r/'review/photo-scout/anonymisation-audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
sheet=Image.new('RGB',(1200,4*260),'#eee');d=ImageDraw.Draw(sheet)
for i,x in enumerate(audit):
    with Image.open(r/x['output']) as im:
        im.thumbnail((590,230));sheet.paste(im,((i%2)*600,(i//2)*260))
    d.text(((i%2)*600+4,(i//2)*260+233),Path(x['output']).name,fill='black')
sheet.save(r/'review/photo-scout/anonymous-review.jpg',quality=90)
print('Applied eight anonymised assets. Face-only preservation checks passed; Winstar vehicle body pixel check passed.')
