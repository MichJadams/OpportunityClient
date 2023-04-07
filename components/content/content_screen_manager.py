from kivy.uix.screenmanager import ScreenManager

from components.content.screens.content_screens import OpportunitiesScreen, StatisticsScreen


class ContentScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(ContentScreenManager, self).__init__(**kwargs)
        opportunities_screen = OpportunitiesScreen(name='opportunities') 
        statistics_screen = StatisticsScreen(name='statistics')
        self.add_widget(opportunities_screen)
        self.add_widget(statistics_screen)
        self.current = 'opportunities'    