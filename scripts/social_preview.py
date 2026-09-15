"""Render assets/social-preview.png (1280x640) for the GitHub repo Social preview setting.

Local only, needs Pillow. Run after build.py so the actor count matches data/actors.json.
GitHub does not read this file automatically: upload it under Settings > General > Social preview.
"""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets' / 'social-preview.png'
FONTS = Path('C:/Windows/Fonts')
W, H = 1280, 640
BG, INK, MUTED, ACCENT, CHIP = '#0f172a', '#f8fafc', '#94a3b8', '#38bdf8', '#1e293b'


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    for candidate in (FONTS / name, FONTS / 'arial.ttf'):
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default(size)


def main() -> None:
    catalog = json.loads((ROOT / 'data' / 'actors.json').read_text(encoding='utf-8'))
    count, cats = len(catalog['actors']), [c['name'] for c in catalog['categories']]

    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 14, H], fill=ACCENT)

    x = 80
    d.text((x, 48), 'AutomationByExperts', font=font('segoeuib.ttf', 34), fill=ACCENT)
    d.text((x, 102), 'Web Scraping APIs', font=font('segoeuib.ttf', 76), fill=INK)
    d.text((x, 188), 'and AI Automation Tools', font=font('segoeuib.ttf', 76), fill=INK)
    d.text((x, 290), f'{count} ready-to-run Apify actors. No code, export to JSON, CSV or Excel.',
           font=font('segoeui.ttf', 32), fill=MUTED)

    chip_font, cx, cy = font('segoeui.ttf', 24), x, 360
    for name in cats:
        tw = d.textlength(name, font=chip_font)
        if cx + tw + 40 > W - 80:
            cx, cy = x, cy + 58
        d.rounded_rectangle([cx, cy, cx + tw + 32, cy + 44], radius=22, fill=CHIP)
        d.text((cx + 16, cy + 7), name, font=chip_font, fill=INK)
        cx += tw + 48

    d.text((x, H - 70), 'github.com/automationbyexperts/web-scraping-apis  |  automationbyexperts.com',
           font=font('segoeui.ttf', 26), fill=MUTED)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, optimize=True)
    print(f'Wrote {OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
