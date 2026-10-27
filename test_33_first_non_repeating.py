import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating():
    assert module.first_non_repeating("aabbcde") == "c"


def test_first_character_non_repeating():
    assert module.first_non_repeating("python") == "p"


def test_no_non_repeating_character():
    assert module.first_non_repeating("aabb") is None
