from __future__ import annotations

from dataclasses import dataclass

from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


@dataclass(frozen=True)
class Palette:
    background: tuple
    surface: tuple
    surface_alternate: tuple
    surface_muted: tuple
    text: tuple
    text_on_surface: tuple
    shadow: tuple
    button_radius: float
    field_radius: float
    button_height: float
    spacing: float
    field_padding: list
    button_font_size: float
    input_font_size: float
    output_font_size: float


DARK_PALETTE = Palette(
    background=(0.12, 0.12, 0.13, 1.0),
    surface=(0.18, 0.18, 0.19, 1.0),
    surface_alternate=(0.22, 0.22, 0.24, 1.0),
    surface_muted=(0.42, 0.42, 0.45, 1.0),
    text=(0.94, 0.94, 0.96, 1.0),
    text_on_surface=(0.99, 0.99, 0.99, 1.0),
    shadow=(0.0, 0.0, 0.0, 0.24),
    button_radius=dp(16),
    field_radius=dp(18),
    button_height=dp(56),
    spacing=dp(12),
    field_padding=[dp(16), dp(14), dp(16), dp(14)],
    button_font_size=dp(16),
    input_font_size=dp(20),
    output_font_size=dp(18),
)

LIGHT_PALETTE = Palette(
    background=(0.96, 0.96, 0.98, 1.0),
    surface=(1.0, 1.0, 1.0, 1.0),
    surface_alternate=(0.94, 0.94, 0.96, 1.0),
    surface_muted=(0.82, 0.82, 0.85, 1.0),
    text=(0.10, 0.10, 0.12, 1.0),
    text_on_surface=(0.10, 0.10, 0.12, 1.0),
    shadow=(0.0, 0.0, 0.0, 0.12),
    button_radius=dp(16),
    field_radius=dp(16),
    button_height=dp(56),
    spacing=dp(10),
    field_padding=[dp(16), dp(12), dp(16), dp(12)],
    button_font_size=dp(16),
    input_font_size=dp(20),
    output_font_size=dp(18),
)


class ThemeManager:
    current_mode = 'dark'
    palettes = {'dark': DARK_PALETTE, 'light': LIGHT_PALETTE}

    @classmethod
    def current(cls):
        return cls.palettes[cls.current_mode]

    @classmethod
    def set_mode(cls, mode: str):
        if mode not in cls.palettes:
            raise ValueError(f'Unsupported theme mode: {mode}')
        cls.current_mode = mode


class MaterialTheme:
    @staticmethod
    def current():
        return ThemeManager.current()

    @staticmethod
    def background():
        return MaterialTheme.current().background

    @staticmethod
    def surface():
        return MaterialTheme.current().surface

    @staticmethod
    def surface_alternate():
        return MaterialTheme.current().surface_alternate

    @staticmethod
    def surface_muted():
        return MaterialTheme.current().surface_muted

    @staticmethod
    def text():
        return MaterialTheme.current().text

    @staticmethod
    def text_on_surface():
        return MaterialTheme.current().text_on_surface

    @staticmethod
    def shadow():
        return MaterialTheme.current().shadow

    @staticmethod
    def button_radius():
        return MaterialTheme.current().button_radius

    @staticmethod
    def field_radius():
        return MaterialTheme.current().field_radius

    @staticmethod
    def button_height():
        return MaterialTheme.current().button_height

    @staticmethod
    def spacing():
        return MaterialTheme.current().spacing

    @staticmethod
    def field_padding():
        return MaterialTheme.current().field_padding

    @staticmethod
    def button_font_size():
        return MaterialTheme.current().button_font_size

    @staticmethod
    def input_font_size():
        return MaterialTheme.current().input_font_size

    @staticmethod
    def output_font_size():
        return MaterialTheme.current().output_font_size


class MaterialButton(Button):
    def __init__(self, theme_color=None, **kwargs):
        self.theme_color = theme_color or MaterialTheme.surface_muted()
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.border = (0, 0, 0, 0)
        self.text_size = self.size
        self.halign = 'center'
        self.valign = 'middle'
        self.bind(size=self._update_canvas, pos=self._update_canvas)
        self._update_canvas()

    def _update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*MaterialTheme.shadow())
            RoundedRectangle(
                size=(self.width, self.height),
                pos=(self.x, self.y - dp(2)),
                radius=[MaterialTheme.button_radius()],
            )
            Color(*self.theme_color)
            RoundedRectangle(
                size=self.size,
                pos=self.pos,
                radius=[MaterialTheme.button_radius()],
            )
        self.color = MaterialTheme.text_on_surface()


class MaterialTextInput(TextInput):
    def __init__(self, fill_color=None, **kwargs):
        self.fill_color = fill_color or MaterialTheme.surface()
        super().__init__(**kwargs)
        self.border = (0, 0, 0, 0)
        self.padding = MaterialTheme.field_padding()
        self.bind(size=self._update_canvas, pos=self._update_canvas)
        self._update_canvas()

    def _update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.fill_color)
            RoundedRectangle(
                size=self.size,
                pos=self.pos,
                radius=[MaterialTheme.field_radius()],
            )
