import kivy
#kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.core.text import LabelBase

LabelBase.register(name="oj", fn_regular="orange juice 2.0.ttf")

class LoginScreen(BoxLayout):
    pass

#class MyGrid(GridLayout):

    """def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()

        self.inside.cols = 2

        self.inside.add_widget(Label(text = "username:"))
        self.username = TextInput(multiline = False)
        self.inside.add_widget(self.username)

        self.inside.add_widget(Label(text = "password:"))
        self.password = TextInput(password = True)
        self.inside.add_widget(self.password)

        self.add_widget(self.inside)

        self.submit = Button(text = "Submit", font_size = 40)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)


    def pressed(self, instance):
        uname = self.username.text
        passw = self.password.text
        print("username : " + uname +  " pwd : " + passw)
        print ("pressed")
        self.username.text = ""
        self.password.text = ""
"""


class MyApp(App):

    def build(self):
        return LoginScreen()


recycle = MyApp()
recycle.run()
