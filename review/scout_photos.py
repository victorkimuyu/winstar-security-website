from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import json
root=Path('D:/Winstar website')
out=root/'review/photo-scout'
out.mkdir(exist_ok=True)
manifest=[]
for batch,folder in enumerate(['Photo Gallery/WINSTAR PHOTOS/Resized','Photo Gallery/WINSTAR PHOTOS 2/Resized'],1):
    files=sorted([p for p in (root/folder).iterdir() if p.suffix.lower() in ['.jpg','.jpeg','.png','.webp']],key=lambda p:p.name)
    print(batch,len(files),flush=True)
    for start in range(0,len(files),25):
        group=files[start:start+25]
        canvas=Image.new('RGB',(1200,((len(group)+4)//5)*190),'#eee')
        draw=ImageDraw.Draw(canvas)
        for i,p in enumerate(group):
            with Image.open(p) as im:
                w,h=im.size
                im=ImageOps.exif_transpose(im)
                im.thumbnail((232,155))
                x=(i%5)*240;y=(i//5)*190
                canvas.paste(im,(x+(232-im.width)//2,y))
            ident=f'{batch}-{start+i+1:03}'
            draw.text((x+4,y+157),ident+' '+p.stem[:28],fill='black')
            manifest.append(dict(id=ident,file=p.relative_to(root).as_posix(),width=w,height=h))
        canvas.save(out/f'contact-{batch}-{start//25+1}.jpg',quality=88)
(out/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print('Ready',len(manifest),flush=True)
