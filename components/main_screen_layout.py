from kivy.uix.boxlayout import BoxLayout
from components.content.content_screen_manager import ContentScreenManager
from components.navigation.navigation_container import NavigationContainer

class MainScreenLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreenLayout, self).__init__(**kwargs)
        self.add_widget(NavigationContainer())
        self.add_widget(ContentScreenManager())