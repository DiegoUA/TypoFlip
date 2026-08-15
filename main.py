import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.utils import platform as kivy_platform

from kivy.logger import Logger

from engines.layout_converter import LayoutConverterEngine
from theme import MaterialButton, MaterialTextInput, MaterialTheme, ThemeManager

# Android 16 style: let the system manage safe-area and resize with keyboard.
ThemeManager.set_mode('dark')
Window.softinput_mode = 'resize'
Window.clearcolor = MaterialTheme.background()


class AndroidInsetsWatcher:
    """Polls the current system-bar insets (status bar + navigation/gesture
    bar) from Kivy's own thread and forwards changes to a callback.

    This deliberately does NOT implement a Java
    View.OnApplyWindowInsetsListener via pyjnius' PythonJavaClass. That
    pattern registers a callback that Android invokes on the Activity's own
    UI thread -- which is a *different* thread than the one running Kivy's
    SDL2 game loop on Android. A JNI up-call landing in the Python
    interpreter from that foreign thread, especially in the middle of a
    touch-driven layout pass (e.g. exactly when the on-screen keyboard
    opens after tapping a text field), is a known source of hard crashes
    in Kivy/python-for-android apps -- which is what was happening here.

    Polling sidesteps that class of bug entirely: every read happens on
    Kivy's own thread via Clock.schedule_interval, so there is no foreign
    -thread callback into the interpreter at all, only a plain getter call.
    """

    POLL_INTERVAL = 0.2

    def __init__(self, on_change):
        self._on_change = on_change
        self._last = (None, None)
        self._decor_view = None

    def start(self):
        if kivy_platform != 'android':
            return
        try:
            from jnius import autoclass

            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = PythonActivity.mActivity
            self._decor_view = activity.getWindow().getDecorView()
        except Exception:
            Logger.exception(
                'TypoFlip: could not obtain the Android decor view; '
                'system-bar padding will stay at its default fallback.'
            )
            return

        # Poll continuously: insets change on rotation, when the gesture/
        # 3-button nav bar toggles, and when the keyboard opens/closes.
        Clock.schedule_interval(self._poll, self.POLL_INTERVAL)
        self._poll(0)  # run once immediately so the first frame is correct

    def _poll(self, dt):
        try:
            insets = self._decor_view.getRootWindowInsets()
            if insets is None:
                return  # not laid out yet -- try again next tick
            top_px = insets.getSystemWindowInsetTop()
            bottom_px = insets.getSystemWindowInsetBottom()
        except Exception:
            Logger.exception('TypoFlip: failed to read window insets')
            return

        if (top_px, bottom_px) != self._last:
            self._last = (top_px, bottom_px)
            self._on_change(top_px, bottom_px)



class TypoFlipApp(App):
    def build(self):
        self.title = 'TypoFlip - Layout Converter'
        self.converter = LayoutConverterEngine()

        theme = MaterialTheme.current()
        self.base_padding = [dp(12), dp(12), dp(12), dp(12)]
        root = BoxLayout(
            orientation='vertical',
            padding=list(self.base_padding),
            spacing=theme.spacing,
            size_hint=(1, 1),
        )
        self.root_layout = root

        self.input_field = MaterialTextInput(
            multiline=True,
            size_hint_y=0.54,
            hint_text='Enter or paste text here',
            font_size=theme.input_font_size,
            foreground_color=theme.text,
            hint_text_color=theme.hint_text,
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

        self._insets_watcher = AndroidInsetsWatcher(self._apply_system_insets)
        self._insets_watcher.start()

        return root

    def _apply_system_insets(self, top_px, bottom_px):
        left, _old_top, right, _old_bottom = self.base_padding
        self.root_layout.padding = [
            left,
            max(left, top_px),
            right,
            max(right, bottom_px),
        ]

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
