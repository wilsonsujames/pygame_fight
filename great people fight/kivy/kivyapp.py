import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kivy.require("1.11.1")

class ConnectPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2

        self.add_widget(Label(text="IP:"))
        self.ip=TextInput(multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text="Port:"))
        self.port=TextInput(multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Username:"))
        self.username=TextInput(multiline=False)
        self.add_widget(self.username)

        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())  # just take up the spot.
        self.add_widget(self.join)       

    def join_button(self,instance):
        port=self.port.text
        ip=self.ip.text
        username=self.username.text
        print(f"attempting to join {ip}:{port} as {username}")



class EpicApp(App):
    def build(self):
        return ConnectPage()

if __name__ == "__main__":
    EpicApp().run()
