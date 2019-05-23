import cozmo
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

def cozmo_program(self: cozmo.robot.Robot):
    self.say_text("Hello and welcome to Cozmo Learning", play_excited_animation=True,voice_pitch=-1).wait_for_completed()

def cozmo_button(self: cozmo.robot.Robot):
    self.say_text("hi").wait

class MainWindow(Screen):
    def on_pre_enter(self):
        Window.size = (608,600)
    def btn(self):
        show_popup()
        cozmo.run_program(cozmo_button)
    
    cozmo.run_program(cozmo_program)


class AlegbraWindow(Screen):
    def on_pre_enter(self):
        Window.size = (900,900)

class TrigPythWindow(Screen):
    def on_pre_enter(self):
        Window.size = (900,900)

class GeometryWindow(Screen):
    def on_pre_enter(self):
        Window.size = (900,900)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        self.title = 'Cozmo Learning App'
        return kv

class P(FloatLayout):
    pass

def show_popup():
    show = P() # Create a new instance of the P class 

    popupWindow = Popup(title="Help", content=show, size_hint=(None,None),size=(400,400)) 
    # Create the popup window

    popupWindow.open() # show the popup




    
if __name__ == "__main__":
    MyMainApp().run()



