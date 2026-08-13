from engines.layout_converter import LayoutConverterEngine
from data.character_maps import KEYBOARD_MAPS


def test_build_tables_and_empty():
    engine = LayoutConverterEngine()
    # empty input returns empty string
    assert engine.convert("", mode="UKR_TO_ENG") == ""


def test_keyboard_map_lengths_match():
    for mode, mapping in KEYBOARD_MAPS.items():
        src = mapping["src"]
        tgt = mapping["target"]
        assert len(src) == len(tgt), f"src/target length mismatch for {mode}"


def test_conversion_preserves_length():
    # Use the registered src string for UKR_TO_ENG and ensure conversion returns same length
    mapping = KEYBOARD_MAPS.get("UKR_TO_ENG")
    assert mapping is not None
    src = mapping["src"]
    engine = LayoutConverterEngine()
    out = engine.convert(src, mode="UKR_TO_ENG")
    assert len(out) == len(src)
