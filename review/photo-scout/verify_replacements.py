from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re
r=Path('D:/Winstar website');o=r/'review/photo-scout'
class Check(HTMLParser):
    def __init__(self):super().__init__();self.stack=[];self.errors=[];self.ids=[]
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        for k in ('src','href'):
            u=urlsplit(a.get(k,''));p=unquote(u.path)
            if p and not u.scheme and not u.netloc and not (r/p).exists():self.errors.append(p)
        if t=='img' and 'alt' not in a:self.errors.append('Missing image alternative')
        if t not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append(t)
    def handle_endtag(self,t):
        if not self.stack or self.stack.pop()!=t:self.errors.append('Nesting '+t)
for name in ['index','services','manned-guarding','canine-security','cctv-surveillance','security-alarm-systems','vip-cargo-escorts']:
    c=Check();c.feed((r/f'{name}.html').read_text(encoding='utf-8'));assert not c.errors and not c.stack and len(c.ids)==len(set(c.ids)),(name,c.errors)
    print('PASS',name)
for f in ['home','service-heroes']:
    s=(r/f'static/{f}.css').read_text();assert s.count('{')==s.count('}')
canvas=Image.new('RGB',(1200,1080),'#eee');d=ImageDraw.Draw(canvas)
for i,(name,x) in enumerate([('winstar-guarding',.75),('winstar-site-security',.59),('winstar-response',.49)]):
    with Image.open(r/f'static/images/slider/{name}.jpg') as im:
        desktop=ImageOps.fit(im,(830,345),centering=(x,.45))
        mobile=ImageOps.fit(im,(230,345),centering=(x,.5))
    canvas.paste(desktop,(0,i*360));canvas.paste(mobile,(860,i*360));d.text((4,i*360+346),name+' — desktop / mobile focal crop',fill='black')
canvas.save(o/'homepage-crop-review.jpg',quality=88)
print('Saved desktop/mobile crop comparison (images only; browser layout still needs review).')
for p in (r/'static/images/slider').glob('winstar-*.jpg'):print(p.name,round(p.stat().st_size/1024),'KB')
