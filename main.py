from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock

from engines.layout_converter import LayoutConverterEngine

class TypoFlipApp(App):
    def build(self):
        self.title = "TypoFlip - Layout Converter"
        self.converter = LayoutConverterEngine()

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input field
        self.input_field = TextInput(
            hint_text="Type or paste Ukrainian text here...",
            multiline=True
        )
        self.input_field.bind(text=self.on_text_change)

        # Output field
        self.output_field = TextInput(
            hint_text="Converted English layout output...",
            multiline=True,
            readonly=True
        )

        # Copy button
        self.copy_btn = Button(
            text="Copy to Clipboard",
            markup=True,  # Enables Kivy BBCode-style color tags
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
            # Kivy button text logic on copy
            self.copy_btn.markup = True
            self.copy_btn.text = "Copied! [size=20sp][image=assets/clipboard.png][/size]"
            # Reset button text back after 3 seconds
            Clock.schedule_once(self.reset_copy_button, 3)

    def reset_copy_button(self, dt):
        self.copy_btn.text = "Copy to Clipboard"

if __name__ == '__main__':
    TypoFlipApp().run()