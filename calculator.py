from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivy.lang import Builder

Builder.load_string('''

<MyOneLabel@Button>:
    font_size: 32
    background_color: (250.0, 0.0, 0.0, 1.0)
  
<Container>:
    id: calculator
    display: entry
    rows: 6

 
    BoxLayout:
        TextInput:
            id: entry
            font_size: 32
            multiline: False
  
    BoxLayout:
        MyOneLabel:
            text: "7"
            on_press: entry.text += self.text
        MyOneLabel:
            text: "8"
            on_press: entry.text += self.text
        MyOneLabel:
            text: "9"
            on_press: entry.text += self.text
        MyOneLabel:
            text: "+"
            on_press: entry.text += self.text
  
    BoxLayout:
        MyOneLabel:
            text: "4"
            on_press: entry.text += self.text
        MyOneLabel:
            text: "5"
            on_press: entry.text += self.text
        MyOneLabel:
            text: "6"
            on_press: entry.text += self.text
        MyOneLabel:
            text: "-"
            on_press: entry.text += self.text
  
    BoxLayout:
        MyOneLabel:
            text: "1"
            on_press: entry.text += self.text
        MyOneLabel:
            text: "2"
            on_press: entry.text += self.text
        MyOneLabel:
            text: "3"
            on_press: entry.text += self.text
        MyOneLabel:
            text: "*"
            on_press: entry.text += self.text

    BoxLayout:
        MyOneLabel:
            text: "AC"
            on_press: entry.text = ""
        MyOneLabel:
            text: "0"
            on_press: entry.text += self.text
        MyOneLabel:
            text: "."
            on_press: entry.text += self.text             
        MyOneLabel:
            text: "/"
            on_press: entry.text += self.text
 
    BoxLayout: 
        MyOneLabel:
            text: "<-"
            on_press: entry.text = entry.text[:-1]  
        MyOneLabel:
            text: "="
            on_press: calculator.calculate(entry.text)
        
''')






class Container(GridLayout):
    def calculate(self,cal):
        if cal:
            try:
                self.display.text=str(eval(cal))
            except Exception:
                self.display.text='Ошибка'


class СalculatorApp(MDApp):
    def __init__(self,**kwargs):
        self.title = 'Time'

        super().__init__(**kwargs)
    def build(self):
        Window.size = (450, 300)
        self.theme_cls.theme_style = 'Light'
        return Container()

if __name__ == '__main__':
    СalculatorApp().run()