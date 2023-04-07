from kivy.uix.screenmanager import Screen
from kivy.app import App
import jwt

from components.main_screen_layout import MainScreenLayout

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
        return super().on_pre_enter(*args)