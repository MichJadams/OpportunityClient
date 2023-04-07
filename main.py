from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.dashboard_screen import DashBoardScreen
from screens.login_screen import LoginScreen

class MyApp(App):
    access_token = ''
    screen_manager = ScreenManager()
    api_address= 'http://23.88.137.75'
    def build(self):
        self.screen_manager.add_widget(LoginScreen(name='login'))
        self.screen_manager.add_widget(DashBoardScreen(name='dashboard'))

        return self.screen_manager


if __name__ == '__main__':
    MyApp().run()