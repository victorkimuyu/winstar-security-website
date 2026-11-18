from pathlib import Path
from PIL import Image,ImageOps
import json
r=Path('D:/Winstar website');o=r/'review/photo-scout'
m={x['id']:x for x in json.loads((o/'manifest.json').read_text())}
for ident in ['1-024','1-017','1-002','1-026','2-027','1-007','2-143']:
    with Image.open(r/m[ident]['file']) as im:
        im=ImageOps.exif_transpose(im);im.thumbnail((1100,750));im.save(o/f'preview-{ident}.jpg',quality=90)
print('Previews ready')
