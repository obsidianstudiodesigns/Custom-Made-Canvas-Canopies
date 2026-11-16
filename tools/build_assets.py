"""Build web images, favicons and the share image from the raw photos in _source/.

Run from the project root:  python -I tools/build_assets.py
Needs Pillow and fontTools (with brotli) installed.
"""
import io
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_source")
OUT = os.path.join(ROOT, "assets", "img")
os.makedirs(OUT, exist_ok=True)

ACCENT = (232, 184, 41)
INK = (14, 16, 12)

# name: (source file, crop box as fractions l, t, r, b, widths)
IMAGES = {
    "hero-wide": ("gen/hero-wide.png", None, (960, 1600)),
    "hero-tall": ("gen/hero-tall.png", None, (640, 864)),
    "craft": ("gen/craft.png", None, (800, 1280)),
    "canvas-hilux": ("fb/ccc-10.jpg", None, (640, 1200)),
    "canvas-cruiser": ("fb/ccc-07.jpg", (0, 0, 1, .92), (640, 1200)),
    "canvas-ranger": ("fb/ccc-11.jpg", None, (640, 1200)),
    "rails-cruiser": ("fb/ccc-44.jpg", None, (640, 1200)),
    "rails-hilux": ("fb/ccc-01.jpg", None, (640, 1200)),
    "rails-isuzu": ("fb/ccc-15.jpg", (0, .05, 1, 1), (640, 1200)),
    "rails-white": ("fb/ccc-41.jpg", None, (640, 1200)),
    "hunt-navara": ("fb/ccc-49.jpg", None, (640, 1000)),
    "hunt-seats": ("fb/ccc-37.jpg", None, (640, 1200)),
    "hunt-bench": ("fb/ccc-58.jpg", None, (640, 1200)),
    "hunt-frame": ("fb/ccc-70.jpg", (0, 0, 1, .93), (640, 1200)),
    "hunt-hilux": ("fb/ccc-46.jpg", None, (640, 1200)),
    "hunt-cruiser": ("fb/ccc-62.jpg", None, (640, 1200)),
    "hunt-ranger": ("fb/ccc-43.jpg", None, (640, 1200)),
    "roofrack": ("fb/ccc-02.jpg", None, (640, 1200)),
    "tank-pour": ("fb/ccc-14.jpg", None, (640, 1200)),
    "tank-rack": ("fb/ccc-50.jpg", None, (640, 1400)),
    "rooftop-tent": ("fb/ccc-12.jpg", None, (640, 1200)),
    "alu-canopy": ("fb/ccc-13.jpg", None, (640, 1180)),
    "shade-carport": ("fb/ccc-28.jpg", None, (640, 1400)),
    "shade-gate": ("fb/ccc-29.jpg", None, (640, 1200)),
    "shade-patio": ("fb/ccc-32.jpg", None, (640, 1400)),
    "blinds": ("fb/ccc-19.jpg", (0, .07, .93, .88), (640, 1200)),
    "awning-house": ("fb/ccc-22.jpg", (0, .07, .95, 1), (640, 1200)),
    "awning-vehicle": ("fb/ccc-24.jpg", (0, 0, 1, .9), (640, 1200)),
    "canvas-bags": ("fb/ccc-47.jpg", None, (640, 1000)),
    "build-seats": ("fb/ccc-66.jpg", None, (640, 1200)),
    "hunter": ("fb/ccc-51.jpg", None, (640, 1200)),
}


def load(rel, crop):
    im = Image.open(os.path.join(SRC, rel)).convert("RGB")
    if crop:
        w, h = im.size
        l, t, r, b = crop
        im = im.crop((int(l * w), int(t * h), int(r * w), int(b * h)))
    return im


def save_sizes(name, im, widths):
    sizes = []
    for w in widths:
        w = min(w, im.width)
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(
            os.path.join(OUT, f"{name}-{w}.webp"), "WEBP", quality=78, method=6)
        sizes.append((w, h))
    return sizes


_CACHE = {}


