#!/usr/bin/env python3
"""Expanded Materials mod-patch badges + Workshop preview.

Same geometry system as the rest of the suite (300x100 bar/circle/ring knockout;
512 preview) so they read as one set, with the EM family's own identity:

- Muted-material accents: METALS = copper, MASONRY = sandstone gold. Both warm and
  close in hue on purpose (they are a family); value/saturation keep them apart -
  copper is the darker red-metal, gold the lighter yellow.
- Own emblems, nothing from Combat Extended's art (no CE dependency, no weapons):
  METALS = three stacked ingots, MASONRY = a running-bond stone-block wall, each
  with a single accent piece mirroring the other.

Run from Media/:  python3 badge_gen.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "/usr/share/fonts/dejavu-sans-fonts/DejaVuSansCondensed-Bold.ttf"
S = 4
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
COPPER = (214, 128, 48, 255)   # METALS
GOLD = (230, 182, 60, 255)     # MASONRY


def ingots(img, d, cx, cy, scale, accent):
    """Three stacked ingots: two on the bottom course, one centred on top."""
    def ingot(x, y, w, h, fill):
        taper = w * 0.22
        d.polygon(
            [(x - w / 2 + taper, y - h / 2), (x + w / 2 - taper, y - h / 2),
             (x + w / 2, y + h / 2), (x - w / 2, y + h / 2)],
            fill=fill,
        )
    w = 34 * scale
    h = 15 * scale
    gap = 2 * scale
    ingot(cx - (w + gap) / 2, cy + h * 0.75, w, h, WHITE)
    ingot(cx + (w + gap) / 2, cy + h * 0.75, w, h, WHITE)
    ingot(cx, cy - h * 0.75, w, h, accent)


def blocks(img, d, cx, cy, scale, accent):
    """Two courses of near-square stone blocks in running bond; top-centre block
    accent (mirrors the ingots' single-accent composition)."""
    bw = 22 * scale
    bh = 15 * scale
    g = 2.5 * scale

    def rect(xc, yc, w, h, fill):
        d.rectangle([xc - w / 2, yc - h / 2, xc + w / 2, yc + h / 2], fill=fill)

    off = (bw + g) / 2
    yb = cy + (bh + g) / 2
    yt = cy - (bh + g) / 2
    hw = (bw - g) / 2
    rect(cx - off, yb, bw, bh, WHITE)          # bottom course, two full blocks
    rect(cx + off, yb, bw, bh, WHITE)
    rect(cx, yt, bw, bh, accent)               # top course, offset half a block
    rect(cx - bw / 2 - g - hw / 2, yt, hw, bh, WHITE)
    rect(cx + bw / 2 + g + hw / 2, yt, hw, bh, WHITE)


def render_badge(path, subtitle, accent, emblem):
    W, H = 300 * S, 100 * S
    bar = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    db = ImageDraw.Draw(bar)
    db.rectangle([0, 25 * S, 300 * S, 74 * S], fill=BLACK)
    hole = Image.new("L", (W, H), 0)
    dh = ImageDraw.Draw(hole)
    cx, cy, r, gap = 50 * S, 50 * S, 50 * S, 5 * S
    dh.ellipse([cx - (r + gap), cy - (r + gap), cx + (r + gap), cy + (r + gap)], fill=255)
    dh.rectangle([0, 0, 5 * S, H], fill=255)
    bar.putalpha(Image.composite(Image.new("L", (W, H), 0), bar.getchannel("A"), hole))

    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    img.alpha_composite(bar)
    d = ImageDraw.Draw(img)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLACK)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=accent, width=3 * S)
    emblem(img, d, cx, cy, S, accent)

    CX = 202 * S
    f1 = ImageFont.truetype(FONT, 15 * S)
    t1 = "EXPANDED MATERIALS"
    w1 = d.textlength(t1, font=f1)
    d.text((CX - w1 / 2, 32 * S), t1, font=f1, fill=WHITE)
    f2 = ImageFont.truetype(FONT, 10 * S)
    K = 1.6 * S
    w2 = sum(d.textlength(c, font=f2) + K for c in subtitle) - K
    x = CX - w2 / 2
    for ch in subtitle:
        d.text((x, 55 * S), ch, font=f2, fill=accent)
        x += d.textlength(ch, font=f2) + K
    img.resize((300, 100), Image.LANCZOS).save(path)
    print("wrote", path)


def render_preview(path, subtitle, accent, emblem):
    P = 4
    W = H = 512 * P
    img = Image.new("RGBA", (W, H), (12, 12, 12, 255))
    d = ImageDraw.Draw(img)
    cx, cy, r = 256 * P, 190 * P, 140 * P
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLACK, outline=accent, width=8 * P)
    emblem(img, d, cx, cy, P * 2.8, accent)

    def fitp(texts, max_size, max_w):
        s = int(max_size)
        while s > 10 and max(d.textlength(t, font=ImageFont.truetype(FONT, s)) for t in texts) > max_w:
            s -= 1
        return ImageFont.truetype(FONT, s)

    line1, line2 = "EXPANDED MATERIALS", subtitle
    ftitle = fitp([line1, line2], 42 * P, 470 * P)
    plh = sum(ftitle.getmetrics())
    ytop = 367 * P
    for text, y, color in [(line1, ytop, WHITE), (line2, ytop + plh, accent)]:
        w = d.textlength(text, font=ftitle)
        d.text(((W - w) / 2, y), text, font=ftitle, fill=color)
    img.resize((512, 512), Image.LANCZOS).save(path)
    print("wrote", path)


if __name__ == "__main__":
    render_badge(os.path.join(HERE, "Badge_MMP.png"), "METALS MOD PATCHES", COPPER, ingots)
    render_badge(os.path.join(HERE, "Badge_MMMas.png"), "MASONRY MOD PATCHES", GOLD, blocks)
    render_preview(os.path.join(HERE, "..", "About", "Preview.png"),
                   "METALS MOD PATCHES", COPPER, ingots)
    # Distribute this mod's badge to sibling repos so their READMEs cross-link with
    # relative paths (personal tooling - skipped when a sibling is absent).
    import shutil
    siblings = [
        "CombatExtended-SimpleSidearms Compatibility Patch",
        "CombatExtended-SimpleSidearms-Compatibility-Loadouts",
        "CombatExtended-SimpleSidearms-Compatibility-Tactics",
        "Better-Attack-Orders-for-Simple-Sidearms",
        "Pawns-Optimize-Weapon-Quality",
    ]
    for sib in siblings:
        media = os.path.expanduser(f"~/Projects/{sib}/Media")
        if os.path.isdir(media):
            shutil.copy(os.path.join(HERE, "Badge_MMP.png"), os.path.join(media, "Badge_MMP.png"))
            print("distributed Badge_MMP.png ->", media)
