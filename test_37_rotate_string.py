import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_string():
    assert module.rotate_string("python", 2) == "onpyth"


def test_rotate_by_zero():
    assert module.rotate_string("python", 0) == "python"


def test_empty_string():
    assert module.rotate_string("", 2) == ""
