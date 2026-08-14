import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.utils import platform as kivy_platform

from engines.layout_converter import LayoutConverterEngine
from theme import MaterialButton, MaterialTextInput, MaterialTheme, ThemeManager

# Android 16 style: let the system manage safe-area and resize with keyboard.
ThemeManager.set_mode('dark')
Window.softinput_mode = 'resize'
Window.clearcolor = MaterialTheme.background()


def get_status_bar_height(default_dp: float = 12.0):
    """Return status bar height in dp on Android, else return a sane default.

    This uses pyjnius only when running on Android. On desktop and CI the
    function returns default_dp (in dp units) so tests and local runs are
    unaffected.
    """
    from kivy.metrics import dp

    if kivy_platform != 'android':
        return dp(default_dp)

    try:
        # Import jnius lazily to avoid import-time failures on non-Android
        from jnius import autoclass

        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        res = activity.getResources()
        resource_id = res.getIdentifier('status_bar_height', 'dimen', 'android')
        if resource_id > 0:
            status_bar_px = res.getDimensionPixelSize(resource_id)
            # convert px to dp: dp = px / density
            metrics = activity.getResources().getDisplayMetrics()
            density = metrics.density
            return status_bar_px / density
    except Exception:
        # Fall back to a small top padding if anything goes wrong
        return dp(default_dp)



class TypoFlipApp(App):
    def build(self):
        self.title = 'TypoFlip - Layout Converter'
        self.converter = LayoutConverterEngine()

        theme = MaterialTheme.current()
        top_padding = get_status_bar_height(default_dp=12)
        root = BoxLayout(
            orientation='vertical',
            padding=[dp(12), top_padding, dp(12), dp(12)],
            spacing=theme.spacing,
            size_hint=(1, 1),
        )

        self.input_field = MaterialTextInput(
            multiline=True,
            size_hint_y=0.54,
            hint_text='Enter or paste text here',
            font_size=theme.input_font_size,
            foreground_color=theme.text,
            cursor_color=theme.text,
            background_color=(0, 0, 0, 0),
            fill_color=theme.surface,
            halign='left',
        )

        action_bar = BoxLayout(
            size_hint=(0.96, None),
            height=theme.button_height,
            spacing=theme.spacing,
            pos_hint={'center_x': 0.5},
        )

        self.copy_btn = MaterialButton(
            text='Copy to Clipboard',
            size_hint_x=0.5,
            on_press=self.copy_to_clipboard,
            font_size=theme.button_font_size,
            theme_color=theme.surface_muted,
        )
        clear_btn = MaterialButton(
            text='Clear',
            size_hint_x=0.5,
            on_press=self.clear_input,
            font_size=theme.button_font_size,
            theme_color=theme.surface_muted,
        )
        action_bar.add_widget(self.copy_btn)
        action_bar.add_widget(clear_btn)

        self.output_field = MaterialTextInput(
            multiline=True,
            readonly=True,
            size_hint_y=0.30,
            font_size=theme.output_font_size,
            foreground_color=theme.text,
            background_color=(0, 0, 0, 0),
            fill_color=theme.surface_alternate,
            halign='left',
        )

        self.input_field.bind(text=self._on_text_changed)

        root.add_widget(self.input_field)
        root.add_widget(action_bar)
        root.add_widget(self.output_field)

        return root

    def _on_text_changed(self, instance, value):
        try:
            self.output_field.text = self.converter.convert(value, mode='UKR_TO_ENG')
        except Exception:
            self.output_field.text = value

    def copy_to_clipboard(self, instance):
        text = self.output_field.text or ''
        Clipboard.copy(text)
        original = self.copy_btn.text
        self.copy_btn.text = 'Copied!'
        Clock.schedule_once(lambda dt: setattr(self.copy_btn, 'text', original), 1.5)

    def clear_input(self, instance):
        self.input_field.text = ''
        self.output_field.text = ''
        if self.copy_btn.text != 'Copy to Clipboard':
            self.copy_btn.text = 'Copy to Clipboard'


if __name__ == '__main__':
    TypoFlipApp().run()
