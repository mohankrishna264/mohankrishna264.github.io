from PIL import Image, ImageDraw

size = 512


def save_icon(path, color, draw_fn):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_fn(draw, color)
    img.save(path, format='PNG')


save_icon('assets/icons/java.png', (233, 110, 0, 255), lambda draw, color: (
    draw.ellipse([120, 88, 392, 360], outline=color, width=26),
    draw.rectangle([214, 112, 292, 332], fill=color),
    draw.rectangle([182, 332, 326, 388], fill=color),
    draw.rectangle([220, 388, 288, 430], fill=color),
    draw.arc([164, 148, 344, 328], 20, 160, fill=color, width=26),
))

save_icon('assets/icons/spring-boot.png', (72, 183, 72, 255), lambda draw, color: (
    draw.ellipse([116, 110, 398, 392], outline=color, width=24),
    draw.arc([152, 144, 366, 356], 180, 360, fill=color, width=18),
    draw.arc([176, 174, 336, 334], 0, 180, fill=color, width=18),
    draw.ellipse([202, 180, 312, 290], fill=color, outline=color),
))

save_icon('assets/icons/typescript.png', (52, 120, 198, 255), lambda draw, color: (
    draw.rectangle([128, 126, 384, 194], fill=color),
    draw.rectangle([128, 236, 384, 304], fill=color),
    draw.rectangle([128, 346, 384, 414], fill=color),
    draw.polygon([(128, 126), (384, 126), (256, 420)], fill=color),
))

save_icon('assets/icons/react.png', (90, 200, 250, 255), lambda draw, color: (
    draw.ellipse([126, 118, 386, 378], outline=color, width=24),
    draw.line([256, 88, 256, 424], fill=color, width=18),
    draw.line([182, 154, 330, 360], fill=color, width=18),
    draw.line([330, 154, 182, 360], fill=color, width=18),
))

save_icon('assets/icons/langchain.png', (120, 82, 238, 255), lambda draw, color: (
    draw.rectangle([158, 132, 354, 208], fill=color),
    draw.rectangle([158, 304, 354, 380], fill=color),
    draw.line([256, 208, 256, 304], fill=color, width=20),
    draw.line([158, 208, 158, 304], fill=color, width=20),
    draw.line([354, 208, 354, 304], fill=color, width=20),
))

save_icon('assets/icons/openai.png', (16, 185, 129, 255), lambda draw, color: (
    draw.ellipse([158, 120, 354, 392], outline=color, width=28),
    draw.arc([184, 150, 332, 402], 20, 160, fill=color, width=24),
    draw.line([256, 132, 256, 380], fill=color, width=14),
))

save_icon('assets/icons/pytorch.png', (238, 82, 46, 255), lambda draw, color: (
    draw.polygon([(176, 120), (336, 120), (336, 280), (176, 280)], fill=color),
    draw.polygon([(176, 280), (336, 280), (256, 392)], fill=color),
    draw.line([256, 120, 256, 392], fill=color, width=16),
))

save_icon('assets/icons/fastapi.png', (4, 150, 104, 255), lambda draw, color: (
    draw.polygon([(192, 120), (324, 120), (356, 196), (224, 196)], fill=color),
    draw.polygon([(220, 196), (356, 196), (324, 416), (188, 416)], fill=color),
    draw.line([246, 150, 298, 262], fill=(255, 255, 255, 255), width=16),
))

save_icon('assets/icons/postgresql.png', (51, 103, 145, 255), lambda draw, color: (
    draw.ellipse([148, 110, 364, 402], outline=color, width=24),
    draw.line([256, 120, 256, 392], fill=color, width=18),
    draw.line([188, 188, 324, 188], fill=color, width=18),
    draw.line([188, 324, 324, 324], fill=color, width=18),
    draw.ellipse([208, 194, 304, 292], fill=color),
))

print('created png icons')
