import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from myfirebase import MyFirebase
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
import json
import requests

class HomeWindow(Screen):
    pass

class LoginWindow(Screen):
    pass

class SignUpWindow(Screen):
    pass

class NameWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

sm = Builder.load_file("my.kv")

LabelBase.register(name="oj", fn_regular="orange juice 2.0.ttf")

class MyApp(App):
    refresh_token_file = "refresh_token.txt"
    wapik = "AIzaSyBvGJKPt0u1NGMku6SqBQwKCcD87QSG23w"

    def build(self):
        self.my_firebase = MyFirebase()
        return sm

    def on_start(self):
        try:
            with open(self.refresh_token_file, 'r') as f:
                refresh_Token = f.read()
            id_Token, local_Id = self.my_firebase.exchange_refresh_token(refresh_Token)
            self.local_id = local_Id
            self.id_token = id_Token

            result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
            data = json.loads(result.content.decode())

            cashMoney = data['recycled']
            self.cashMoney = cashMoney
            status = data['status']
            self.status = status
            self.root.ids["home_screen"].ids["recycle_label"].text = str(cashMoney)
            self.root.ids['home_screen'].ids['status'].text = status

            self.root.current="home_screen"
        except:
            pass

    def init_status(self, stats):
            self.root.ids["home_screen"].ids['status'].text = stats

    def tinCanCount(self):
        #increment how much tin_cash money they got

        #print(self.local_Id)
        result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
        data = json.loads(result.content.decode())
        cash_M = data["recycled"]
        cM = int(cash_M) + 1
        cashMoneyPatch = '{"recycled": %s}'% str(cM)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=cashMoneyPatch)
        self.root.ids["home_screen"].ids["recycle_label"].text = str(cM)

    def glassBottleCount(self):
        print(self.local_id)
        result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
        data = json.loads(result.content.decode())
        cash_M = data["recycled"]
        cM = int(cash_M) + 2
        cashMoneyPatch = '{"recycled": %s}'% str(cM)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=cashMoneyPatch)
        self.root.ids["home_screen"].ids["recycle_label"].text = str(cM)

    def setNickname(self, u_name):
        they_name = str(u_name)
        print(they_name)
        result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
        data = json.loads(result.content.decode())
        namePatch = '{"nickname": %s}'% they_name
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=namePatch)
        self.root.ids["home_screen"].ids["nickname"].text = they_name

    def sign_out(self):
        #app = App.get_running_app()

        with open(self.refresh_token_file, 'w') as f:
            f.write("")

        self.root.current="login_screen"

        self.root.ids.login_screen.ids.username.text = ""
        self.root.ids.login_screen.ids.pwd.text = ""


recycle = MyApp()
recycle.run()
