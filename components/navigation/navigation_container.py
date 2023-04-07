
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class NavigationContainer(GridLayout):
    def __init__(self, **kwargs):
        super(NavigationContainer, self).__init__(**kwargs)
        self.cols = 1
        self.width = 50
        self.add_widget(Button(text='Main Dashbaord', height=10))
        self.add_widget(Button(text='Statistics',height=10))