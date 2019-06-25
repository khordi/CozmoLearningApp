import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

import time
from PIL import Image, ImageDraw, ImageFont

#--------------------Display writing on Cozmo--------------------

def make_text_image(text_to_draw, x, y, font=None):

    text_image = Image.new('RGBA', cozmo.oled_face.dimensions(), (0, 0, 0, 255))    # make a blank image for the text, initialized to opaque black

    dc = ImageDraw.Draw(text_image)                                         # get a drawing context

    dc.text((x, y), text_to_draw, fill=(255, 255, 255, 255), font=font)    # draw the text

    return text_image


