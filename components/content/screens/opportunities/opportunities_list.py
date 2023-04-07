from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class OpportunitiesList(GridLayout):
    def __init__(self, **kwargs):
        super(OpportunitiesList, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='this is the first opportunity'))
        self.add_widget(Label(text='this is the second opportunity'))
        self.add_widget(Label(text='this is the third opportunity'))