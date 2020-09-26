"""
CP1404/CP5632 Practical - Christian Torrisi
Do-from-scratch - Converting Miles to Kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

CONVERSION_RATIO = 1.60934


class ConvertMilesToKm(App):
    """ A kivy app that converts miles to kilometres"""
    output_message = StringProperty()

    def build(self):
        """Builds the kivy app from the kv file"""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, miles):
        """Converts miles to kilometres when the button is pressed"""
        try:
            miles = float(miles)
            kilometres = float(miles) * CONVERSION_RATIO
        except ValueError:
            kilometres = 0
        self.output_message = "{:.3f}".format(kilometres)

    def handle_increment(self, value):
        """Increases or decreases the test input value based on the button pressed"""
        if self.root.ids.input_number.text == '':
            self.root.ids.input_number.text = str(0)
        new_value = int(self.root.ids.input_number.text) + value
        self.root.ids.input_number.text = str(new_value)


ConvertMilesToKm().run()
