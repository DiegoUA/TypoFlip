# Keyboard mappings registry

UKR_KEYS = (
    "'1234567890-="
    '₴!"№;%:?*()_+'
    "йцукенгшщзхї\\"
    "ЙЦУКЕНГШЩЗХЇ/"
    "фівапролджє"
    "ФІВАПРОЛДЖЄ"
    "ячсмитьбю."
    "ЯЧСМИТЬБЮ,"
)

ENG_KEYS = (
    "`1234567890-="
    '~!@#$%^&*()_+'
    "qwertyuiop[]\\"
    "QWERTYUIOP{}|"
    "asdfghjkl;'"
    'ASDFGHJKL:"'
    "zxcvbnm,./"
    "ZXCVBNM<>?"
)

KEYBOARD_MAPS = {
    "UKR_TO_ENG": {
        "src": UKR_KEYS,
        "target": ENG_KEYS
    }
}