from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class OpportunitiesList(ScrollView):
    opportunities = []
    opportunity_item_container = ''
    def __init__(self, **kwargs):
        super(OpportunitiesList, self).__init__(**kwargs)
        self.size_hint=(1, None)
        self.size=(Window.width, Window.height)
        self.do_scroll_y = True
        self.do_scroll_x = False 
        self.fetch_opportunities()

    def on_pre_enter(self, **args):
        self.fetch_opportunities()
        return super().on_pre_enter(*args)

    def print_result(self, request, result):
        self.opportunities = result
        self.add_widget(OpportunityItemContainer(opportunities=self.opportunities))

    def fetch_opportunities(self, **args):
        app= App.get_running_app()
        user_token = app.access_token
        api_address = "{}/opportunities?token={}".format(app.api_address, user_token)
        UrlRequest(api_address, self.print_result, method="GET")

class OpportunityItemContainer(BoxLayout):
    def __init__(self, opportunities, **kwargs):
        super(OpportunityItemContainer, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.height= self.minimum_height
        self.opportunities = opportunities
        for o in self.opportunities:
            widget = OpporunityItem(o)
            self.add_widget(widget)
            self.draw_border(widget.pos[0], widget.pos[1], widget.pos[0] + widget.width, widget.pos[0]+ widget.height)


    def draw_border(self, left, bottom, right, top):
        pass 
        with self.canvas.before:
            Color(1, 0, 0, 1)
            # draw the four sides of the border separately
            # left = self.pos[0]
            # bottom = self.pos[1]
            # right = self.pos[0] + self.width
            # top = self.pos[1] + self.height
            # draw the top and bottom sides
            Rectangle(pos=(left, top - 2), size=(self.width, 2))
            # Rectangle(pos=(left, bottom), size=(self.width, 2))

            # Rectangle(pos=(left, bottom), size=(2, self.height))
            # Rectangle(pos=(right - 2, bottom), size=(2, self.height))

class OpporunityItem(GridLayout):
    def __init__(self, opportunity, **kwargs):
        super(OpporunityItem, self).__init__(**kwargs)
        self.opportunity = opportunity
        self.cols = 2
        self.height = 200
        self.width = Window.width
        self.size_hint_y = None
        # self.add_widget(Label(text="---------------------------"))
        # self.add_widget(Label(text="---------------------------"))
        self.add_widget(self.CustomLabel(self.opportunity["title"]))
        self.add_widget(self.CustomLabel(self.opportunity["url"]))
        self.add_widget(self.CustomLabel(self.opportunity["notes"]))
        self.add_widget(self.CustomLabel(self.opportunity["updated_at"] if self.opportunity["updated_at"]!= None else "Not Recorded" ))
        self.add_widget(self.CustomLabel(self.opportunity["role_description"]))
        self.add_widget(self.CustomLabel(self.opportunity["application_status"]))
        with self.canvas.before:
            Color(1, 0, 0, 1)
            # draw the four sides of the border separately
            left = self.pos[0]
            bottom = self.pos[1]
            right = self.pos[0] + self.width
            top = self.pos[1] + self.height
            # draw the top and bottom sides
            Rectangle(pos=(left, top - 2), size=(self.width, 2))
            Rectangle(pos=(left, bottom), size=(self.width, 2))

            Rectangle(pos=(left, bottom), size=(2, self.height))
            Rectangle(pos=(right - 2, bottom), size=(2, self.height))

    # def update_border(self, *args):
        
    def CustomLabel(self, text):
        label = Label(text= text)
        label.text_size = (200, None)
        return label

