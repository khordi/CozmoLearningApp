import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import time
import os

from displayText import *
current_directory = os.path.dirname(os.path.realpath(__file__))

def triangleSide(self: cozmo.robot.Robot):
    self.say_text("Welcome to Triangle Sides", play_excited_animation=True,voice_pitch=-1).wait_for_completed()
    self.say_text("We use special words to describe the sides of right triangles.",voice_pitch=-1).wait_for_completed()
    return

def displayHypo(self: cozmo.robot.Robot):
    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images", "triangle.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("The hypotenuse of a right triangle is always the side opposite the right angle. ", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        #time.sleep(2)
        break
    return