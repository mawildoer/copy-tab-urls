# /// script
# dependencies = ["pillow"]
# ///
"""Render the extension icons (icons/icon-<size>.png) from code.

Run: uv run scripts/make_icons.py
"""

from pathlib import Path

from PIL import Image, ImageDraw

SIZES = (16, 32, 48, 128)
SCALE = 8  # supersample, then downscale for smooth edges
BG = (37, 99, 235, 255)  # blue
FG = (255, 255, 255, 255)

out_dir = Path(__file__).resolve().parent.parent / "icons"
out_dir.mkdir(exist_ok=True)

for size in SIZES:
    s = size * SCALE
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, s - 1, s - 1), radius=s * 0.22, fill=BG)
    # Three list rows: a bullet and a line each, i.e. "a list of URLs".
    pad = s * 0.2
    row_h = s * 0.1
    for i in range(3):
        cy = pad + row_h / 2 + i * (s - 2 * pad - row_h) / 2
        d.ellipse((pad, cy - row_h / 2, pad + row_h, cy + row_h / 2), fill=FG)
        x0 = pad + row_h * 1.8
        d.rounded_rectangle((x0, cy - row_h / 2, s - pad, cy + row_h / 2), radius=row_h / 2, fill=FG)
    img.resize((size, size), Image.LANCZOS).save(out_dir / f"icon-{size}.png")
    print(f"wrote icons/icon-{size}.png")
