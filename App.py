from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import DragBehavior

class DragButton(DragBehavior, Button):

    pass

class Menu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text='Menu'))

    pass
class ToolBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text='Toolbox'))

    pass
class HorizontalBox(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        for arg in args:
            self.add_widget(arg)
    pass
class MainArea(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(DragButton(text='New', size_hint=(None,None ),width=60,height=60))

    pass
class StatusBar(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass

class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Menu())
        toolBox = ToolBox()
        mainArea = MainArea()
        self.add_widget(HorizontalBox(toolBox,mainArea))
        self.add_widget(StatusBar(text='Label'))


    pass


class GameEngineApp(App):
    pass




if __name__ == '__main__':
    app = GameEngineApp()
    app.run()