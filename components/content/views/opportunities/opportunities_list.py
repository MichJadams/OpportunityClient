from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.graphics import Rectangle, Color


class OpportunitiesList(GridLayout):
    opportunities = []
    opportunity_item_container = ''
    def __init__(self, **kwargs):
        super(OpportunitiesList, self).__init__(**kwargs)
        self.cols = 1
        self.fetch_opportunities()
        

    def on_pre_enter(self, **args):
        self.fetch_opportunities()
        return super().on_pre_enter(*args)

    def print_result(self, request, result):
        self.opportunities = result
        self.add_widget(OpportunityItemContainer())


    def fetch_opportunities(self, **args):
        app= App.get_running_app()
        user_token = app.access_token
        api_address = "{}/opportunities?token={}".format(app.api_address, user_token)
        UrlRequest(api_address, self.print_result, method="GET")

class OpportunityItemContainer(GridLayout):
    def __init__(self, **kwargs):
        super(OpportunityItemContainer, self).__init__(**kwargs)
        self.cols = 2
        self.height = 40
        self.add_widget(Label(text='this is the third opportunity'))
        with self.canvas:
            Color(1, 0, 0, 1)  # Set the color to red
            self.rect = Rectangle(pos=(0,0), size=(4, 30))