import os
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont

from .holidays import get_todays_holidays

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMAGE_DIRECTORY = os.path.join(ROOT_DIR, "background_images")


def get_random_background() -> Image.Image:
    images = [img for img in os.listdir(IMAGE_DIRECTORY) if img != ".DS_Store"]

    return Image.open(os.path.join(IMAGE_DIRECTORY, random.choice(images)))


def get_random_greeting() -> str:
    return random.choice(["Щастя і здоров'я!", "Бажаю успіхів!", "Нехай щастить!"])


def generate_postcard_with_holiday() -> Image.Image:
    text = f"{get_todays_holidays()}. {get_random_greeting()}"
    return generate_postcard(text)


# def with_paddings(text: str) -> str:
#     count = 0
#     while count < len(text):
#         if count and count % 15 == 0:
#             text = text[:count] + "/n" + text[count:]
#         count += 1
#     return text


def generate_postcard(text: str) -> Image.Image:
    img = get_random_background()

    width, height = img.size
    # Call draw Method to add 2D graphics in an image
    textPromp = ImageDraw.Draw(img)

    font = ImageFont.truetype(os.path.join(ROOT_DIR, "font.ttf"), 60)

    margin = 400
    offset = height / 5
    for line in textwrap.wrap(text, width=15):
        textPromp.text(
            (margin, offset),
            line,
            font=font,
            fill="#aa0000",
            stroke_fill=(0, 0, 0),
            stroke_width=2,
        )
        offset += font.getsize(line)[1]

    # Save the edited image
    img.save("test.png")
