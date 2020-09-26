"""
CP1404/CP5632 Practical - Christian Torrisi
Do-from-scratch - Converting Miles to Kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKm(App):
    """ A kivy app that converts miles to kilometres"""

    def build(self):
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesToKm().run()