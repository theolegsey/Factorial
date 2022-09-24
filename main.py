from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 320)
Config.set('graphics', 'height', 500)
fsb = 40

class FactorialCalcApp(App):

    def factorial_oper(self, instance):
        num = 1
        count = 1
        x = 0
        while True:
            num = num * count
            count += 1
            x += 1
            if str(x) == self.lbl.text:
                break
        self.formula = str(num)
        print(x, num, self.lbl.text)
        self.update_label()
        self.formula = ""

    def update_label(self):
        self.lbl.text = self.formula
    def add_number(self, instance):
        self.formula += str(instance.text)
        if str(instance.text) == "C":
            self.formula = ""
        self.update_label()
    def add_operation(self, instance):
        if self.formula == "":
            self.formula =""
        else:
            self.formula += str(instance.text)
        self.update_label()
    def calc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = ""

    def build(self):
        self.formula = ""
        gl = GridLayout(cols = 4, spacing = 1, size_hint = (1, .75))
        bl = BoxLayout(orientation = 'vertical')
        self.lbl = Label(text = "", font_size = 50, valign = 'center', halign = 'right',size_hint = (1, .25), text_size = (320, 500*0.25))
        bl.add_widget(self.lbl)
        gl.add_widget(Button(text = "7", font_size =fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text = "8", font_size =fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text = "9", font_size =fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text="!", font_size =fsb, on_press = self.factorial_oper, background_color = (.25,.95,.0, 1)))

        gl.add_widget(Button(text="4", font_size =fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text="5", font_size =fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text="6", font_size =fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text="-", font_size =fsb, on_press = self.add_operation, background_color = (.25,.95,.0, 1)))

        gl.add_widget(Button(text="1", font_size =fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text="2", font_size =fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text="3", font_size =fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text="+", font_size =fsb, on_press = self.add_operation, background_color = (.25,.95,.0, 1)))

        gl.add_widget(Button(text=".", font_size =fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text="0", font_size =fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text="=", font_size =fsb, on_press = self.calc_result, background_color = (.25,.95,.0, 1)))
        gl.add_widget(Button(text="C", font_size=fsb, on_press = self.add_number, background_color = (.25,.95,.0, 1)))

        bl.add_widget(gl)
        return bl



if __name__ == "__main__":
    FactorialCalcApp().run()