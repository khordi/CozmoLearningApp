import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import time
import os

from displayText import *
current_directory = os.path.dirname(os.path.realpath(__file__))

def triangleSide(self: cozmo.robot.Robot):
    self.say_text("Welcome to learning about trigonometric ratios", play_excited_animation=True,voice_pitch=-1,duration_scalar=0.6).wait_for_completed()
    self.say_text("In trigonometry we use special words to describe the sides of right angle triangles. which are labelled as H,O,A and refer to the length of the sides.",voice_pitch=-1,duration_scalar=0.6).wait_for_completed()
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
    return

def displayratio(self: cozmo.robot.Robot):
    
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
        self.say_text("over hypotenuse. This is shown as a fraction:", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        #time.sleep(1)

        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "sinex.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        #self.say_text("the opposite over hypotenuse. This is shown as:", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        time.sleep(3)
        break

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
        self.say_text("over hypotenuse. This is shown as a fraction:", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        #time.sleep(1)
        
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "cosx.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        #self.say_text("the opposite over hypotenuse. This is shown as:", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        time.sleep(3)
        break

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
        self.say_text("over adjacent. This is shown as a fraction:", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        #time.sleep(1)

        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "tanx.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 3000.0, in_parallel=True)
        #self.say_text("the opposite over hypotenuse. This is shown as:", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        time.sleep(3)
        break
    
    return
