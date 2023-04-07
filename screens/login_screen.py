
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button

api_address= 'http://23.88.137.75'

class LoginBox(GridLayout):
    def on_login_press(self,instance):
        print("this is the username", self.user_name.text)
        print("this is the password", self.password.text)
        login_address = '{0}/login?name={1}&password={2}'.format(api_address, self.user_name.text, self.password.text)
        UrlRequest(login_address + '/login', self.print_result, method="GET")

    def print_result(self, request, result):
        print('access_token' in result)
        if 'access_token' in result:
            app = App.get_running_app()
            app.access_token = result['access_token']
            app.screen_manager.current = 'dashboard'

    def __init__(self, **kwargs):
        super(LoginBox, self).__init__(**kwargs)
        self.cols = 2 
        self.add_widget(Label(text='Name:'))
        self.user_name = TextInput(multiline=False, write_tab=False)
        self.user_name.focus = True
        self.add_widget(self.user_name)

        self.add_widget(Label(text='password'))
        self.password = TextInput(multiline=False, password=True, write_tab=False)
        self.add_widget(self.password)

        self.login_button = Button()
        self.login_button.bind(on_press=self.on_login_press)

        self.add_widget(self.login_button)

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.add_widget(LoginBox())