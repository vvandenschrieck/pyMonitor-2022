import os
import threading

os.environ["KIVY_NO_CONSOLELOG"] = "1"
from kivy.app import App
from kivy.clock import mainthread
from kivy.properties import ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class StatusTag(Widget):
    color = ListProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(StatusTag, self).__init__(**kwargs)

    def set_color(self, color):
        self.color = color


class GUIView(App):
    def __init__(self, presenter, **kwargs):
        self.__presenter = presenter
        super(GUIView, self).__init__(**kwargs)

    @mainthread
    def refresh(self):
        """Appelée par le présentateur lorsqu'il faut rafraichir la vue"""
        sites = self.__presenter.sites()
        box = self.root.ids.site_status_box
        box.clear_widgets()
        grid = GridLayout(rows=len(sites), cols=2)
        # Create a Label + Tag for each site
        for site, status in sites.items():
            grid.add_widget(Label(text=site))
            tag = StatusTag()
            if status == 'OK':
                tag.set_color([0, 1, 0, 1])
            grid.add_widget(tag)
        box.add_widget(grid)

        # Clear previous messages
        self.root.ids.msg_label.text = ""

    def test_all(self):
        """Callback lorsque l'utilisateur souhaite retester les sites"""
        # Run in a thread to prevent GUI blocking.
        # DANGER : Not thread-safe!
        x = threading.Thread(target=self.__presenter.test_all)
        x.start()

    def msg(self, msg):
        self.root.ids.msg_label.text = msg

# if __name__ == "__main__":
#     Config.set('graphics', 'width', '600')
#     Config.set('graphics', 'height', '400')
#     GUIView().run()
