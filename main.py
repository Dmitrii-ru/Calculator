from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivy.lang import Builder
# 12
Config.set('kivy', 'kyeboard mode', 'systemanddock')

Window.size = (360, 700)

Builder.load_string('''
<MyOneLabel@MDLabel>
    font_size: '25sp'
    haling: 'left'
    valing: 'middle'
    text_size: self.size

<Container>:
    rows: 3
    text_input: text_input
    label_hours: label_hours
    label_minutes: label_minutes
    label_seconds: label_seconds
    label_m_seconds: label_m_seconds
    label_weeks: label_weeks


    AnchorLayout:
        anchor_y : 'top'
        size_hint: 1, 0.15
        padding: 30


        MDTextField:
            text:''
            id: text_input
            font_size: '45sp'
            input_filter: 'int'
            input_type: 'number'
            multiline: False
            hint_text: 'Ввод'

    GridLayout:
        cols:2
        padding: [40, 0, 0, 0]

        BoxLayout:
            orientation: 'vertical'

            MyOneLabel:
                text: 'Часы'

            MyOneLabel:
                text: 'Минуты'

            MyOneLabel:
                text: 'Секунды'

            MyOneLabel:
                text: 'Милисекудны'

            MyOneLabel:
                text: 'Недели'

        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.5 ,1

            MyOneLabel:
                text: '0'
                id: label_hours

            MyOneLabel:
                text: '0'
                id: label_minutes

            MyOneLabel:
                text: '0'
                id: label_seconds

            MyOneLabel:
                text: '0'
                id: label_m_seconds

            MyOneLabel:
                text: '0'
                id: label_weeks
    BoxLayout:
        size_hint: 0.9, 0.15
        padding: [30, 20, 30,20]

        MDRaisedButton:
            text: 'Погнали!'
            fond_size: 'sp'
            on_release:
                root. convert()
''')


class Container(GridLayout):
    def convert(self):
        try:
            number = int(self.text_input.text)
        except Exception:
            number = 0
        self.label_hours.text=str(number*24)
        self.label_minutes.text=str(number*24*60)
        self.label_seconds.text=str(number*24*60*60)
        self.label_m_seconds.text=str(number*24*60*60*60)
        self.label_weeks.text=str('%.2f' % round(number/7,2))

class Ducky(MDApp):
    def __init__(self,**kwargs):
        self.title = 'Calculator'
        self.theme_cls.theme_style = 'Light'
        super().__init__(**kwargs)
    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Container()


if __name__ == '__main__':
    Ducky().run()
