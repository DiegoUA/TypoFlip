import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window

from engines.layout_converter import LayoutConverterEngine

# Configure Kivy window to resize layout above Android soft keyboard
Window.softinput_mode = 'below_target'


class TypoFlipApp(App):
    def build(self):
        self.title = "TypoFlip - Layout Converter"
        self.converter = LayoutConverterEngine()

        # Top padding dp(54) provides clean clearance below status bar/camera notch
        layout = BoxLayout(
            orientation='vertical',
            padding=[dp(12), dp(54), dp(12), dp(12)],
            spacing=dp(10)
        )

        # Input field
        self.input_field = TextInput(
            hint_text="Type or paste Ukrainian text here...",
            multiline=True,
            size_hint_y=0.4
        )
        self.input_field.bind(text=self.on_text_change)

        # Output field
        self.output_field = TextInput(
            hint_text="Converted English layout output...",
            multiline=True,
            readonly=True,
            size_hint_y=0.4
        )

        # Copy button
        self.copy_btn = Button(
            text="Copy to Clipboard",
            markup=True,
            size_hint_y=0.2
        )
        self.copy_btn.bind(on_press=self.copy_to_clipboard)

        # Assemble UI
        layout.add_widget(self.input_field)
        layout.add_widget(self.output_field)
        layout.add_widget(self.copy_btn)

        return layout

    def on_text_change(self, instance, text_value):
        """Triggers live conversion using the layout engine."""
        converted_text = self.converter.convert(text_value, mode="UKR_TO_ENG")
        self.output_field.text = converted_text

        if self.copy_btn.text != "Copy to Clipboard":
            self.copy_btn.text = "Copy to Clipboard"

    def copy_to_clipboard(self, instance):
        """Copies output text to system clipboard."""
        if self.output_field.text:
            Clipboard.copy(self.output_field.text)
            self.copy_btn.markup = True
            
            # Resolve absolute filesystem path for Kivy image markup on Android
            icon_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "assets", "clipboard.png")
            )
            self.copy_btn.text = f"Copied! [size=20sp][image={icon_path}][/size]"
            
            # Reset button text back after 3 seconds
            Clock.schedule_once(self.reset_copy_button, 3)

    def reset_copy_button(self, dt):
        self.copy_btn.text = "Copy to Clipboard"


if __name__ == '__main__':
    TypoFlipApp().run()