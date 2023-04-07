from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class StatisticsGrid(GridLayout):
    def __init__(self, **kwargs):
        super(StatisticsGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='this is the statistics grid'))