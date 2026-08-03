from pathlib import Path
from PIL import Image

icons_dir = Path("assets/icons")
reference = Image.open(icons_dir / "Python.png").convert("RGBA")
ref_w, ref_h = reference.size
ref_long = max(ref_w, ref_h)
exclude = {"Python.png", "SQL.png", "aws.png"}


def fill_percent(img: Image.Image) -> float:
    alpha = img.getchannel("A")
    total = alpha.width * alpha.height
    non_transparent = sum(1 for p in alpha.getdata() if p > 0)
    return non_transparent / total * 100.0


for path in sorted(icons_dir.glob("*.png")):
    if path.name in exclude:
        continue

    img = Image.open(path).convert("RGBA")
    bbox = img.getbbox()
    if bbox is None:
        print(f"{path.name}: no non-transparent pixels, skipped")
        continue

    left, top, right, bottom = bbox
    cropped = img.crop((left, top, right, bottom))
    cropped_w, cropped_h = cropped.size
    longest = max(cropped_w, cropped_h)

    if longest == 0:
        print(f"{path.name}: empty image, skipped")
        continue

    scale = ref_long / longest
    resized_w = max(1, int(cropped_w * scale))
    resized_h = max(1, int(cropped_h * scale))
    resized = cropped.resize((resized_w, resized_h), Image.LANCZOS)

    canvas = Image.new("RGBA", (ref_w, ref_h), (0, 0, 0, 0))
    pad = int(ref_long * 0.05)
    x = (ref_w - resized_w) // 2
    y = (ref_h - resized_h) // 2
    if resized_w > ref_w - 2 * pad:
        x = pad
    if resized_h > ref_h - 2 * pad:
        y = pad

    canvas.alpha_composite(resized, dest=(x, y))

    before = fill_percent(img)
    after = fill_percent(canvas)
    canvas.save(path)
    print(f"{path.name}: fill {before:.2f}% -> {after:.2f}%")
