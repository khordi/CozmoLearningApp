import cozmo

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
    self.say_text("hi").wait


    
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



