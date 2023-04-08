
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App

class NavigationContainer(GridLayout):
    def logout(self, instance):
        app = App.get_running_app()
        app.access_token = ""
        app.user_storage.put('credentials', access_token='')
        app.screen_manager.current = 'login'

    def __init__(self, **kwargs):
        super(NavigationContainer, self).__init__(**kwargs)
        self.cols = 1
        self.size_hint=(0.2, 1)
        print(self.col_default_width)
        self.add_widget(Button(text='Main Dashbaord', height=10))
        self.add_widget(Button(text='Statistics',height=10))
        self.logout_button = Button(text='Logout and Clear Credentials', height=10)
        self.logout_button.bind(on_press=self.logout)
        self.add_widget(self.logout_button)