def font(path, size, **axes):
    """Pin a variable woff2 to a static instance (fontTools) and load it in Pillow."""
    key = (path, tuple(sorted(axes.items())))
    if key not in _CACHE:
        from fontTools.varLib.instancer import instantiateVariableFont
        f = TTFont(path)
        f.flavor = None
        names = [a.axisTag for a in f["fvar"].axes]
        f = instantiateVariableFont(f, {n: axes.get(n, 400 if n == "wght" else 100) for n in names})
        buf = io.BytesIO()
        f.save(buf)
        _CACHE[key] = buf.getvalue()
    return ImageFont.truetype(io.BytesIO(_CACHE[key]), size)


ARCHIVO = os.path.join(ROOT, "assets", "fonts", "archivo-var.woff2")
GEIST = os.path.join(ROOT, "assets", "fonts", "geist-var.woff2")


def mark(size):
    """Brand mark: yellow tile with an expanded CC monogram."""
    scale = 4
    s = size * scale
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, s - 1, s - 1), radius=int(s * .18), fill=ACCENT)
    f = font(ARCHIVO, int(s * .46), wght=860, wdth=125)
    d.text((s / 2, s / 2 + s * .02), "CC", font=f, fill=INK, anchor="mm")
    return im.resize((size, size), Image.LANCZOS)


def favicons():
    for n in (16, 32, 48, 96):
        mark(n).save(os.path.join(ROOT, f"favicon-{n}.png"))
    mark(256).save(os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    for n, fn in ((192, "icon-192.png"), (512, "icon-512.png")):
        mark(n).save(os.path.join(ROOT, fn))
    # apple + maskable need a solid background and safe padding
    for n, fn, pad in ((180, "apple-touch-icon.png", .12), (512, "icon-maskable-512.png", .2)):
        bg = Image.new("RGBA", (n, n), INK + (255,))
        inner = mark(int(n * (1 - 2 * pad)))
        bg.paste(inner, (int(n * pad), int(n * pad)), inner)
        bg.convert("RGB").save(os.path.join(ROOT, fn))
    mark(120).save(os.path.join(OUT, "mark-120.png"))


def og():
    W, H = 1200, 630
    base = load("gen/hero-wide.png", None)
    r = max(W / base.width, H / base.height)
    base = base.resize((round(base.width * r), round(base.height * r)), Image.LANCZOS)
    x = (base.width - W) // 2
    im = base.crop((x, 0, x + W, H)).convert("RGBA")
    shade = Image.new("RGBA", (W, H))
    sd = ImageDraw.Draw(shade)
    for i in range(W):
        a = int(235 * max(0, 1 - i / (W * .72)) ** 1.25)
        sd.line([(i, 0), (i, H)], fill=INK + (a,))
    im = Image.alpha_composite(im, shade)
    d = ImageDraw.Draw(im)
    m = mark(84)
    im.paste(m, (72, 70), m)
    d.text((176, 92), "CUSTOM MADE", font=font(GEIST, 26, wght=600), fill=(236, 232, 220))
    d.text((176, 122), "CANVAS CANOPIES", font=font(GEIST, 26, wght=600), fill=ACCENT)
    h1 = font(ARCHIVO, 60, wght=820, wdth=116)
    y = 262
    for line in ("BUILT FOR THE", "BAKKIE YOU", "ACTUALLY DRIVE."):
        d.text((72, y), line, font=h1, fill=(240, 236, 226))
        y += 66
    sub = font(GEIST, 27, wght=450)
    d.text((72, y + 24), "Canvas canopies, aluminium cattle rails and hunting", font=sub, fill=(200, 198, 184))
    d.text((72, y + 60), "frames. Made to measure in Pretoria.  082 950 8390", font=sub, fill=(200, 198, 184))
    im.convert("RGB").save(os.path.join(OUT, "og-share.jpg"), quality=86, optimize=True, progressive=True)


if __name__ == "__main__":
    lines = []
    for name, (rel, crop, widths) in IMAGES.items():
        sizes = save_sizes(name, load(rel, crop), widths)
        lines.append(f"{name}: " + ", ".join(f"{w}x{h}" for w, h in sizes))
    with open(os.path.join(OUT, "_sizes.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    favicons()
    og()
    print("\n".join(lines))
