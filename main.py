import cozmo
from PIL import Image, ImageDraw, ImageFont

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
#-----------------------------------------------------------------
def cozmo_program(self: cozmo.robot.Robot):
    self.say_text("Hello and welcome to Cozmo Learning", play_excited_animation=True,voice_pitch=-1).wait_for_completed()

def cozmo_button(self: cozmo.robot.Robot):
    self.say_text("hi").wait_for_completed()

def expression_variables(self: cozmo.robot.Robot):
    #self.say_text("Expressions and variables", play_excited_animation=True,voice_pitch=-1).wait_for_completed()
    self.say_text("An algebraic expression comprises both numbers and variables together with at least one arithmetic operation.",use_cozmo_voice=True, voice_pitch=-1,duration_scalar=0.7).wait_for_completed()

#------------------------------write text on Cozmos face---------------------------------------------


def make_text_image(text_to_draw, x, y, font=None):

    text_image = Image.new('RGBA', cozmo.oled_face.dimensions(), (0, 0, 0, 255))    # make a blank image for the text, initialized to opaque black

    dc = ImageDraw.Draw(text_image)                                         # get a drawing context

    dc.text((x, y), text_to_draw, fill=(255, 255, 255, 255), font=font)    # draw the text

    return text_image

#-------get font --------------
_math_font = None
try:
    _math_font = ImageFont.truetype("arial.ttf", 20)
except:
    pass
#--------------------------------
def make_equation_image():
    
    time_text = "test"

    return make_text_image(time_text, 8, 6, _math_font)

def displaytext(robot: cozmo.robot.Robot):

    while True:
        math_image = make_equation_image()                                           # Create the updated image with this time
        oled_face_data = cozmo.oled_face.convert_image_to_screen_data(math_image)
        robot.display_oled_face_image(oled_face_data, 1000.0)                       # display for 1 second

    cozmo.run_program(displaytext)

    
#------------First Screen-------------------------------------------
class MainWindow(Screen):
    def on_pre_enter(self):
        Window.size = (608,600)
    def btn(self):
        show_popup()
        #cozmo.run_program(cozmo_button)
    
    #cozmo.run_program(cozmo_program)


class AlegbraWindow(Screen):
    def on_pre_enter(self):
        Window.size = (608,600)
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
        Window.size = (608,600)

class GeometryWindow(Screen):
    def on_pre_enter(self):
        Window.size = (608,600)

#----------------------------------------------------------------
#-----------------------Tutorials--------------------------------
class AlgebraTutorial(Screen):
        def on_pre_enter(self):
            Window.size = (608,600)
        def checkSection(self):
            self.ids['expression_button'].background_color = 0,1,0,0.5
        def expression_variables(self):
            cozmo.run_program(displaytext)
            cozmo.run_program(expression_variables)        
        



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



