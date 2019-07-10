import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import degrees, distance_mm, speed_mmps
import time

from displayText import *

import random
import os
_math_font = None  #try removing the try and except and = this to font etc
try:
    _math_font = ImageFont.truetype("arial.ttf", 25)
except:
    pass

_text_font = None  #try removing the try and except and = this to font etc
try:
    _text_font = ImageFont.truetype("arial.ttf", 19)
except:
    pass
current_directory = os.path.dirname(os.path.realpath(__file__))
#---------------------------------------------------------------------------

def question1T(self: cozmo.robot.Robot):
    self.say_text("For Question 1, you must describe what the special words refer too.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    self.say_text("What do hypotenuse, opposite and adjacent refer too in a triangle?",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    return

def question2T(self: cozmo.robot.Robot):

    self.say_text("For Question 2, you must describe where you can find a special term on a triangle", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    self.say_text("Where is the  hypotenuse located on a triangle?",voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    return

def question3T(self: cozmo.robot.Robot):
    
    self.say_text("For Question 3, you must describe where you can find a special term on a triangle", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    self.say_text("Where is the opposite located on a triangle?",voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    return

def question4T(self: cozmo.robot.Robot):
    
    self.say_text("For Question 4, you must describe where you can find a special term on a triangle", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    self.say_text("Where is the adjacent located on a triangle?",voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    return
def question5T(self: cozmo.robot.Robot):
    
    self.say_text("For Question 5, you must name the associated words.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    self.say_text("What are the three trigonmetic ratios?",voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    return

def question6T(self: cozmo.robot.Robot):
    
    self.say_text("For Question 6, you must name the term used to help you remember functions", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    self.say_text("What term is used to help you remember the trigonmetic ratios?",voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    return

def question7T(self: cozmo.robot.Robot):
    
    self.say_text("For Question 7, you must identify an expression used for the associated term", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    self.say_text("What is the expression for sine?",voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    return

def question8T(self: cozmo.robot.Robot):
    self.say_text("For Question 8, you must identify an expression used for the associated term", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    self.say_text("What is the expression for cosine?",voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    return

def question9T(self: cozmo.robot.Robot):
    
    self.say_text("For Question 9, you must identify an expression used for the associated term", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    self.say_text("What is the expression for tangent?",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    
    return

def question10T(self: cozmo.robot.Robot):
    
    self.say_text("For Question 10, you must work out the angle for a triangle using SOH CAH TOA", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "trigq.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("Work out the missing angle, x, when hypotenuse = 9, opposite = 7 and adjacent=4", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
    return
