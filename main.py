import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window

# Configure Kivy window to resize layout above Android soft keyboard
Window.softinput_mode = 'below_target'


class TypoFlipApp(App):
    def build(self):
        self.title = "TypoFlip - Layout Converter"
        self.converter = LayoutConverterEngine()

        # Top padding dp(54) provides clean clearance below status bar/camera notch
        layout = BoxLayout(
            orientation='vertical',
            padding=[dp(12), 0, dp(12), dp(12)],
            spacing=dp(10)
        )

        # Central action bar
        action_bar = BoxLayout(size_hint_y=0.45, height=dp(48))
        self.copy_btn = Button(
            text="Copy to Clipboard",
            size_hint_x=None,
            width=dp(120),
            on_press=self.copy_to_clipboard
        )
        clear_btn = Button(
            text="Clear Input",
            size_hint_x=None,
            width=dp(120),
            on_press=self.clear_input
        )

        action_bar.add_widget(self.input_field)
        action_bar.add_widget(action_bar)
        action_bar.add_widget(self.output_field)

        # Assemble UI
        layout.add_widget(action_bar)

        return layout

    def clear_input(self, instance):
        """Clears input and output fields."""
        self.input_field.text = ""
        self.output_field.text = ""
        if self.copy_btn.text != "Copy to Clipboard":
            self.copy_btn.text = "Copy to Clipboard"
