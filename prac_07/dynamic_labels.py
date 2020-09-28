"""
CP1404/CP5632 Practical - Christian Torrisi
Do-from-scratch - Dynamic Kivy Widgets
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """A program to create dynamic labels based on a list of names"""

    def __init__(self, **kwargs):
        """Construct the main app"""
        super().__init__(**kwargs)
        self.names = ['James', 'Jimmy', 'John', 'Jeremy', 'Joseph', 'Jordan', 'Steve', ]

    def build(self):
        """Builds the kivy app from the kv file"""
        self.title = "Dynamic Labels - Names"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name in the list and adds it to the GUI"""
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.labels_box.add_widget(temp_label)


DynamicLabelsApp().run()
