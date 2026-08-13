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
from jnius import autoclass  # Import autoclass from jnius to resolve the undefined name error

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
            self.copy_btn.text = "Copied!"
            Clock.schedule_once(self.reset_copy_button, 3)

    def reset_copy_button(self, dt):
        self.copy_btn.text = "Copy to Clipboard"

    def clear_input(self, instance):
        """Clears input and output fields."""
        self.input_field.text = ""
        self.output_field.text = ""
        if self.copy_btn.text != "Copy to Clipboard":
            self.copy_btn.text = "Copy to Clipboard"


def get_status_bar_height():
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    activity = PythonActivity.mActivity
    resources = activity.getResources()
    status_bar_height = resources.getDimensionPixelSize(
        resources.getIdentifier("status_bar_height", "dimen", "android")
    )
    return dp(status_bar_height)


if __name__ == '__main__':
    TypoFlipApp().run()
