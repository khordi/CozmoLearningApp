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
#----------------------------------------------------------------
def cozmo_program(self: cozmo.robot.Robot):
    self.say_text("Hello and welcome to Cozmo Learning", play_excited_animation=True,voice_pitch=-1).wait_for_completed()
def cozmo_button(self: cozmo.robot.Robot):
    self.say_text("hi").wait_for_completed()
#----------------------------------------------------------------

#---------------------Algebra Tutorials--------------------------

def expression_variables(self: cozmo.robot.Robot):
    self.say_text("Welcome to expressions and variables", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    self.say_text("An algebraic expression is made of both numbers and variables aswell as an arithmetic operation. An example of this is:", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
    return

def sub_evaluate(self: cozmo.robot.Robot):
    self.say_text("Welcome to substitution and evaluation", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    return

def expression_words(self: cozmo.robot.Robot):
    self.say_text("Welcome to expression and word problems", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

    return

def combining_liketerms(self: cozmo.robot.Robot):
    self.say_text("Welcome to combining like terms", voice_pitch=0,duration_scalar=0.6).wait_for_completed()

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
    _math_font = ImageFont.truetype("arial.ttf", 20)
except:
    pass
def make_equation_image():
    
    time_text = "2x + 4x = 0"

    return make_text_image(time_text, 8, 6, _math_font)
def displaytext(self: cozmo.robot.Robot):
    cube1 = self.world.get_light_cube(LightCube1Id)  # looks like a paperclip
    cube2 = self.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart

    while True:
        math_image = make_equation_image()                                           # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        self.display_oled_face_image(oled_face_data, 1000.0)                       # display for 1 second
        time.sleep(5)
        break

    if ('cube1','cube2') is not None:
        cube1.set_lights(cozmo.lights.green_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")
    
    try:
        self.say_text("Tap the Green cube if you are ready to move onto the next tutorial. You can come back anytime an revisit this topic, i'd be happy to help", voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        self.say_text("", play_excited_animation=True, voice_pitch=0,duration_scalar=0.6).wait_for_completed()
        cube1.wait_for_tap()

    except:
        return
    
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
#-----------------------Tutorials--------------------------------
class AlgebraTutorial(Screen):

        def on_pre_enter(self):
            Window.size = (608,608)

        def checkSection(self):
            self.ids['expression_button'].background_color = 0,1,0,0.5

        def expression_variables(self):
            cozmo.run_program(expression_variables)
            cozmo.run_program(displaytext)

        def sub_evaluate(self):
            cozmo.run_program(sub_evaluate)

        def expression_words(self):
            cozmo.run_program(expression_words)
        
        def combining_liketerms(self):
            cozmo.run_program(combining_liketerms)

        def algebraic_equations(self):
            cozmo.run_program(algebraic_equations)
        #def
        #def

class TrigPythTutorial(Screen):
    pass

class GeometryTutorial(Screen):
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



