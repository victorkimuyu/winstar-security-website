from pathlib import Path
from PIL import Image
import sys

root = Path(__file__).resolve().parents[1]
with Image.open(sys.argv[1]) as image:
    image.convert('RGB').save(root/'static/images/services/event-winstar-arrivals.jpg', quality=93, optimize=True)
    print(image.size)
