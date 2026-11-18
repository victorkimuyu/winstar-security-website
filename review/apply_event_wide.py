from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
source = Path('C:/Users/Victor/.codex/generated_images/01a13352-b047-7881-bcec-6b1997725f55/exec-4c49450e-8a7f-4e42-914d-7407e8457bca.png')
with Image.open(source) as image:
    image.convert('RGB').save(root/'static/images/services/event-winstar-wide.jpg', quality=93, optimize=True)
    print(image.size)
