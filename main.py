from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.label = Label(
            text="Hello! Kivy APK is working 🚀",
            font_size="24sp"
        )

        self.button = Button(
            text="Click Me",
            size_hint=(1, 0.3)
        )

        self.button.bind(on_press=self.on_button_click)

        self.add_widget(self.label)
        self.add_widget(self.button)

    def on_button_click(self, instance):
        self.label.text = "Button Clicked ✅"


class MyKivyApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        return MainLayout()


if __name__ == "__main__":
    MyKivyApp().run()
