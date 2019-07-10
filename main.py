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

from algebraquestions import *
from geometryquestions import * 
from trigquestions import *
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

    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question1A)
        return

class TrigWindow(Screen):
    def titleSection(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n')
        appendFile.write('\n Trig Answers')
        appendFile.close()    
    pass

    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question1T)
        return

class GeometryWindow(Screen):
    def titleSection(self):

        appendFile = open('answers.txt', 'a')
        appendFile.write('\n')
        appendFile.write('\n Geometry Answers')
        appendFile.close()    
    pass

    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question1G)
        return
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
        self.ids.algebraic_button.background_color = 0,1,0,0.5

    def completed5(self):
        self.ids.expression_words_button.background_color = 0,1,0,0.5

    
        

    def expression_variables(self): #introducing expressions with a variable
        cozmo.run_program(expression_variables)
        cozmo.run_program(get_in_position)
        cozmo.run_program(displaytext_1)
        return

    def combining_liketerms(self):
        cozmo.run_program(combining_liketerms1)
        cozmo.run_program(get_in_position)
        cozmo.run_program(displaytext_2)
        cozmo.run_program(displaytext_3)
        return

    def sub_evaluate(self): #introducing expressions with more than one variable
        cozmo.run_program(sub_evaluate)
        cozmo.run_program(get_in_position)
        cozmo.run_program(displaytext_4)
        cozmo.run_program(displaytext_5)
        return

    def algebraic_equations(self):
        cozmo.run_program(algebraic_equations)
        cozmo.run_program(get_in_position)        
        cozmo.run_program(displaytext_7)
        cozmo.run_program(displaytext_8)
        return

    def expression_words(self: cozmo.robot.Robot): #word example of using past three topics
        cozmo.run_program(expression_words)
        cozmo.run_program(get_in_position)
        cozmo.run_program(displaytext_6)
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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question2A)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question1A)

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

    def question(self):
        cozmo.run_program(get_in_position)    
        cozmo.run_program(question3A)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question2A)

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

    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question4A)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question3A)

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

    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question5A)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question4A)

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

    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question6A)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question5A)

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

    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question7A)
        

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question6A)

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

    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question8A)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question7A)

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

    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question9A)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question8A)

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

    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question10A)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question9A)

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

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question10A)
        
#---------------------------------------------
#----------------------TRIG AND PYTHAG--------------------------

class TrigTutorial(Screen):
    
    def enableButtonRatios(self):
        self.ids.trigratios.disabled = False
    def enableButtonSoh(self):
        self.ids.soh_button.disabled = False
    def enableButtonCah(self):
        self.ids.cah_button.disabled = False
    def enableButtonToa(self):
        self.ids.toa_button.disabled = False

    def completed1(self):
        self.ids.triangledef.background_color = 0,1,0,0.5
        
    def completed2(self):
        self.ids.trigratios.background_color = 0,1,0,0.5

    def completed3(self):
        self.ids.soh_button.background_color = 0,1,0,0.5

    def completed4(self):
        self.ids.cah_button.background_color = 0,1,0,0.5

    def completed5(self):
        self.ids.toa_button.background_color = 0,1,0,0.5


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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question2T)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question1T)

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question3T)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question2T)

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question4T)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question3T)     

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question5T)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question4T)    

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question6T)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question5T)

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question7T)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question6T)      

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question8T)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question7T)        

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question9T)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question8T)     

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question10T)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question9T)       

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

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question10T)   

#---------------------------------------------
#--------------------------GEOMETRY------------------------------

class GeometryTutorial(Screen):
    
    def enableButtonShapes(self):
        self.ids.shapes_button.disabled = False
    def enableButtonArea(self):
        self.ids.area_button.disabled = False
    def enableButtonPerimeter(self):
        self.ids.perimeter_button.disabled = False
    def enableButtonVolume(self):
        self.ids.volume_button.disabled = False    
    def enableButtonPythag(self):
        self.ids.pythag_button.disabled = False    

    def completed1(self):
        self.ids.angles_button.background_color = 0,1,0,0.5
        
    def completed2(self):
        self.ids.shapes_button.background_color = 0,1,0,0.5

    def completed3(self):
        self.ids.area_button.background_color = 0,1,0,0.5

    def completed4(self):
        self.ids.perimeter_button.background_color = 0,1,0,0.5

    def completed5(self):
        self.ids.volume_button.background_color = 0,1,0,0.5
    
    def completed6(self):
        self.ids.pythag_button.background_color = 0,1,0,0.5    
    
    def angletut(self):
        cozmo.run_program(angleTut)
        return

    def shape(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(shapes)
        return

    def area(self):
        cozmo.run_program(get_in_position)    
        cozmo.run_program(areatut)
        return

    def perimetertut(self):
        cozmo.run_program(get_in_position)            
        cozmo.run_program(perimeter)
        return

    def volume(self):
        cozmo.run_program(get_in_position)                    
        cozmo.run_program(volumetut)
        return

    def pythag(self):
        cozmo.run_program(get_in_position)            
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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question2G)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question1G)

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question3G)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question2G)

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question4G)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question3G)     

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question5G)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question4G)    

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question6G)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question5G)

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question7G)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question6G)      

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question8G)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question7G)        

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question9G)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question8G)     

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
    
    def question(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question10G)

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question9G)       

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

    def requestion(self):
        cozmo.run_program(get_in_position)
        cozmo.run_program(question10G)     
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





