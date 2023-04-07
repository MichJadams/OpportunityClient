from kivy.uix.screenmanager import Screen
from components.content.screens.opportunities.opportunities_list import OpportunitiesList
from components.content.screens.statistics.statistics_grid import StatisticsGrid

class StatisticsScreen(Screen):
    def __init__(self, **kwargs):
        super(StatisticsScreen, self).__init__(**kwargs)
        self.add_widget(StatisticsGrid())

class OpportunitiesScreen(Screen):
    def __init__(self, **kwargs):
        super(OpportunitiesScreen, self).__init__(**kwargs)
        self.add_widget(OpportunitiesList())
