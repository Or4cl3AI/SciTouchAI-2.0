```python
import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class TouchScreenApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation="vertical")
        self.input_field = TextInput(multiline=False)
        self.submit_button = Button(text="Submit")
        self.output_display = Label()
        self.main_layout.add_widget(self.input_field)
        self.main_layout.add_widget(self.submit_button)
        self.main_layout.add_widget(self.output_display)
        self.submit_button.bind(on_press=self.process_input)
        return self.main_layout

    def process_input(self, instance):
        user_input = self.input_field.text
        if not user_input:
            self.output_display.text = "inputError"
            return
        try:
            # Assuming the analyzeData function is defined in ai_module.py
            from ai_module import analyzeData
            data_set = analyzeData(user_input)
            self.output_display.text = "outputMessage: " + str(data_set)
        except Exception as e:
            self.output_display.text = "inputError: " + str(e)
        self.input_field.text = ""

if __name__ == "__main__":
    TouchScreenApp().run()
```