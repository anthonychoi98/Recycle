import json
import requests
from kivy.app import App

class MyFirebase():

    wapik = "AIzaSyBvGJKPt0u1NGMku6SqBQwKCcD87QSG23w" #web API key
    refresh_token_file = "refresh_token.txt"

    def sign_up(self, email, password):
        #firebase returns localID,authID,and a refreshToken
        app = App.get_running_app()
        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyBvGJKPt0u1NGMku6SqBQwKCcD87QSG23w"

        signup_payload = {"email": email,
                        "password":password,
                        "returnsecureToken": True,
                        }

        signup_request = requests.post(url=signup_url, data=signup_payload)
        print(signup_request.ok)
        print(signup_request.content.decode())
        sign_up_data = json.loads(signup_request.content.decode())

        if signup_request.ok == True:
            error_message = "Success!"
            App.get_running_app().root.ids['signup'].ids['signin_message'].text = error_message
            refresh_token = sign_up_data['refreshToken']
            localId = sign_up_data['localId']
            idToken = sign_up_data['idToken']
            print("created account!")

            with open("refresh_token.txt", "w") as f:
                f.write(refresh_token)

            app.local_id = localId
            app.id_token = idToken

            my_payload = '{"nickname": "something", "avatar": "image0.jpg", "status": "Horseman", "recycled": "0", "total_recycled": "0", "smallBottles": "0", "bigBottles": "0", "csmallBottles": "0", "cbigBottles": "0"}'
            post_request = requests.patch("https://recyclingapp-44e68.firebaseio.com/" + localId + ".json?auth=" + idToken,
            data=my_payload)
            print(post_request.ok)
            print(json.loads(post_request.content.decode()))

            app.root.current = "name_screen"


        if signup_request.ok == False:
            error_data = json.loads(signup_request.content.decode())
            error_message = error_data["error"]["message"]
            print(error_message)
            app.root.ids['signup'].ids['signin_message'].text = error_message
        pass

    def exchange_refresh_token(self, refresh_Token):
        print("hello/")
        refresh_url = "https://securetoken.googleapis.com/v1/token?key=AIzaSyBvGJKPt0u1NGMku6SqBQwKCcD87QSG23w"
        refresh_payload = '{"grant_type": "refresh_token", "refresh_token": "%s"}'% refresh_Token
        refresh_req = requests.post(refresh_url, data=refresh_payload)

        id_token = refresh_req.json()['id_token']
        local_id = refresh_req.json()['user_id']

        return id_token, local_id


    def sign_in(self, email, password):
        signin_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + self.wapik
        signin_payload = {"email": email, "password": password, "returnSecureToken": True}
        signin_request = requests.post(signin_url, data=signin_payload)
        sign_up_data = json.loads(signin_request.content.decode())
        app = App.get_running_app()

        if signin_request.ok == False:
            error_message = sign_up_data["error"]["message"]
            print(error_message)
            app.root.ids['login_screen'].ids['login_message'].text = error_message

        if signin_request.ok == True:
            print("alright alright alright alright alright ok")
            refresh_token = sign_up_data['refreshToken']
            localId = sign_up_data['localId']
            idToken = sign_up_data['idToken']
            # Save refreshToken to a file
            with open(app.refresh_token_file, "w") as f:
                f.write(refresh_token)

            # Save localId to a variable in main app class
            # Save idToken to a variable in main app class
            app.local_id = localId
            app.id_token = idToken

            result = requests.get('https://recyclingapp-44e68.firebaseio.com/' + app.local_id + '.json?auth=' + app.id_token)
            data = json.loads(result.content.decode())
            cM = data["recycled"]
            nname = data["nickname"]
            stat = data["status"]

            app.root.ids["soul_screen"].ids["recycle_label"].text = str(cM)
            app.root.ids["soul_screen"].ids["status"].text = stat
            #app.root.ids["soul_screen"].ids["nickname"].text = nname
            app.on_start()




        #ok
