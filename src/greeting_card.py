import os
import random

from PIL import Image, ImageDraw, ImageFont

from .holidays import get_todays_holidays

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMAGE_DIRECTORY = os.path.join(ROOT_DIR, "background_images")


def get_random_background() -> Image.Image:
    images = [img for img in os.listdir(IMAGE_DIRECTORY) if img != ".DS_Store"]

    return Image.open(os.path.join(IMAGE_DIRECTORY, random.choice(images)))


def generate_postcard(text: str) -> Image.Image:
    img = get_random_background()

    width, height = img.size
    # Call draw Method to add 2D graphics in an image
    textPromp = ImageDraw.Draw(img)

    myFont = ImageFont.truetype(os.path.join(ROOT_DIR, "font.ttf"), 200)

    textPromp.text((width / 2, height / 2), text, fill=(255, 0, 0), font=myFont)

    # Save the edited image
    img.save("test.png")
