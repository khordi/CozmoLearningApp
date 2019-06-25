import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import time

from displayText import *

#------------------Basic Cozmo movements-------------------------
def cozmo_program(self: cozmo.robot.Robot):
    self.say_text("Hello and welcome to Cozmo Learning", play_excited_animation=True,voice_pitch=-1).wait_for_completed()
def cozmo_button(self: cozmo.robot.Robot):
    self.say_text("hi").wait_for_completed()

def get_in_position(self: cozmo.robot.Robot):
    '''If necessary, Move Cozmo's Head and Lift to make it easy to see Cozmo's face'''
    if (self.lift_height.distance_mm > 45) or (self.head_angle.degrees < 40):
        with self.perform_off_charger():
            lift_action = self.set_lift_height(0.0, in_parallel=True)
            head_action = self.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE,in_parallel=True)
            lift_action.wait_for_completed()
            head_action.wait_for_completed()

def set_lights(self: cozmo.robot.Robot):
    cube1 = self.world.get_light_cube(LightCube1Id) 
    cube2 = self.world.get_light_cube(LightCube2Id)  # looks like a paperclip
    cube3 = self.world.get_light_cube(LightCube3Id) 
    if ('cube1','cube2', 'cube3') is not None:
        cube1.set_light_corners(cozmo.lights.blue_light, cozmo.lights.off_light,cozmo.lights.off_light,cozmo.lights.green_light)
        cube2.set_light_corners(cozmo.lights.red_light, cozmo.lights.green_light,cozmo.lights.off_light,cozmo.lights.red_light)
        cube3.set_light_corners(cozmo.lights.blue_light, cozmo.lights.red_light,cozmo.lights.red_light,cozmo.lights.off_light)

        time.sleep(20)
    return

#----------------------------------------------------------------

#add some random sayings here so the robot doesnt become so boring and 
#predictable, make sure the the code selects at random 

#---------------------Algebra Tutorials--------------------------
def WhatisAlgebra(self: cozmo.robot.Robot):
    start = 0
    print(start)
    if start == 0 :
        self.say_text("Welcome! Lets start learning Algebra!", play_excited_animation=True,voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.say_text("Algebra encompasses relationships, symbols and the study of change. We use this in our everyday lifes. for example: working out the cost for food, or house rent.",voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()    
        self.say_text("The main purpose of Algebra is to show math relationships by using letters and numbers", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.say_text("You can learn Algebra by using the tutorials and then practice what you have learned with the Questions and Answers", play_excited_animation= True, voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        start = 1
        print(start)
    elif start == 1:
        pass


def expression_variables(self: cozmo.robot.Robot):
    self.say_text("Welcome to expressions and variables", play_excited_animation=True,voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.say_text("An algebraic expression is made of both numbers and variables aswell as an arithmetic operation. An example of this is:", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    return

def combining_liketerms1(self: cozmo.robot.Robot):
    self.say_text("Welcome to combining like terms", play_excited_animation=True, voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.say_text("Combining like terms or variables can help make expressions easier to understand and work with. For example:", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    return

def combining_liketerms2(self: cozmo.robot.Robot):
    self.say_text("This can be simplified to:", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    return

def sub_evaluate(self: cozmo.robot.Robot):
    self.say_text("Welcome to substitution and evaluation", play_excited_animation=True, voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.say_text("An expression can be evaluated if the variables are known to us. For example:", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    
    
def expression_words(self: cozmo.robot.Robot):
    self.say_text("Welcome to expression and word problems",play_excited_animation=True, voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.say_text("Lets test everything you have learned so far! Are you ready?", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.say_text("A raffle is being held to make money for charity. The individual cost of participating in the raffle is give by the following expression:", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    return

def algebraic_equations(self: cozmo.robot.Robot):
    self.say_text("Welcome to Equivalent algebraic equations", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.say_text("Finding the equivalent equation can help simplify your question, for example:", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    return

#---------------------------------------------------------------------------------------

_math_font = None  #try removing the try and except and = this to font etc
try:
    _math_font = ImageFont.truetype("arial.ttf", 25)
except:
    pass
    
def displaytext_1(self: cozmo.robot.Robot):
    cube2 = self.world.get_light_cube(LightCube2Id)  # looks like a paperclip
    #cube2 = self.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart

    while True:
        math_image = make_text_image("2x + 4", 8, 6, _math_font)                                          # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 2000.0)                       # display for 1 second
        time.sleep(5)
        break

    if ('cube2') is not None:
        cube2.set_lights(cozmo.lights.green_light)
        #cube2.set_lights(cozmo.lights.red_light)

    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")
    
    try:
        self.say_text("Tap the Green cube if you are ready to move onto the next tutorial. You can come back anytime an revisit this topic, i'd be happy to help", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.say_text("", play_excited_animation=True, voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        cube2.wait_for_tap()

    except:
        return

def displaytext_2(self: cozmo.robot.Robot):
    while True:
        math_image = make_text_image("2x + 2y + 5y +7x", 8, 6, _math_font)  # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 2000.0).wait_for_completed() # display for 1 second
        break
    return

def displaytext_3(self: cozmo.robot.Robot):
    while True:
        math_image = make_text_image("9x + 7y", 8, 6, _math_font)    # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 2000.0).wait_for_completed()   # display for 1 second
        break
    return

def displaytext_4(self: cozmo.robot.Robot):
    while True:
        math_image = make_text_image("2x + 2y", 8, 6, _math_font)  # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 2000.0, in_parallel=True)
        self.say_text("Where x = 2 and y =1. If we substitute these into our expression and evaluate, then we will get:", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break
    return

def displaytext_5(self: cozmo.robot.Robot):
    while True:
        math_image = make_text_image("2(2) + 2(1)", 8, 6, _math_font)  # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 2000.0, in_parallel=True)  # display for 1 second
        self.say_text("Which equals to 6", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break
    return

def displaytext_6(self: cozmo.robot.Robot):
    cube2 = self.world.get_light_cube(LightCube2Id)  # looks like a paperclip
    tap = 0
    while True:
        math_image = make_text_image("3t + 4t + 4", 8, 6, _math_font)  # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 2000.0, in_parallel=True)  # display for 1 second
        self.say_text("Where t represents the number of tickets someone purchases. Evaluate the expression when t=4.", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break
    
    if ('cube2') is not None:
        cube2.set_lights(cozmo.lights.blue_light)
        #cube2.set_lights(cozmo.lights.red_light)

    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")
    
    
    #self.say_text("When you have worked out the answer, tap the blue cube equal to the amount you calculated for the answer", play_excited_animation=True, voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while tap < 5:
        
        cube2.wait_for_tap()
        tap += 1  # This is the same as count = count + 1   

    time.sleep(1)
    return 

def displaytext_7(self: cozmo.robot.Robot):
    while True:
        math_image = make_text_image("2(4x + 7y)", 8, 6, _math_font)  # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 2000.0, in_parallel=True)  # display for 1 second
        self.say_text("Which is the same as", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break
    return    

def displaytext_8(self: cozmo.robot.Robot):
    while True:
        math_image = make_text_image("8x + 14y", 8, 6, _math_font)  # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 2000.0, in_parallel=True)  # display for 1 second
        self.say_text("", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break
    return