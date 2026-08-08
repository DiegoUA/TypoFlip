from data.character_maps import KEYBOARD_MAPS

class LayoutConverterEngine:
    def __init__(self):
        self._translation_tables = {}
        self._build_tables()

    def _build_tables(self):
        """Pre-computes maketrans tables for instant runtime performance."""
        for mode, mapping in KEYBOARD_MAPS.items():
            src = mapping["src"]
            target = mapping["target"]
            self._translation_tables[mode] = str.maketrans(src, target)

    def convert(self, text: str, mode: str = "UKR_TO_ENG") -> str:
        """Converts string layout based on selected language mode."""
        if not text:
            return ""
        table = self._translation_tables.get(mode)
        if table:
            return text.translate(table)
        return text