from kivy.app import App
from kivy.uix.label import Label

class AIApp(App):
    def build(self):
        return Label(text="AI Factory Running 🚀")

AIApp().run()
