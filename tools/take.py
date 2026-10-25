"""take.py <skill_id> <capture.png> : save 512 icon + 855 backup art."""
import sys
from PIL import Image
sid, src = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB')
w, h = im.size; s = min(w, h)
im = im.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))
im.save(f'art/{sid}.webp', 'WEBP', quality=88)
im.resize((512, 512), Image.LANCZOS).save(f'icons/{sid}.webp', 'WEBP', quality=86)
print(sid, 'ok')
