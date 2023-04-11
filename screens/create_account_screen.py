from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
import json

class CreateAccount(GridLayout):
    def navigate_to_login_screen(self, instance):
        app = App.get_running_app()
        app.screen_manager.transition.direction = 'right'
        app.screen_manager.current = 'login'


    def create_account(self, instance):
        app = App.get_running_app()
        body = {"name": self.user_name.text, "password": self.password.text}
        login_address = '{0}/create_user'.format(app.api_address)
        body_as_json = json.dumps(body)
        UrlRequest(login_address, 
                   self.created_user_success, 
                   on_failure=self.created_user_error, 
                   req_body=body_as_json, 
                   method="POST")

    def created_user_success(self, request, response):
        self.message.text = 'user created, feel free to go back and login or create another user'
        self.user_name.text = ""
        self.password.text = ""

    def created_user_error(self, request, response):
        self.message.text = 'There was an error creating your account. Please try some other combinations'

    def __init__(self, **kwargs):
        super(CreateAccount, self).__init__(**kwargs)
        self.cols = 2 

        self.back_btn = Button(text='Back')
        self.back_btn.bind(on_press=self.navigate_to_login_screen)
        self.add_widget(self.back_btn)

        self.message = Label(text='here is some information about the app')
        self.add_widget(self.message)

        self.add_widget(Label(text='Name'))
        self.user_name = TextInput(multiline=False, write_tab=False)
        self.user_name.focus = True
        self.add_widget(self.user_name)

        self.add_widget(Label(text='password'))
        self.password = TextInput(multiline=False, password=True, write_tab=False)
        self.add_widget(self.password)

        self.create_account_btn = Button(text='create account')
        self.create_account_btn.bind(on_press=self.create_account)
        self.add_widget(self.create_account_btn)


class CreateAccountScreen(Screen):
    def __init__(self, **kwargs):
        super(CreateAccountScreen, self).__init__(**kwargs)
        self.add_widget(CreateAccount())