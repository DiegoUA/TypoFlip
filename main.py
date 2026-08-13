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
            padding=[dp(12), get_status_bar_height(), dp(12), dp(12)],
            spacing=dp(10)
        )

        # Main text input
        self.input_field = TextInput(
            multiline=True,
            size_hint_y=0.6,
            hint_text="Enter or paste text here",
        )

        # Action bar with buttons
        action_bar = BoxLayout(size_hint_y=None, height=dp(48), spacing=dp(8))
        self.copy_btn = Button(
            text="Copy to Clipboard",
            size_hint_x=None,
            width=dp(140),
            on_press=self.copy_to_clipboard
        )
        clear_btn = Button(
            text="Clear",
            size_hint_x=None,
            width=dp(90),
            on_press=self.clear_input
        )
        action_bar.add_widget(self.copy_btn)
        action_bar.add_widget(clear_btn)

        # Output (read-only)
        self.output_field = TextInput(
            multiline=True,
            readonly=True,
            background_color=(0.95, 0.95, 0.95, 1),
            size_hint_y=0.35,
        )

        # Bind input change to conversion
        self.input_field.bind(text=self._on_text_changed)

        # Assemble UI
        layout.add_widget(self.input_field)
        layout.add_widget(action_bar)
        layout.add_widget(self.output_field)

        return layout

    def _on_text_changed(self, instance, value):
        try:
            self.output_field.text = self.converter.convert(value, mode="UKR_TO_ENG")
        except Exception:
            # Fail-safe: if conversion fails, show original text
            self.output_field.text = value

    def copy_to_clipboard(self, instance):
        text = self.output_field.text or ""
        Clipboard.copy(text)
        # Provide quick feedback
        original = self.copy_btn.text
        self.copy_btn.text = "Copied!"
        Clock.schedule_once(lambda dt: setattr(self.copy_btn, 'text', original), 1.5)

    def clear_input(self, instance):
        """Clears input and output fields."""
        self.input_field.text = ""
        self.output_field.text = ""
        if self.copy_btn.text != "Copy to Clipboard":
            self.copy_btn.text = "Copy to Clipboard"


def get_status_bar_height():
    # Placeholder function for getting status bar height
    return dp(54)


if __name__ == "__main__":
    TypoFlipApp().run()
