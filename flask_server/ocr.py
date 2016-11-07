import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO


def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)


def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))

def process_image_file_jpg(imgFile):
    image = Image.open(imgFile)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)

def process_image_file_png(imgFile):
    im = Image.open(imgFile)
    bg = Image.new("RGB", im.size, (255,255,255))
    bg.paste(im,im)
    #print image_to_string(bg)
    return pytesseract.image_to_string(bg)