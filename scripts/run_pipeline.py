from __future__ import annotations

from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except Exception:  # pragma: no cover - only used when Pillow is present
    Image = None
    ImageDraw = None
    ImageFont = None


def generate_placeholder_thumbnail(output_path: str | Path, title: str = "LFR Pipeline") -> str:
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)

    if Image is None or ImageDraw is None:
        target.write_text(f"Thumbnail: {title}\n", encoding="utf-8")
        return str(target)

    image = Image.new("RGBA", (1280, 720), color=(10, 23, 38, 255))
    draw = ImageDraw.Draw(image)
    draw.rectangle((30, 30, 1250, 690), fill=(21, 52, 78, 255), outline=(85, 130, 255, 255), width=4)
    draw.text((80, 120), title, fill=(255, 255, 255), font=ImageFont.load_default())
    draw.text((80, 220), "Little Friends Rhymes", fill=(135, 206, 250, 255), font=ImageFont.load_default())
    draw.text((80, 540), "Generated with the LFR pipeline", fill=(210, 230, 255, 255), font=ImageFont.load_default())
    image.save(target, format="PNG")
    return str(target)


__all__ = ["generate_placeholder_thumbnail"]
