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


def register_android_insets_listener(on_insets_changed):
    """Attach a live WindowInsets listener on Android so the app can react
    to the *current* system bar sizes (status bar + navigation/gesture bar)
    and to changes in them (rotation, 3-button vs. gesture nav, foldables,
    etc.), instead of reading a static dimension once at startup.

    Android 15+ (which this app targets via android.api = 36) enforces
    edge-to-edge rendering: the app's window is always drawn full-screen
    behind the system bars, whether we ask for it or not. A one-time
    "status_bar_height" dimen lookup with a small hardcoded fallback (the
    old approach) can't account for that, and never updates -- which is
    why content was drawn under the clock/notch and, depending on device,
    under the gesture bar too.

    `on_insets_changed(top_px, bottom_px)` is called on the Kivy thread
    every time the system reports the current inset sizes, in real
    (unscaled) pixels -- Kivy's own coordinate space on Android already
    matches physical pixels, so these values can be used directly as
    widget padding without any dp conversion.

    Uses the plain Android framework View.OnApplyWindowInsetsListener
    (API 21+) with the legacy getSystemWindowInsetTop/Bottom() accessors
    (API 20+, deprecated but still fully functional) rather than the
    AndroidX Insets APIs, so this works without adding an extra AndroidX
    Gradle dependency to the Buildozer/p4a build.
    """
    if kivy_platform != 'android':
        return

    try:
        from jnius import autoclass, PythonJavaClass, java_method

        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        window = activity.getWindow()
        decor_view = window.getDecorView()

        class _InsetsListener(PythonJavaClass):
            __javainterfaces__ = ['android/view/View$OnApplyWindowInsetsListener']
            __javacontext__ = 'app'

            @java_method(
                '(Landroid/view/View;Landroid/view/WindowInsets;)'
                'Landroid/view/WindowInsets;'
            )
            def onApplyWindowInsets(self, view, insets):
                top_px = insets.getSystemWindowInsetTop()
                bottom_px = insets.getSystemWindowInsetBottom()
                Clock.schedule_once(
                    lambda dt: on_insets_changed(top_px, bottom_px)
                )
                return insets

        listener = _InsetsListener()
        decor_view.setOnApplyWindowInsetsListener(listener)
        # Keep a strong reference on the activity -- pyjnius listener
        # objects get garbage-collected (and silently stop firing) if
        # nothing on the Java side holds onto them.
        activity._typoflip_insets_listener = listener
        decor_view.requestApplyInsets()
    except Exception:
        # Never let a missing API / OEM quirk crash startup; the app just
        # keeps its default padding in that case.
        pass



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

        register_android_insets_listener(self._apply_system_insets)

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
