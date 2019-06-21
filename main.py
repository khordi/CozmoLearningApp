import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

from PIL import Image, ImageDraw, ImageFont
import time
import asyncio

from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy import Eq, solve_linear_system, Matrix
import sympy as sp

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, FadeTransition
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout



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
            head_action = self.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE,
                                               in_parallel=True)
            lift_action.wait_for_completed()
            head_action.wait_for_completed()



#----------------------------------------------------------------

#---------------------Algebra Tutorials--------------------------

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
    return


def expression_words(self: cozmo.robot.Robot):
    self.say_text("Welcome to expression and word problems",play_excited_animation=True, voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.say_text("Lets test everything you have learned so far! Are you ready?", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.say_text("A raffle is being held to make money for charity. The individual cost of participating in the raffle is give by the following expression:", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    return



def algebraic_equations(self: cozmo.robot.Robot):
    self.say_text("Welcome to algebraic equations", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    return
#----------------------------------------------------------------

#--------------------Display writing on Cozmo--------------------

def make_text_image(text_to_draw, x, y, font=None):

    text_image = Image.new('RGBA', cozmo.oled_face.dimensions(), (0, 0, 0, 255))    # make a blank image for the text, initialized to opaque black

    dc = ImageDraw.Draw(text_image)                                         # get a drawing context

    dc.text((x, y), text_to_draw, fill=(255, 255, 255, 255), font=font)    # draw the text

    return text_image
    
_math_font = None  #try removing the try and except and = this to font etc
try:
    _math_font = ImageFont.truetype("arial.ttf", 25)
except:
    pass
#----------------------------------------------------------------

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
        self.play_anim()
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
    return None
    
#----------------------First Screen------------------------------
class MainWindow(Screen):
    def on_pre_enter(self):
        Window.size = (608,608)
    def btn(self):
        show_popup()
        #cozmo.run_program(cozmo_button)
    
    #cozmo.run_program(cozmo_program)

class AlegbraWindow(Screen):

    def on_pre_enter(self):
        Window.size = (608,608)
    def algebraSolver(self):
        #x = 0
        #y = 0
        #eq1 = sp.Function('eq1')
        #eq2 = sp.Function('eq2')

        #eq1 = Eq(2*x - y,-4)
        #eq2 = Eq(3*x - y,-2)
        
        x,y = sp.symbols('x y')
        row1 = [2, -2, -4]
        row2 = [6, -8, -2]

        system = Matrix((row1,row2))
        print(solve_linear_system(system,x,y))

class TrigPythWindow(Screen):
    def on_pre_enter(self):
        Window.size = (608,608)

class GeometryWindow(Screen):
    def on_pre_enter(self):
        Window.size = (608,608)

#----------------------------------------------------------------
#------------------Tutorials/Q's & A's---------------------------
class AlgebraTutorial(Screen):

    def enableButtonSub(self):
        self.ids.button_sub.disabled = False
    def enableButtonComb(self):
        self.ids.combining_button.disabled = False
    def enableButtonExp(self):
        self.ids.expression_words_button.disabled = False
    def enableButtonAlge(self):
        self.ids.algebraic_button.disabled = False

    def on_pre_enter(self):
        Window.size = (608,608)

    def completed1(self):
        self.ids.expression_button.background_color = 0,1,0,0.5
        
    def completed2(self):
        self.ids.combining_button.background_color = 0,1,0,0.5

    def completed3(self):
        self.ids.button_sub.background_color = 0,1,0,0.5

    def completed4(self):
        self.ids.expression_words_button.background_color = 0,1,0,0.5

    def completed5(self):
        self.ids.combining_button.background_color = 0,1,0,0.5

    
        

    def expression_variables(self): #introducing expressions with a variable
        #cozmo.run_program(expression_variables)
        #cozmo.run_program(get_in_position)
        #cozmo.run_program(displaytext_1)
        return

    def combining_liketerms(self):
        #cozmo.run_program(combining_liketerms1)
        #cozmo.run_program(displaytext_2)
        #cozmo.run_program(combining_liketerms2)
        #cozmo.run_program(displaytext_3)
        return

    def sub_evaluate(self): #introducing expressions with more than one variable
        #cozmo.run_program(sub_evaluate)
        #cozmo.run_program(displaytext_4)
    #    cozmo.run_program(displaytext_5)

        return

    def expression_words(self: cozmo.robot.Robot): #word example of using past three topics
    #    cozmo.run_program(expression_words)
    #    cozmo.run_program(displaytext_6)
        return
        
    
    def algebraic_equations(self):
    #    cozmo.run_program(algebraic_equations)
    #def
    #def
        return
class AlegbraQnA(Screen):
    pass

class TrigPythTutorial(Screen):
    pass
class TrigPythQnA(Screen):
    pass

class GeometryTutorial(Screen):
    pass
class GeometryQnA(Screen):
    pass
#----------------------------------------------------------------

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        self.title = 'Cozmo Learning App'
        return kv

class HELP(FloatLayout):
    pass

def show_popup():
    show = HELP() # Create a new instance of the P class 

    popupWindow = Popup(title="Help", content=show, size_hint=(None,None),size=(400,400)) 
    # Create the popup window

    popupWindow.open() # show the popup

    
if __name__ == "__main__":
    MyMainApp().run()





