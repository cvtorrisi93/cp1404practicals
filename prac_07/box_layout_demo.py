"""
CP1404/CP5632 Practical - Christian Torrisi
Walkthrough Example - Box Layout Demo exercise
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """App to greet a name entered into the text field"""
    def build(self):
        """Build the app from the kv file"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Say Hello to the name that is entered into the text field when the button is pressed"""
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_all(self):
        """Clear the label and textbox entries to blank when the button is pressed"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
