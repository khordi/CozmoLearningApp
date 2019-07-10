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

def question1G(self: cozmo.robot.Robot):
    self.say_text("For Question 1, you must identify what point two lines share.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()


    self.say_text("if i drive from point A to point B",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed()
    self.say_text("turn 20 degrees",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.turn_in_place(degrees(20)).wait_for_completed()
    self.say_text("then move from point B to point C. ",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed()
    self.turn_in_place(degrees(-20)).wait_for_completed()
    self.say_text("What point does AB and BC share?",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
   
    time.sleep(2)
    return

def question2G(self: cozmo.robot.Robot):
    rand = (random.randint(1,4))
    print(rand)
    if rand == 1:
        self.say_text("For Question 2, you must identify the type of the angle cozmo makes", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.turn_in_place(degrees(45)).wait_for_completed()
        self.say_text("I turned 45 degrees, what type of angle is this?", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.turn_in_place(degrees(-45)).wait_for_completed() 
        return
    elif rand == 2:
        self.say_text("For Question 2, you must identify the name of the angle cozmo makes", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.turn_in_place(degrees(90)).wait_for_completed()
        self.say_text("I turned 90 degrees, what type of angle is this?", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.turn_in_place(degrees(-90)).wait_for_completed()
        return
    elif rand == 3:  
        self.say_text("For Question 2, you must identify the name of the angle cozmo makes", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.turn_in_place(degrees(135)).wait_for_completed()
        self.say_text("I turned 135 degrees, what type of angle is this?", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.turn_in_place(degrees(-135)).wait_for_completed()
        return
    elif rand == 4:    
        self.say_text("For Question 2, you must identify the name of the angle cozmo makes", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.turn_in_place(degrees(180)).wait_for_completed()
        self.say_text("I turned 180 degrees, what type of angle is this?", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.turn_in_place(degrees(-180)).wait_for_completed()
        return
    return

def question3G(self: cozmo.robot.Robot):
    
    self.say_text("For Question 3, you will need to match the shapes to the question.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    rand = (random.randint(1,3))

    if rand == 1: 
        self.say_text("which shape is a circle?", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        while True:
            resampling_mode = Image.BICUBIC
            image_name = os.path.join(current_directory, "face_images","shapes", "square.png")
            image = Image.open(image_name)
            resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
            face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
            self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
            self.say_text("Is it: A", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
            break
        while True:
            resampling_mode = Image.BICUBIC
            image_name = os.path.join(current_directory, "face_images","shapes", "triangle.png")
            image = Image.open(image_name)
            resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
            face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
            self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
            self.say_text("B", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
            break
        while True:
            resampling_mode = Image.BICUBIC
            image_name = os.path.join(current_directory, "face_images","shapes", "circle.png")
            image = Image.open(image_name)
            resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
            face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
            self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
            self.say_text(" or C", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
            break
    elif rand == 2: 
        self.say_text("Which of these shapes are quadrilaterals?", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        while True:
            resampling_mode = Image.BICUBIC
            image_name = os.path.join(current_directory, "face_images","shapes", "square.png")
            image = Image.open(image_name)
            resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
            face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
            self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
            self.say_text("Is it: A", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
            break
        while True:
            resampling_mode = Image.BICUBIC
            image_name = os.path.join(current_directory, "face_images","shapes", "trapezoid.png")
            image = Image.open(image_name)
            resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
            face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
            self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
            self.say_text("B", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
            break
        while True:
            resampling_mode = Image.BICUBIC
            image_name = os.path.join(current_directory, "face_images","shapes", "circle.png")
            image = Image.open(image_name)
            resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
            face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
            self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
            self.say_text("C", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
            break
        while True:
            resampling_mode = Image.BICUBIC
            image_name = os.path.join(current_directory, "face_images","shapes", "rhombus.png")
            image = Image.open(image_name)
            resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
            face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
            self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
            self.say_text(" or D", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
            break
    elif rand == 3: 
        self.say_text("which shape is a trapezoid?", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        while True:
            resampling_mode = Image.BICUBIC
            image_name = os.path.join(current_directory, "face_images","shapes", "trapezoid.png")
            image = Image.open(image_name)
            resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
            face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
            self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
            self.say_text("Is it: A", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
            break
        while True:
            resampling_mode = Image.BICUBIC
            image_name = os.path.join(current_directory, "face_images","shapes", "trapezoid1.png")
            image = Image.open(image_name)
            resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
            face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
            self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
            self.say_text("B", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
            break
        while True:
            resampling_mode = Image.BICUBIC
            image_name = os.path.join(current_directory, "face_images","shapes", "trapezoid2.png")
            image = Image.open(image_name)
            resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
            face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
            self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
            self.say_text(" or C", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
            break
        while True:
            resampling_mode = Image.BICUBIC
            image_name = os.path.join(current_directory, "face_images","shapes", "rhombus.png")
            image = Image.open(image_name)
            resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
            face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
            self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
            self.say_text(" or D", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
            break
    return

def question4G(self: cozmo.robot.Robot):
    self.say_text("For Question 4, you will need to identify the shape that matches the description of the question.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    time.sleep(1)
    self.say_text("which shape has characteristics of both rectangle and rhombus groups.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    return

def question5G(self: cozmo.robot.Robot):
    self.say_text("For Question 5, you will need to work out the area of the rectangle.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    
    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "rectangleq.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("If the length equals 7 and the width equals 3 what is the Area of the rectangle?", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break
    return

def question6G(self: cozmo.robot.Robot):
    self.say_text("For Question 6, you will need to work out the area of the triangle.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    
    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images", "triangleqg.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("If the base equals 4 and the height equals 7 what is the Area of the rectangle?", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break

    return

def question7G(self: cozmo.robot.Robot):
    self.say_text("For Question 7, you will need to work out how long the sides of a rhombus is using perimeter.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "rhombusq.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("if the total perimeter of this rhombus is 48 centimetres, what length is side x?", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break
    return

def question8G(self: cozmo.robot.Robot):
    self.say_text("For Question 8, you will need to work out the perimeter of the rectangle.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "rectangleq.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("If the length equals 7 and the width equals 3 what is the perimeter of the rectangle?", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break
    return

def question9G(self: cozmo.robot.Robot):
    
    self.say_text("For Question 9, you will need to work out the volume of the rectangle.", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "volume.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("If the length equals 4, the breadth equals 3 and the width equals 1 what is the volume of the rectangle?", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()         
        break

def question10G(self: cozmo.robot.Robot):

    self.say_text("For Question 10, work out x on the triangle using pythagoras", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "trianglex.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("where b = 7 and a = 4", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break
    return





