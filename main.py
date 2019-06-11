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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
import json
import requests

class HomeWindow(Screen):
    pass

class SoulWindow(Screen):
    pass

class LoginWindow(Screen):
    pass

class SignUpWindow(Screen):
    pass

class NameWindow(Screen):
    pass

class Misc(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class P(FloatLayout):
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

            cashMoney = float(cashMoney)
            cashMoney ='${:,.2f}'.format(cashMoney)
            print(cashMoney)

            status = data['status']
            self.status = status
            n = data['nickname']
            self.username = n
            self.root.ids["soul_screen"].ids["recycle_label"].text = str(cashMoney)
            self.root.ids['soul_screen'].ids['status'].text = status
            #self.root.ids["soul_screen"].ids["nickname"].text = n
            self.root.current="soul_screen"
        except:
            pass

    def status_popup(self, stats):
        show = P()
        txt = "You have been promoted to " + stats
        #self.root.ids["popup_screen"].ids["rank"].text = txt
        popupWindow = Popup(title="Congratulations, you've leveled up!", content=show, size_hint=(.8,.4))
        popupWindow.open()

    def init_status(self, stats):
        self.root.ids["soul_screen"].ids['status'].text = stats

    def check_status(self, cashMoney, stats):
        if(cashMoney > 10.0 and cashMoney < 20.0 and stats != "Lancer"):
            newStatus = "Lancer"
            self.status_popup(newStatus)
            statsPatch = '{"status": "%s"}'% newStatus
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print("Lancer status achieved!")
        if(cashMoney > 20.0 and cashMoney < 40.0 and stats != "Gallant"):
            newStatus = "Gallant"
            self.status_popup(newStatus)
            statsPatch = '{"status": "%s"}'% newStatus
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print("Gallant status achieved!")
        if(cashMoney > 40.0 and cashMoney < 60.0):
            if(stats != "Keeper"):
                newStatus = "Keeper"
                #print("SHOLD BE HERE")
                self.status_popup(newStatus)
                statsPatch = '{"status": "%s"}'% newStatus
                requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
                self.root.ids["soul_screen"].ids["status"].text = newStatus
                print("Keeper status achieved!")
        if(cashMoney > 60.0 and cashMoney < 80.0):
            if(stats != "Protector"):
                newStatus = "Protector"
                self.status_popup(newStatus)
                statsPatch = '{"status": "%s"}'% newStatus
                requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
                self.root.ids["soul_screen"].ids["status"].text = newStatus
                print("Protector status achieved!")
        if(cashMoney > 80.0 and cashMoney < 100.0 and stats != "Defender"):
            newStatus = "Defender"
            self.status_popup(newStatus)
            statsPatch = '{"status": "%s"}'% newStatus
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print("Defender status achieved!")
        if(cashMoney > 100.0 and cashMoney < 140.0 and stats != "Warder"):
            print(stats, "this the status")
            newStatus = "Warder"
            self.status_popup(newStatus)
            statsPatch = '{"status": "%s"}'% newStatus
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print(newStatus," status achieved!")
        if(cashMoney > 140.0 and cashMoney < 200.0 and stats != "Guardian"):
            newStatus = "Guardian"
            self.status_popup(newStatus)
            statsPatch = '{"status": "%s"}'% newStatus
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print(newStatus, ", status achieved!")
        if(cashMoney > 200.0 and cashMoney < 300.0 and stats != "Chevaliar"):
            newStatus = "Chevaliar"
            statsPatch = '{"status": "%s"}'% newStatus
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print(newStatus, " status achieved!")
        if(cashMoney > 300.0 and cashMoney < 500.0 and stats != "Justiciar"):
            newStatus = "Justiciar"
            statsPatch = '{"status": "%s"}'% newStatus
            #print("before is : ", statsPatch)
            self.status_popup(newStatus)
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print(newStatus, " status achieved!")
        if(cashMoney > 500.0 and stats != "Paladin"):
            newStatus = "Paladin"
            statsPatch = '{"status": "%s"}'% newStatus
            self.status_popup(newStatus)
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print(newStatus, " status achieved! Congratulations!!")


    def smallCount(self):
        result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
        data = json.loads(result.content.decode())
        cash_M = data["recycled"]
        stats = data["status"]
        smallB = data["smallBottles"]
        small_B = int(smallB) + 1
        cM = float(cash_M) + 4.05
        cashMoney_arg = cM
        cashMoneyPatch = '{"recycled": "%s"}'% str(cM)
        smallB_Patch = '{"smallBottles": "%s"}' % str(small_B)

        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=cashMoneyPatch)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=smallB_Patch)

        cM = float(cM)
        cM ='${:,.2f}'.format(cM)
        print(cM)
        self.check_status(cashMoney_arg, stats)

        #create check status method...
            #if cM > 10$, update status as Amateur

        self.root.ids["soul_screen"].ids["recycle_label"].text = str(cM)

    def bigCount(self):
        result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
        data = json.loads(result.content.decode())
        cash_M = data["recycled"]
        stats = data["status"]
        bigB = data["bigBottles"]
        big_B = int(bigB) + 1
        cM = float(cash_M) + 9.10
        cashMoney_arg = cM
        cashMoneyPatch = '{"recycled": "%s"}'% str(cM)
        bigB_Patch = '{"bigBottles": "%s"}' % str(big_B)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=cashMoneyPatch)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=bigB_Patch)
        cM = float(cM)
        cM ='${:,.2f}'.format(cM)
        print(cM)

        self.check_status(cashMoney_arg, stats)

        #if cM > 10$, update status as Amateur

        self.root.ids["soul_screen"].ids["recycle_label"].text = str(cM)

    def setNickname(self, u_name):
        they_name = str(u_name)
        print(they_name)
        result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
        data = json.loads(result.content.decode())
        nam = data["nickname"]
        print(nam, " is the current nickname")
        namePatch = '{"nickname": "%s"}'% they_name
        print(namePatch)
        name_req = requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=namePatch)
        #self.root.ids["soul_screen"].ids["nickname"].text = they_name
        print(name_req.ok)
        print(json.loads(name_req.content.decode()))

    def sign_out(self):
        #app = App.get_running_app()

        with open(self.refresh_token_file, 'w') as f:
            f.write("")

        self.root.current="login_screen"

        self.root.ids.login_screen.ids.username.text = ""
        self.root.ids.login_screen.ids.pwd.text = ""
        self.root.ids.soul_screen.ids.recycle_label.text=""
        self.root.ids.soul_screen.ids.status.text=""
        #self.root.ids.soul_screen.ids.nickname.text=""



recycle = MyApp()
recycle.run()
