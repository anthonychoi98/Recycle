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
from kivy.properties import StringProperty
import json
import webbrowser
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

class EntryWindow(Screen):
    pass

class Misc(Screen):
    pass

class UndoWindow(Screen):
    pass

class DetailsWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class ImageLabel(Label, Image):
    pass

class P1(FloatLayout):
    pass

class P2(FloatLayout):
    pass

sm = Builder.load_file("my.kv")

LabelBase.register(name="oj", fn_regular="orange juice 2.0.ttf")
LabelBase.register(name="gb", fn_regular="Grenze-SemiBold.ttf")

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

            self.updateDetails()
            #self.root.ids["soul_screen"].ids["nickname"].text = n
            self.root.current="soul_screen"
        except:
            pass

    def opensite(self):
        webbrowser.open('https://www.calrecycle.ca.gov/BevContainer/Consumers/Facts/')
        #print('hello')

    def check_popup(self, title, text):
        show = P2()
        popupWindow = Popup(title=title, content=show, size_hint=(.8,.4))
        popupWindow.open()

    def status_popup(self, title, text):
        #have two different popups, 1 for stats, 1 for making sure if you wanna resetbin
        show = P1()
        popupWindow = Popup(title=title, content=show, size_hint=(.8,.4))
        popupWindow.open()

    def init_status(self, stats):
        self.root.ids["soul_screen"].ids['status'].text = stats

    def check_status(self, cashMoney, stats):
        if(cashMoney > 10.0 and cashMoney < 20.0 and stats != "Lancer"):
            newStatus = "Lancer"
            text = "Your status has updated!"
            self.status_popup(newStatus, text)
            statsPatch = '{"status": "%s"}'% newStatus
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print("Lancer status achieved!")
        if(cashMoney > 20.0 and cashMoney < 40.0 and stats != "Gallant"):
            newStatus = "Gallant"
            text = "Your status has updated!"
            self.status_popup(newStatus, text)
            statsPatch = '{"status": "%s"}'% newStatus
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print("Gallant status achieved!")
        if(cashMoney > 40.0 and cashMoney < 60.0):
            if(stats != "Keeper"):
                newStatus = "Keeper"
                text = "Your status has updated!"
                self.status_popup(newStatus, text)
                statsPatch = '{"status": "%s"}'% newStatus
                requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
                self.root.ids["soul_screen"].ids["status"].text = newStatus
                print("Keeper status achieved!")
        if(cashMoney > 60.0 and cashMoney < 80.0):
            if(stats != "Protector"):
                newStatus = "Protector"
                text = "Your status has updated!"
                self.status_popup(newStatus, text)
                statsPatch = '{"status": "%s"}'% newStatus
                requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
                self.root.ids["soul_screen"].ids["status"].text = newStatus
                print("Protector status achieved!")
        if(cashMoney > 80.0 and cashMoney < 100.0 and stats != "Defender"):
            newStatus = "Defender"
            text = "Your status has updated!"
            self.status_popup(newStatus, text)
            statsPatch = '{"status": "%s"}'% newStatus
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print("Defender status achieved!")
        if(cashMoney > 100.0 and cashMoney < 140.0 and stats != "Warder"):
            print(stats, "this the status")
            newStatus = "Warder"
            text = "Your status has updated!"
            self.status_popup(newStatus, text)
            statsPatch = '{"status": "%s"}'% newStatus
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print(newStatus," status achieved!")
        if(cashMoney > 140.0 and cashMoney < 200.0 and stats != "Guardian"):
            newStatus = "Guardian"
            text = "Your status has updated!"
            self.status_popup(newStatus, text)
            statsPatch = '{"status": "%s"}'% newStatus
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print(newStatus, ", status achieved!")
        if(cashMoney > 200.0 and cashMoney < 300.0 and stats != "Chevaliar"):
            newStatus = "Chevaliar"
            text = "Your status has updated!"
            self.status_popup(newStatus, text)
            statsPatch = '{"status": "%s"}'% newStatus
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print(newStatus, " status achieved!")
        if(cashMoney > 300.0 and cashMoney < 500.0 and stats != "Justiciar"):
            newStatus = "Justiciar"
            statsPatch = '{"status": "%s"}'% newStatus
            #print("before is : ", statsPatch)
            text = "Your status has updated!"
            self.status_popup(newStatus, text)
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print(newStatus, " status achieved!")
        if(cashMoney > 500.0 and stats != "Paladin"):
            newStatus = "Paladin"
            text = "Your status has updated!"
            self.status_popup(newStatus, text)
            statsPatch = '{"status": "%s"}'% newStatus
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=statsPatch)
            self.root.ids["soul_screen"].ids["status"].text = newStatus
            print(newStatus, " status achieved! Congratulations!!")


    def smallCount(self, num):
        result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
        data = json.loads(result.content.decode())
        cash_M = data["recycled"]
        total_recycled = data["total_recycled"]
        print(total_recycled)

        stats = data["status"]
        smallB = data["smallBottles"]
        csmallB = data["csmallBottles"]

        small_B = int(smallB) + int(num)
        csmall_B = int(csmallB) + int(num)
        num = int(num)
        cM = float(cash_M) + (num*1.05)
        t_cM = float(total_recycled) + (num*1.05)

        cashMoney_arg = t_cM

        cashMoneyPatch = '{"recycled": "%s"}'% str(cM)
        t_cashMoneyPatch = '{"total_recycled": "%s"}'% str(t_cM)
        smallB_Patch = '{"smallBottles": "%s"}' % str(small_B)
        csmallB_Patch = '{"csmallBottles": "%s"}' % str(csmall_B)

        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=cashMoneyPatch)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=t_cashMoneyPatch)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=smallB_Patch)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=csmallB_Patch)

        cM = float(cM)
        cM ='${:,.2f}'.format(cM)
        print(cM)
        self.check_status(cashMoney_arg, stats)

        self.updateDetails()

        sHintText = self.root.ids["entry_screen"].ids["small_input"].text
        if(sHintText != ""):
            self.root.ids["entry_screen"].ids["small_input"].text = ''
            self.root.current = "soul_screen"


    def bigCount(self, num):
        result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
        data = json.loads(result.content.decode())
        cash_M = data["recycled"]
        total_recycled = data["total_recycled"]
        stats = data["status"]
        bigB = data["bigBottles"]
        cbigB = data["cbigBottles"]

        #increment # of big bottles, and curr money, total money
        big_B = int(bigB) + int(num)
        cbig_B = int(cbigB) + int(num)
        num = int(num)

        cM = float(cash_M) + (num*9.10)
        t_cM = float(total_recycled) + (num*9.10)

        #check total recycled for leveling
        cashMoney_arg = t_cM

        cashMoneyPatch = '{"recycled": "%s"}'% str(cM)
        t_cashMoneyPatch = '{"total_recycled": "%s"}'% str(t_cM)
        bigB_Patch = '{"bigBottles": "%s"}' % str(big_B)
        cbigB_Patch = '{"cbigBottles": "%s"}' % str(cbig_B)

        #update total money, current bin money, and # of big bottles
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=cashMoneyPatch)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=t_cashMoneyPatch)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=bigB_Patch)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=cbigB_Patch)

        cM = float(cM)
        cM ='${:,.2f}'.format(cM)
        print(cM)

        #check if user has levelled up
        self.check_status(cashMoney_arg, stats)

        #update details_screen
        self.updateDetails()

        #clear entry screen, return home
        bHintText = self.root.ids["entry_screen"].ids["big_input"].text
        if(bHintText != ""):
            self.root.ids["entry_screen"].ids["big_input"].text = ''
            self.root.current = "soul_screen"


    def subSmallCount(self, num):
        result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
        data = json.loads(result.content.decode())
        cash_M = data["recycled"]
        total_recycled = data["total_recycled"]
        print(total_recycled)

        stats = data["status"]
        smallB = data["smallBottles"]
        csmallB = data["csmallBottles"]
        #CHECK IF USER CAN DELETE CERTAIN AMOUNT OF BOTTLES...

        small_B = int(smallB) - int(num)
        csmall_B = int(csmallB) - int(num)
        num = int(num)
        cM = float(cash_M) - (num*1.05)
        t_cM = float(total_recycled) - (num*1.05)

        if(cM < 0):
            print(cM)
            msg = "Invalid Submission"
            self.root.ids["undo_screen"].ids["errormsg"].text = msg

        else:
            cashMoney_arg = t_cM

            cashMoneyPatch = '{"recycled": "%s"}'% str(cM)
            t_cashMoneyPatch = '{"total_recycled": "%s"}'% str(t_cM)
            smallB_Patch = '{"smallBottles": "%s"}' % str(small_B)
            csmallB_Patch = '{"csmallBottles": "%s"}' % str(csmall_B)

            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=cashMoneyPatch)
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=t_cashMoneyPatch)
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=smallB_Patch)
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=csmallB_Patch)

            cM = float(cM)
            cM ='${:,.2f}'.format(cM)
            print(cM)
            self.check_status(cashMoney_arg, stats)
            #updates money/recycling labels
            self.updateDetails()

            sHintText = self.root.ids["undo_screen"].ids["small_input"].text
            if(sHintText != ""):
                self.root.ids["undo_screen"].ids["small_input"].text = ''
                self.root.current = "soul_screen"


    def subBigCount(self, num):
        result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
        data = json.loads(result.content.decode())
        cash_M = data["recycled"]
        total_recycled = data["total_recycled"]
        stats = data["status"]
        bigB = data["bigBottles"]
        cbigB = data["cbigBottles"]

        #increment # of big bottles, and curr money, total money
        big_B = int(bigB) - int(num)
        cbig_B = int(cbigB) - int(num)
        num = int(num)

        cM = float(cash_M) - (num*9.10)
        t_cM = float(total_recycled) - (num*9.10)

        if(cM < 0):
            print(cM)
            msg = "Invalid Submission"
            self.root.ids["undo_screen"].ids["errormsg"].text = msg

        else:
            #check total recycled for leveling
            cashMoney_arg = t_cM

            cashMoneyPatch = '{"recycled": "%s"}'% str(cM)
            t_cashMoneyPatch = '{"total_recycled": "%s"}'% str(t_cM)
            bigB_Patch = '{"bigBottles": "%s"}' % str(big_B)
            cbigB_Patch = '{"cbigBottles": "%s"}' % str(cbig_B)

            #update total money, current bin money, and # of big bottles
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=cashMoneyPatch)
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=t_cashMoneyPatch)
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=bigB_Patch)
            requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=cbigB_Patch)

            cM = float(cM)
            cM ='${:,.2f}'.format(cM)
            print(cM)

            #check and update user status
            self.check_status(cashMoney_arg, stats)

            #update score/money
            self.updateDetails()

            #clear entry screen, return home
            bHintText = self.root.ids["undo_screen"].ids["big_input"].text
            if(bHintText != ""):
                self.root.ids["undo_screen"].ids["big_input"].text = ''
                self.root.current = "soul_screen"


    def resetBin(self):
        res = 0
        binResetPatch = '{"recycled": "%s"}'% str(res)
        c_sb_Patch = '{"csmallBottles": "%s"}' % str(res)
        c_bb_Patch = '{"cbigBottles": "%s"}' % str(res)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=binResetPatch)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=c_sb_Patch)
        requests.patch('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token, data=c_bb_Patch)

        self.root.ids["soul_screen"].ids["recycle_label"].text = str(res)
        self.root.ids["details_screen"].ids["currentsmallBottles"].text = str(res)
        self.root.ids["details_screen"].ids["currentbigBottles"].text = str(res)

        print("resetted")
        pass

    def enterAmount(self, amount):
        pass

    def updateDetails(self):
        result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + self.local_id + '.json?auth=' + self.id_token)
        data = json.loads(result.content.decode())
        sB = data["smallBottles"]
        bB = data["bigBottles"]
        cSB = data["csmallBottles"]
        cBB = data["cbigBottles"]
        totalCash = data["total_recycled"]
        currentCash = data["recycled"]

        totalCash = float(totalCash)
        cM ='${:,.2f}'.format(totalCash)
        #print(cM)
        currentCash = float(currentCash)
        cCM = '${:,.2f}'.format(currentCash)

        self.root.ids["details_screen"].ids["currentsmallBottles"].text = str(cSB)
        self.root.ids["details_screen"].ids["currentbigBottles"].text = str(cBB)
        self.root.ids["details_screen"].ids["currentMoney"].text = str(cCM)
        self.root.ids["details_screen"].ids["smallBottles"].text = str(sB)
        self.root.ids["details_screen"].ids["bigBottles"].text = str(bB)
        self.root.ids["details_screen"].ids["totalMoney"].text = str(cM)
        self.root.ids["soul_screen"].ids["recycle_label"].text = str(cCM)
        self.root.ids["undo_screen"].ids["errormsg"].text = ""
        pass


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
        self.root.ids.details_screen.ids.bigBottles.text=""
        self.root.ids.details_screen.ids.smallBottles.text=""
        self.root.ids.details_screen.ids.totalMoney.text=""
        #self.root.ids.soul_screen.ids.nickname.text=""



recycle = MyApp()
recycle.run()
