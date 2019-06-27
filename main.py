from kivy.config import Config
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '608')
Config.set('graphics', 'height', '608')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, FadeTransition
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

from algebra import *
from trig import *


from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy import Eq, solve_linear_system, Matrix
import sympy as sp
#----------------------First Screen------------------------------
class MainWindow(Screen):
    def btn(self):
        show_popup()
        #cozmo.run_program(cozmo_button)
    def WhatisAlgebra(self):
        cozmo.run_program(WhatisAlgebra)
        return
    
    #cozmo.run_program(cozmo_program)

class AlegbraWindow(Screen):
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


class trigWindow(Screen):
    pass

class GeometryWindow(Screen):
    pass

#-----------------Tutorials/Q's & A's--------------------------------------------------------------


#--------------------------ALGEBRA------------------------------
class AlgebraTutorial(Screen):
# call cozmo functions here to link up kivy and cozmo
    # enable buttons
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

    # change button when completed
    def completed1(self):
        self.ids.expression_button.background_color = 0,1,0,0.5
        
    def completed2(self):
        self.ids.combining_button.background_color = 0,1,0,0.5

    def completed3(self):
        self.ids.button_sub.background_color = 0,1,0,0.5

    def completed4(self):
        self.ids.expression_words_button.background_color = 0,1,0,0.5

    def completed5(self):
        self.ids.algebraic_button.background_color = 0,1,0,0.5

    
        

    def expression_variables(self): #introducing expressions with a variable
        #cozmo.run_program(expression_variables)
        #cozmo.run_program(get_in_position)
        #cozmo.run_program(displaytext_1)
        #cozmo.run_program(set_lights)
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
        #cozmo.run_program(displaytext_5)
        return

    def expression_words(self: cozmo.robot.Robot): #word example of using past three topics
        #cozmo.run_program(expression_words)
        #cozmo.run_program(displaytext_6)
        return
        
    
    def algebraic_equations(self):
        #cozmo.run_program(algebraic_equations)
        #cozmo.run_program(displaytext_7)
        #cozmo.run_program(displaytext_8)
        return

class AlegbraQnA(Screen):
# needs completed, make up 10 questions easy,medium and hard difficulty
#
    pass


 

#----------------------TRIG AND PYTHAG--------------------------
class trigTutorial(Screen):

    def triangleSides(self):
        #cozmo.run_program(triangleSide)
        #cozmo.run_program(get_in_position)
        #cozmo.run_program(displayHOA)
        return
    

    def sohcahtoa(self):
        #cozmo.run_program(trigratio)
        #cozmo.run_program(get_in_position)
        #cozmo.run_program(displayratio)
        return






class trigQnA(Screen):
    pass


#--------------------------GEOMETRY------------------------------
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





