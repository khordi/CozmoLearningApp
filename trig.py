import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import degrees, distance_mm, speed_mmps

import time
import os

from displayText import *
current_directory = os.path.dirname(os.path.realpath(__file__))

def triangleSide(self: cozmo.robot.Robot):
    self.say_text("Welcome to learning about triangle definitions!", play_excited_animation=True,voice_pitch=-1,duration_scalar=0.6).wait_for_completed()
    self.say_text("In trigonometry we use special words to describe the sides of right angle triangles. which are labelled as H,O,Ae and refer to the length of the sides.",voice_pitch=-1,duration_scalar=0.6).wait_for_completed()
    return

def displayHOA(self: cozmo.robot.Robot):

    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "triangleH.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("The hypotenuse of a right triangle is always the side opposite the right angle and always the longest side of a triangle ", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break

    self.say_text("There are two more sides which are labeled in relation to an angle.",voice_pitch=-1,duration_scalar=0.6).wait_for_completed()
    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "triangleO.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("The label opposite, is a side across from a given angle", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break

    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "triangleA.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("and the adjacent side is the non-hypotenuse side that is next to a given angle", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        time.sleep(1)
        break

    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "triangleHOA.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("Putting it all together from the perspective of the given angle gives us this", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break

    return

def trigratio(self: cozmo.robot.Robot):
    self.say_text("From the triangle sides tutorial, we learned that the hypotenuse, opposite, and adjacent referred to the lengths of the sides. Now we will learn trigonmetic ratios", play_excited_animation=True,voice_pitch=-1,duration_scalar=0.6).wait_for_completed()
    self.set_lift_height(0.0, in_parallel=True).wait_for_completed()
    self.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE,in_parallel=True).wait_for_completed()

    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "sine.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("The three common ratios are sine", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()

        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "cos.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("cosine", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()

        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "tan.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text(" and tangent", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()

        break
    self.say_text("These ratios can be remembered using the phrase SOH CAH TOA", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()

    return

def displaysin(self: cozmo.robot.Robot):
    self.say_text("Lets learn the ratio sine first", play_excited_animation=True,voice_pitch=-1,duration_scalar=0.6).wait_for_completed()
    self.set_head_angle(degrees(90)).wait_for_completed()

    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "ratioO.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("sine of the angle X is given by the opposite ", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()

        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "ratioOH.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("over hypotenuse. This is shown as an expression:", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        #time.sleep(1)

        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "sinex.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("and can be remembered using SOH, where S is sine, O is opposite, and H is hypotenuse", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        time.sleep(3)
        break

def displaycos(self: cozmo.robot.Robot):
    self.say_text("Lets learn the ratio cosine now", play_excited_animation=True,voice_pitch=-1,duration_scalar=0.6).wait_for_completed()
    self.set_head_angle(degrees(90)).wait_for_completed()

    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "ratioA.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("cos of the angle X is given by the adjacent ", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()

        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "ratioAH.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("over hypotenuse. This is shown as an expression:", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        #time.sleep(1)
        
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "cosx.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("and can be remembered using cah, where C is cos, A is adjacent, and H is hypotenuse", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        time.sleep(3)
        break
    return

def displaytan(self: cozmo.robot.Robot):
    self.say_text("Lastly lets learn the ratio tangent", play_excited_animation=True,voice_pitch=-1,duration_scalar=0.6).wait_for_completed()
    self.set_head_angle(degrees(90)).wait_for_completed()

    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "ratioO.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("tan of the angle X is given by the opposite ", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()

        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "ratioOA.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("over adjacent. This is shown as an expression:", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        #time.sleep(1)

        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "tanx.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        self.say_text("and can be remember using TOA, where T is tan, O is opposite, and A is adjacent", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        time.sleep(3)
        break
    return