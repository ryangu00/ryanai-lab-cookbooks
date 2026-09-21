#!/usr/bin/env python3
"""Draw the repo banner. Pure PIL, no generated imagery — RyanAI Lab house style.

Concept: 38 first-hand cookbooks, pick the one you need.
Left = wordmark. Right = an index grid of 38 small tiles (one per cookbook),
with a single orange tile marking the one you pick.
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
BG = (10, 10, 10)
WHITE = (245, 245, 245)
GREY = (140, 140, 140)
DIM = (70, 70, 70)
ORANGE = (255, 122, 26)
OUT = pathlib.Path(__file__).resolve().parents[1] / "docs/assets/banner.png"

HN = "/System/Library/Fonts/HelveticaNeue.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"

def font(path, size, index=0):
    try:
        return ImageFont.truetype(path, size, index=index)
    except Exception:
        return ImageFont.load_default()

f_title = font(HN, 88, 7)     # Light
f_tag = font(HN, 30, 7)
f_mono = font(MENLO, 17)
f_label = font(MENLO, 15)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# crosshair corners
for cx, cy in ((40, 40), (W - 40, H - 40)):
    d.line([(cx - 11, cy), (cx + 11, cy)], fill=DIM, width=1)
    d.line([(cx, cy - 11), (cx, cy + 11)], fill=DIM, width=1)

# 5x3 dot lattices
for ox, oy in ((72, 78), (1150, 536)):
    for r in range(3):
        for c in range(5):
            x, y = ox + c * 15, oy + r * 12
            d.ellipse([x, y, x + 1.6, y + 1.6], fill=DIM)

# wordmark
d.text((80, 196), "RYANAI LAB", font=f_title, fill=WHITE)
d.text((80, 288), "COOKBOOK INDEX", font=f_title, fill=WHITE)
d.text((82, 414), "38 first-hand cookbooks — pick the one you need.", font=f_tag, fill=WHITE)
d.text((82, 462), "ONE REPOSITORY PER EXPERIMENT · FIRST-HAND NUMBERS · REPRODUCIBLE", font=f_mono, fill=GREY)

# right: index motif — a grid of 38 book tiles, one picked (orange)
GX, GY = 890, 210
TILE, GAP = 26, 10
COLS = 8
ROWS_FULL, LAST_ROW = 4, 6          # 4 full rows of 8 + 6 tiles = 38
ORANGE_IDX = 30                     # first tile of the partial last row

idx = 0
accent_pos = None
for r in range(ROWS_FULL + 1):
    n = COLS if r < ROWS_FULL else LAST_ROW
    for c in range(n):
        x = GX + c * (TILE + GAP)
        y = GY + r * (TILE + GAP)
        box = [x, y, x + TILE, y + TILE]
        if idx == ORANGE_IDX:
            d.rectangle(box, fill=ORANGE)
            accent_pos = (x, y)
        else:
            d.rectangle(box, outline=(96, 96, 96), width=1)
        idx += 1

ax, ay = accent_pos
d.text((GX, GY - 26), "01 BOOKS", font=f_label, fill=GREY)
d.text((GX, GY + (ROWS_FULL + 1) * (TILE + GAP) + 6), "02 PICK ONE", font=f_label, fill=ORANGE)  # below the grid, clear of every tile

# footer rule + labels
d.line([(80, 560), (W - 80, 560)], fill=(40, 40, 40), width=1)
d.text((80, 576), "RYANAI LAB", font=f_label, fill=GREY)
d.text((W - 80 - 250, 576), "DELL PRO MAX WITH GB10", font=f_label, fill=GREY)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print("wrote", OUT)
