
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.anchorlayout import AnchorLayout

api_address= 'http://23.88.137.75'
class RememberCredentials(GridLayout):
     def __init__(self, **kwargs):
        super(RememberCredentials, self).__init__(**kwargs)
        self.cols =2 
        self.add_widget(Label(text='Remember Credentials?'))
        self.remember_credentials_check = CheckBox()
        self.add_widget(self.remember_credentials_check)

class LoginBox(GridLayout):
    def on_login_press(self,instance):
        app = App.get_running_app()
        login_address = '{0}/login?name={1}&password={2}'.format(app.api_address, self.user_name.text, self.password.text)
        UrlRequest(login_address, self.go_to_dashboard, on_failure=self.on_login_failure, method="GET")

    def on_login_failure(self, request, result):
        self.login_message.text = 'there was an error logging you in, please try again'

    def go_to_dashboard(self, request, result):
        if 'access_token' in result:
            app = App.get_running_app()
            app.access_token = result['access_token']
            if self.remember_credentials.remember_credentials_check.active:
                app.user_storage.put('credentials',access_token=result['access_token'])
            app.screen_manager.transition.direction = 'left'
            self.password.text = ""
            self.user_name.text = ""
            self.remember_credentials.remember_credentials_check.active = False
            app.screen_manager.current = 'dashboard'

    def navigate_to_create_account(self, instance):
        app = App.get_running_app()
        app.screen_manager.transition.direction = 'left'
        app.screen_manager.current = 'create_account'

    def __init__(self, **kwargs):
        super(LoginBox, self).__init__(**kwargs)
        self.cols = 2 
        self.login_message = Label(text="please login")
        self.add_widget(self.login_message)
        self.create_account_btn = Button(text='Create An Account')
        self.create_account_btn.bind(on_press=self.navigate_to_create_account)
        self.add_widget(self.create_account_btn)
        self.add_widget(Label(text='Name:'))
        self.user_name = TextInput(multiline=False, write_tab=False)
        self.user_name.focus = True
        self.add_widget(self.user_name)

        self.add_widget(Label(text='password'))
        self.password = TextInput(multiline=False, password=True, write_tab=False)
        self.add_widget(self.password)

        self.login_button = Button(text='login')
        self.login_button.bind(on_press=self.on_login_press)

        self.add_widget(self.login_button)
        self.remember_credentials = RememberCredentials()
        self.add_widget(self.remember_credentials)

class LoginWrapper(AnchorLayout):
    def __init__(self, **kwargs):
        super(LoginWrapper, self).__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'center'
        self.padding = [100,100]
        self.add_widget(LoginBox())
    
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.add_widget(LoginWrapper())