import kivy
from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        label = Label(text="Hello, Kivy!")
        layout.add_widget(label)

        button = Button(text="Click Me!")
        button.bind(on_press=lambda instance: self.on_button_click(instance, "Additional Argument", 42))

        return layout
    
    def on_button_click(self, instance, addition_arg, int_arg):
        instance.text = "Button Clicked!"
        print("Additional argument:", additional_arg)
        print("Integer argument:", int_agr)

if __name__ == '__main__':
    MyApp().run()
