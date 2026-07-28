from io import BytesIO
import math
import random
import string
from PIL import Image, ImageDraw, ImageFont


def create_captcha():
    allowed_chars = "".join(set(string.ascii_uppercase + string.digits) - set("0O1IL"))
    text = "".join(random.choices(allowed_chars, k=5))

    width, height = 200, 80
    image = Image.new("RGB", (width, height), (255, 255, 255))

    try:
        base_font = ImageFont.truetype("comic.ttf", 36)
    except IOError:
        base_font = ImageFont.load_default()

    char_images = []
    for char in text:
        char_img = Image.new("RGBA", (40, 50), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_img)

        char_draw.text(
            (5, 2),
            char,
            font=base_font,
            fill=(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)),
        )

        angle = random.randint(-25, 25)
        char_img = char_img.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
        char_images.append(char_img)

    x_offset = 15
    for char_img in char_images:
        y_offset = random.randint(10, 30)
        image.paste(char_img, (x_offset, y_offset), char_img)
        x_offset += random.randint(18, 26)

    draw = ImageDraw.Draw(image)

    for _ in range(6):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line(
            [(x1, y1), (x2, y2)],
            fill=(random.randint(50, 150), random.randint(50, 150), random.randint(50, 150)),
            width=2,
        )

    image = image.resize((width // 2, height // 2), Image.Resampling.NEAREST)
    image = image.resize((width, height), Image.Resampling.NEAREST)

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer, text