from data.character_maps import KEYBOARD_MAPS


def test_map_entries_exist():
    assert "UKR_TO_ENG" in KEYBOARD_MAPS


def test_src_target_lengths():
    for mode, mapping in KEYBOARD_MAPS.items():
        assert len(mapping["src"]) == len(mapping["target"]) , f"Lengths differ for {mode}"
