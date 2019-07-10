import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import degrees
import time

from displayText import *

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

def question1A(self: cozmo.robot.Robot):
    self.say_text("For Question 1, you must identify the variables used in the expression.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        math_image = make_text_image("10x+4y+b", 8, 6, _math_font)                                          # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 3000.0)                       # display for 1 second
        self.say_text("The expression is: 10x + 4y + b", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        self.set_head_angle(degrees(0)).wait_for_completed()
        break
    return

def question2A(self: cozmo.robot.Robot):
    self.say_text("For Question 2, you must simplify the expression by combining the like terms.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        math_image = make_text_image("7x-5x+2y-2y", 8, 6, _text_font)                                          # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 3000.0)                       # display for 1 second
        self.say_text("The expression is: 7x minus 5x + 2y minus 2y", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        self.set_head_angle(degrees(0)).wait_for_completed()
        break
    return
  
def question3A(self: cozmo.robot.Robot):
    self.say_text("For Question 3, you must simplify the expression and solve for y", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        math_image = make_text_image("x+8 = 2y-7", 8, 6, _math_font)                                          # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 3000.0)                       # display for 1 second
        self.say_text("The expression is: x + 8 = 2y minus 7", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        self.set_head_angle(degrees(0)).wait_for_completed()
        break
    return

def question4A(self: cozmo.robot.Robot):
    self.say_text("For Question 4, you must simplify the expression and evaluate.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        math_image = make_text_image("  11x-4x+1", 8, 6, _text_font)                                          # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 3000.0)                       # display for 1 second
        self.say_text("The expression is: 11x minus 4x + 1, where x = 2", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        self.set_head_angle(degrees(0)).wait_for_completed()
        break
    return

def question5A(self: cozmo.robot.Robot):
    self.say_text("For Question 5, you must simplify the expression and evaluate. solving for x", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        math_image = make_text_image("x-4y = 2x-2y", 8, 6, _text_font)                                          # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 3000.0)                       # display for 1 second
        self.say_text("The expression is: x minus 4y = 2x minus 2y, where y = 5", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        self.set_head_angle(degrees(0)).wait_for_completed()
        break
    return

def question6A(self: cozmo.robot.Robot):
    self.say_text("For Question 6, you must simplify the expression to its final form.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        math_image = make_text_image("2(3x+8)+2", 8, 6, _math_font)                                          # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 3000.0)                       # display for 1 second
        self.say_text("The expression is: 3x+8 multiplied by 2,  plus 2", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        self.set_head_angle(degrees(0)).wait_for_completed()
        break
    return

def question7A(self: cozmo.robot.Robot):
    self.say_text("For Question 7, you must simplify the expression to its final form.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        math_image = make_text_image("(x+7)+2(2y+2x)", 8, 6, _text_font)                                          # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 3000.0)                       # display for 1 second
        self.say_text("The expression is: x+7, plus 2y+2x multiplied by 2", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        self.set_head_angle(degrees(0)).wait_for_completed()
        break
    return

def question8A(self: cozmo.robot.Robot):
    self.say_text("For Question 8, you must create an expression from the following sentence.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.say_text("Mark needs to work out how many apples and oranges he ate, He started with 10 apples, and 5 oranges, he ate 4 apples and ate 2 oranges. Write an expression to help mark work this out", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    return

def question9A(self: cozmo.robot.Robot):
    self.say_text("For Question 9, you must evaluate the following expression.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    while True:
        math_image = make_text_image("3.5b+1.5h", 8, 6, _math_font)                                          # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 3000.0)                       # display for 1 second
        self.say_text("Tom owns a hot-food truck. The expression, 3.5b + 1.5h gives the cost of burgers, and hot dogs. What is the cost of 2 burgers and 3 hotdogs.", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        self.set_head_angle(degrees(0)).wait_for_completed()
        break
    return

def question10A(self: cozmo.robot.Robot):
    self.say_text("For Question 10, you must evaluate the following expression.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    while True:
        math_image = make_text_image("2(1.5t+8)", 8, 6, _math_font)                                          # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 3000.0)                       # display for 1 second
        self.say_text("The expression, 1.5t + 8 multiplied by 2 predicts the height in centimeters of a plant t days from today. what is the height of the plant 3 days from today. ", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        self.set_head_angle(degrees(0)).wait_for_completed()
        break
    return



