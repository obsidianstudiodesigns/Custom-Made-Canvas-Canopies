"""Pack Phosphor icon SVGs (MIT, phosphoricons.com) from _source/dl/icons into assets/icons.svg."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_source", "dl", "icons")
out = ['<svg xmlns="http://www.w3.org/2000/svg" style="display:none">']
for fn in sorted(os.listdir(SRC)):
    body = open(os.path.join(SRC, fn), encoding="utf-8").read()
    inner = re.search(r"<svg[^>]*>(.*)</svg>", body, re.S).group(1)
    out.append(f'<symbol id="i-{fn[:-4]}" viewBox="0 0 256 256" fill="currentColor">{inner}</symbol>')
out.append("</svg>")
open(os.path.join(ROOT, "assets", "icons.svg"), "w", encoding="utf-8").write("\n".join(out))
print("icons:", len(out) - 2)
