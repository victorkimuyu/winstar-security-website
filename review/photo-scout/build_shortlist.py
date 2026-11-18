from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import json,html
root=Path('D:/Winstar website');out=root/'review/photo-scout'
m={x['id']:x for x in json.loads((out/'manifest.json').read_text())}
choices=[
('1-002','Home / operational capacity','Strong branded vehicle and two personnel. Crop competing banners and keep the full vehicle identity. Good hero candidate after restrained reframing.','Crop / optional extension'),
('1-007','Alarms / monitoring','Two control-room operators, phone and workstation: shows the service behind the alarm. Strong replacement for a generic monitoring illustration. Inspect screens and desk papers before publishing.','Crop'),
('1-017','Security Guards / property sectors','Active vehicle check with a recognisable entrance. Stronger service narrative than another static line-up. Crop road/sky, preserve guard and inspection mirror.','Crop'),
('1-024','Security Guards / Company','Guard framed by the building entrance. Balanced architectural setting; useful hero or section image. Retain door frame as context.','Crop / optional extension'),
('1-026','CCTV hero','Technician working on an actual camera, with strong equipment detail. Crop around face, hands and camera; extend sky sideways only if required for title space.','Crop / optional extension'),
('1-038','Home capacity / Company / Guards','Supervisor briefing a team: clear evidence of operational preparation. Keep supervisor, notes and responding guards in frame.','Crop'),
('1-059','Event Security','Actual event-related setting with Winstar branding, but guard faces away and file is only 1024px wide. Supporting image or uniform reference; not first-choice desktop hero.','Supporting only'),
('2-027','K9 hero','Dog actively checking a vehicle with handler. Better service story than a posed dog. Preserve leash, handler hands and vehicle opening; extend surrounding greenery if needed.','Crop / optional extension'),
('2-046','Security Guards / reception / hospitality','Courteous visitor interaction at reception. Strong guest-assistance image; not evidence of biometric equipment or airport screening.','Crop'),
('2-060','Home / hospitality / Company','Two reception personnel in a bright architectural setting, friendly expressions and visible uniforms. Strong people-focused supporting photograph.','Crop'),
('2-068','Alarms response / Company / Home','Fleet overview with branded vehicles. Useful proof of operational resources. Wide hero crop can work if vehicle names and personnel remain readable.','Crop'),
('2-085','Company / operational management','Two control-room personnel with reporting materials. Good management/support image; more posed than the working control-room sequence.','Crop'),
('2-127','K9 / integrated response','Two response personnel, dog and branded vehicle. Strong team/capacity context; use beside deployment support rather than claiming detection in progress.','Crop'),
('2-134','VIP & Cargo Escorts / response capacity','Branded vehicle with two personnel and clear exterior setting. Suitable generic escort-support hero; does not demonstrate a VIP or cargo assignment itself.','Crop / optional extension'),
('2-143','Alarms rapid response','Officer stepping from response vehicle: clear action, stronger than leaning/posing. Crop carefully to retain head, handhold and vehicle door.','Crop'),
('2-040','Electric Fencing / perimeter maintenance','Technician working above a wall. Visible wire appears to include razor wire; inspect before labelling this an electric-fence installation. Good perimeter-work supporting image.','Supporting only'),
('2-038','Company / technical installation','Personnel handling a ladder with PPE. Useful engineering/installation support, but no visible installed product to identify a specific service.','Crop'),
('2-094','Company / customer care','Guard assisting a wheelchair user. Strong service and accessibility story. Supporting image, retain the actual assistance interaction.','Crop'),
('2-100','Alarms / communications','Close radio-use image in vehicle. Good inset for control-room/field communication; portrait composition less suited to wide hero.','Supporting only'),
('2-129','Security Guards / Home people panel','Wide team line-up. Good alternative to expanding the old close portrait; less explanatory than briefing or visitor-assistance shots.','Crop'),
]
data=[]
for ident,placement,note,edit in choices:
 x=dict(m[ident],placement=placement,note=note,edit=edit);data.append(x)
for start in range(0,15,6):
 group=data[start:start+6];canvas=Image.new('RGB',(1200,((len(group)+2)//3)*310),'#eee');d=ImageDraw.Draw(canvas)
 for i,x in enumerate(group):
  with Image.open(root/x['file']) as im:
   im=ImageOps.exif_transpose(im);im.thumbnail((390,270));px=(i%3)*400;py=(i//3)*310;canvas.paste(im,(px+(390-im.width)//2,py))
  d.text((px+4,py+275),x['id']+' '+Path(x['file']).name[:35],fill='black')
 canvas.save(out/f'selected-{start//6+1}.jpg',quality=90)
(out/'shortlist.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
cards=[]
for x in data:
 src='../../'+x['file'];safe=html.escape
 cards.append(f'<article data-edit="{safe(x["edit"])}"><a href="{safe(src)}"><img src="{safe(src)}" loading="lazy" alt="{safe(x["placement"])}"></a><div><small>{x["id"]} · {x["width"]} × {x["height"]}</small><h2>{safe(x["placement"])}</h2><p>{safe(x["note"])}</p><b>{safe(x["edit"])}</b><p class="filename">{safe(x["file"])}</p></div></article>')
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Winstar photo shortlist</title><style>body{font:16px/1.5 Arial,sans-serif;margin:0;background:#f4f5f7;color:#39375b}header,main{max-width:1320px;margin:auto;padding:32px}h1{font-size:38px;margin:0 0 12px}header{padding-bottom:0}main{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}article{background:white}article img{width:100%;aspect-ratio:1.5;object-fit:contain;background:#e6e7ec;display:block}article>div{padding:22px}h2{font-size:20px;margin:10px 0}p{font-size:14px}small{color:#666}b{font-size:12px;color:#1780b8}.filename{overflow-wrap:anywhere;font-size:12px}button{padding:10px 16px;border:1px solid #ccc;background:white;cursor:pointer;margin:4px}button.active{background:#39375b;color:white}article[hidden]{display:none}@media(max-width:900px){main{grid-template-columns:repeat(2,1fr)}}@media(max-width:560px){main{grid-template-columns:1fr}header,main{padding:20px}}</style><header><h1>Winstar photo shortlist</h1><p>204 source images reviewed · 20 shortlisted · 18 November 2026</p><p>Click an image to inspect the source. Suggestions only; website assets have not been replaced.</p><nav><button class="active" data-filter="all">All</button><button data-filter="Crop">Crop</button><button data-filter="Crop / optional extension">Possible extension</button><button data-filter="Supporting only">Supporting only</button></nav></header><main>'''+''.join(cards)+'''</main><script>document.querySelectorAll('button').forEach(b=>b.onclick=()=>{document.querySelectorAll('button').forEach(x=>x.classList.toggle('active',x===b));document.querySelectorAll('article').forEach(a=>a.hidden=b.dataset.filter!=='all'&&a.dataset.edit!==b.dataset.filter)});</script></html>'''
(out/'shortlist.html').write_text(page,encoding='utf-8')
print('Shortlist, gallery and detailed review sheets saved.')
