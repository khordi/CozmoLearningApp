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
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

from algebra import *
from trig import *
from geometry import *

 
from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy import Eq, solve_linear_system, Matrix
import sympy as sp

#----------------------Main Screen------------------------------

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

    def titleSection(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n')
        appendFile.write('\n Algebra Answers')
        appendFile.close()

class TrigWindow(Screen):
    def titleSection(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n')
        appendFile.write('\n Trig Answers')
        appendFile.close()    
    pass

class GeometryWindow(Screen):
    def titleSection(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n')
        appendFile.write('\n Geometry Answers')
        appendFile.close()    
    pass

#--------------------------ALGEBRA------------------------------

class AlgebraTutorial(Screen):

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
        cozmo.run_program(expression_variables)
        cozmo.run_program(get_in_position)
        cozmo.run_program(displaytext_1)
        return

    def combining_liketerms(self):
        cozmo.run_program(combining_liketerms1)
        cozmo.run_program(displaytext_2)
        cozmo.run_program(combining_liketerms2)
        cozmo.run_program(displaytext_3)
        return

    def sub_evaluate(self): #introducing expressions with more than one variable
        cozmo.run_program(sub_evaluate)
        cozmo.run_program(displaytext_4)
        cozmo.run_program(displaytext_5)
        return

    def expression_words(self: cozmo.robot.Robot): #word example of using past three topics
        cozmo.run_program(expression_words)
        cozmo.run_program(displaytext_6)
        return
        
    
    def algebraic_equations(self):
        cozmo.run_program(algebraic_equations)
        cozmo.run_program(displaytext_7)
        cozmo.run_program(displaytext_8)
        return

#---------------------------------------------

class Algebra1(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 1 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""

class Algebra2(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 2 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""

class Algebra3(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 3 = ')        
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Algebra4(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 4 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Algebra5(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 5 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""

class Algebra6(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 6 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Algebra7(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 7 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Algebra8(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 8 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Algebra9(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 9 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Algebra10(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 10 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

#---------------------------------------------
#----------------------TRIG AND PYTHAG--------------------------

class TrigTutorial(Screen):

    def triangleSides(self):
        cozmo.run_program(triangleSide)
        cozmo.run_program(get_in_position)
        cozmo.run_program(displayHOA)
        return
    
    def trigonometricratios(self):
        cozmo.run_program(trigratio)
        return

    def soh(self):
        cozmo.run_program(displaysin)
        return

    def cah(self):
        cozmo.run_program(displaycos)
        return

    def toa(self):
        cozmo.run_program(displaytan)
        return

#---------------------------------------------

class Trig1(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 1 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""

class Trig2(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 2 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""

class Trig3(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 3 = ')        
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Trig4(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 4 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Trig5(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 5 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""

class Trig6(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 6 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Trig7(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 7 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Trig8(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 8 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Trig9(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 9 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Trig10(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 10 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

#---------------------------------------------
#--------------------------GEOMETRY------------------------------

class GeometryTutorial(Screen):
    
    def angletut(self):
        cozmo.run_program(angleTut)
        return

    def shape(self):
        cozmo.run_program(shapes)
        return

    def area(self):
        cozmo.run_program(areatut)
        return

    def perimetertut(self):
        cozmo.run_program(perimeter)
        return

    def volume(self):
        cozmo.run_program(volumetut)
        return

    def pythag(self):
        cozmo.run_program(pythagoras)
        return

#---------------------------------------------

class Geometry1(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 1 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""

class Geometry2(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 2 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""

class Geometry3(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 3 = ')        
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Geometry4(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 4 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Geometry5(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 5 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""

class Geometry6(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 6 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Geometry7(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 7 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Geometry8(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 8 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Geometry9(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 9 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        

class Geometry10(Screen):
    answer = ObjectProperty(None)

    def submit(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n Answer 10 = ')
        appendFile.write(self.answer.text)
        appendFile.close()
        self.reset()
        
    def reset(self):
        self.answer.text = ""        
  
#---------------------------------------------
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





