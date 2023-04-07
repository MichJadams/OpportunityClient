from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.stacklayout import StackLayout

import jwt
api_address= 'http://23.88.137.75'

class LoginButton(Button):
    def __init__(self, **kwargs):
        super(LoginButton, self).__init__(**kwargs)
        self.text = "login"

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
        self.user_name = TextInput(multiline=False)
        self.add_widget(self.user_name)

        self.add_widget(Label(text='password'))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.login_button = LoginButton()
        self.login_button.bind(on_press=self.on_login_press)

        self.add_widget(self.login_button)

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.add_widget(LoginBox())


# ---------------main content------------
class OpportunitiesList(GridLayout):
    def __init__(self, **kwargs):
        super(OpportunitiesList, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='this is the first opportunity'))
        self.add_widget(Label(text='this is the second opportunity'))
        self.add_widget(Label(text='this is the third opportunity'))


class StatisticsGrid(GridLayout):
    def __init__(self, **kwargs):
        super(StatisticsGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='this is the statistics grid'))
    
class OpportunitiesScreen(Screen):
    def __init__(self, **kwargs):
        super(OpportunitiesScreen, self).__init__(**kwargs)
        self.add_widget(OpportunitiesList())

class StatisticsScreen(Screen):
    def __init__(self, **kwargs):
        super(StatisticsScreen, self).__init__(**kwargs)
        self.add_widget(StatisticsGrid())

class NavigationContainer(GridLayout):
    def __init__(self, **kwargs):
        super(NavigationContainer, self).__init__(**kwargs)
        self.cols = 1
        self.width = 50
        self.add_widget(Button(text='Main Dashbaord', height=10))
        self.add_widget(Button(text='Statistics',height=10))

class ContentScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(ContentScreenManager, self).__init__(**kwargs)
        opportunities_screen = OpportunitiesScreen(name='opportunities') 
        statistics_screen = StatisticsScreen(name='statistics')
        self.add_widget(opportunities_screen)
        self.add_widget(statistics_screen)
        self.current = 'opportunities'    

class MainScreenLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreenLayout, self).__init__(**kwargs)
        self.add_widget(NavigationContainer())
        self.add_widget(ContentScreenManager())

class DashBoardScreen(Screen):
    def __init__(self,**kwargs):
        super(DashBoardScreen, self).__init__(**kwargs)
        text = 'Dashboard works!'

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        access_token = app.access_token
        if(len(access_token) > 0):
            decoded_jwt = jwt.decode(access_token, options={"verify_signature": False})
            text = 'you have been logged in!' + decoded_jwt['sub']
            self.add_widget(MainScreenLayout())
        else:
            app.screen_manager.current = 'login'
        # self.add_widget(Label(text=text))
        return super().on_pre_enter(*args)



# --------------------------
class MyApp(App):
    access_token = ''
    screen_manager = ScreenManager()

    def build(self):
        self.screen_manager.add_widget(LoginScreen(name='login'))
        self.screen_manager.add_widget(DashBoardScreen(name='dashboard'))

        return self.screen_manager


if __name__ == '__main__':
    MyApp().run()