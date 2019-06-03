import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from myfirebase import MyFirebase

class MainAppWindow(Screen):
    pass

class LoginWindow(Screen):
    pass

class SignUpWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

sm = Builder.load_file("my.kv")

LabelBase.register(name="oj", fn_regular="orange juice 2.0.ttf")

class MyApp(App):

    def build(self):
        self.my_firebase = MyFirebase
        return sm


recycle = MyApp()
recycle.run()
