
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.dashboard_screen import DashBoardScreen
from screens.login_screen import LoginScreen
from kivy.storage.jsonstore import JsonStore
import jwt 
from datetime import datetime, timezone

class OpportunityApp(App):
    access_token = ''
    screen_manager = ScreenManager()
    api_address= 'http://23.88.137.75'
    user_storage = JsonStore('credentials.json')

    def build(self):
        self.screen_manager.add_widget(LoginScreen(name='login'))
        self.screen_manager.add_widget(DashBoardScreen(name='dashboard'))
        try:
            stored_access_token = self.user_storage.get('credentials')['access_token']
            if stored_access_token:
                exp_timestamp  = jwt.decode(stored_access_token, options={"verify_signature": False})['exp']
                exp_time = datetime.fromtimestamp(exp_timestamp, timezone.utc)
                now = datetime.now(timezone.utc)
                if now > exp_time:
                    self.screen_manager.current = 'login'
                else:
                    self.access_token = stored_access_token
                    self.screen_manager.current = 'dashboard'
        except:
            pass
        return self.screen_manager

if __name__ == '__main__':
    OpportunityApp().run()