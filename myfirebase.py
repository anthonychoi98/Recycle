import json
import requests
from kivy.app import App

class MyFirebase():

    wapik = "AIzaSyBvGJKPt0u1NGMku6SqBQwKCcD87QSG23w" #web API key

    #def patch(self, JSON):
        #to_database = json.loads(JSON)
        #requests.patch(url = self.url, json = to_database)

    def sign_up(self, email, password):
        #firebase returns localID,authID,and a refreshToken
        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyBvGJKPt0u1NGMku6SqBQwKCcD87QSG23w"

        signup_data = {"email": email,
                        "password":password,
                        "returnsecureToken": True,
                        }

        signup_request = requests.post(url=signup_url, data=signup_data)
        print(signup_request.ok)
        print(signup_request.content.decode())

        if signup_request.ok == True:
            print("created account!")

        if signup_request.ok == False:
            error_data = json.loads(signup_request.content.decode())
            error_message = error_data["error"]["message"]
            print(error_message)
            App.get_running_app().root.ids['signup'].ids['signin_message'].text = error_message

        pass


    def sign_in(self):
        pass
