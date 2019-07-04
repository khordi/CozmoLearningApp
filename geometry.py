import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import time
import os

from PIL import Image, ImageDraw, ImageFont


current_directory = os.path.dirname(os.path.realpath(__file__))



def angleTut(self: cozmo.robot.Robot):
    #intro to angle with example
    self.say_text("An angle is two rays that share the same vertex. Intersecting lines can also form angles: Angles are also measured in degrees.", play_excited_animation=True,voice_pitch=-1,duration_scalar=0.6).wait_for_completed()
    self.say_text("As an example, if i drive from point A to point B",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed()
    self.say_text("turn 45 degrees",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.turn_in_place(degrees(45)).wait_for_completed()
    self.say_text("then move from point B to point C. Both rays AB and BC will share the angle which was made at this point",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed()
    self.turn_in_place(degrees(-45)).wait_for_completed()
    time.sleep(2)
    #explaining the different types of angles
    self.say_text("There are also 4 types of angles. Lets begin at 0 facing North.",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.turn_in_place(degrees(180)).wait_for_completed()
    
    self.say_text("The first type is Acute angle and is measured between 0 and 90 degrees.",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.turn_in_place(degrees(-90)).wait_for_completed()
    
    self.say_text("The second type is right angle and is exactly 90 degrees ",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    
    self.say_text("The third type is obtuse angle and is measured between 90 and 180 degrees",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.turn_in_place(degrees(-90)).wait_for_completed()

    self.say_text("The forth type is straight angle and is exactly 180 degrees",voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    return 

def shapes(self: cozmo.robot.Robot):
    #recognizing the different types of shapes
    self.say_text("There are various shapes that you will encounter everywhere. Shapes can be categorized into many groups, lets learn them!",voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "circle.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("Lets start off with the easy group... Circles!", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break

    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "circle-arrows.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("A circle is recognized when the length through the centre is the same all the way round the shape", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break
    
    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "triangle.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("The second group is triangles, which has three sides or corners", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break
   # self.say_text("There is also types of angles triangles that are named by their angles. These names should be familar, acute triangle, where all angles are l, right triangles where 1 angle is 90 degrees", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()


    self.say_text("The following groups can be also be grouped under quadrilaterals", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "rectangle.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("The third group is rectangle", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break

    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "rectangle-ra.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("which has 4 sides and is distinguished by its 4 right angle corners. ", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break
    
    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "rhombus.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("The fourth group is Rhombus, which has 4 even sides but no right angle corners", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break

    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "square.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("The fifth group is square", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break

    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "square-ra.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("which has characteristics of both rectangle and rhombus groups. it has 4 even sides and 4 right angle triangle corners", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break
    
    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "trapezoid.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("The last group is trapezoid, which has 4 sides where 2 are parallel sides and the other 2 are not ", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break

    return

def areatut(self: cozmo.robot.Robot):

    self.say_text("Area is the measure of how much 2-dimensional space something takes up. This can be useful to know. for example, if you need to work out how much paint is needed to cover a wall", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()

    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "area-rec.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("This simple example shows this rectangle has an area of 8 square units", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break
    self.say_text("lets use a practical example, lets 1 of my cubes measure 1 square unit on its length and width. If we join three of my cubes together to make a rectangle how much area do they take up if Area equals length times width", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       

    #cube1 = self.world.get_light_cube(LightCube1Id) 
    #cube2 = self.world.get_light_cube(LightCube2Id)  # looks like a paperclip
    #cube3 = self.world.get_light_cube(LightCube3Id) 
    #if ('cube1','cube2', 'cube3') is not None:
    #    cube1.set_light_corners(cozmo.lights.blue_light, cozmo.lights.off_light,cozmo.lights.off_light,cozmo.lights.green_light)
        #cube2.set_light_corners(cozmo.lights.red_light, cozmo.lights.green_light,cozmo.lights.off_light,cozmo.lights.red_light)
        #cube3.set_light_corners(cozmo.lights.blue_light, cozmo.lights.red_light,cozmo.lights.red_light,cozmo.lights.off_light)

    #    time.sleep(20)

    return

def perimeter(self: cozmo.robot.Robot):
    self.say_text("perimeter is the distance around the outside of a 2D shape", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       

    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "trapezoid-perimeter.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("We can find the perimeter of this shape my simply adding all the side lengths. 2+3+5+3 equals 13 centimeters", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break

    return

def volumetut(self: cozmo.robot.Robot):
    
    self.say_text("Volume is the amount of 3-dimensional space something takes up. A good example of this is how much water can a bucket hold.", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()

    while True:
        resampling_mode = Image.BICUBIC
        image_name = os.path.join(current_directory, "face_images","shapes", "volume.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("For this example the volume is worked out by 8 time 3 times 1 which equals 24 units cubed", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()       
        break


    return

def pythagoras(self: cozmo.robot.Robot):
    
    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images","shapes", "pythag.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("The pythagoras theorem states that the square of the hypotenuse, which is opposit the right angle, is equal to the sum of the squares of the other two sides", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed()
        break

    while True:
        resampling_mode = Image.NEAREST
        image_name = os.path.join(current_directory, "face_images","shapes", "pythag-form.png")
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        self.display_oled_face_image(face_image, 2000.0, in_parallel=True)
        self.say_text("This can be written as, Ae squared equals B squared plus C squared", voice_pitch=0,duration_scalar=0.6, in_parallel=True).wait_for_completed() 
        break

    return