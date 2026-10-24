import string


def is_pangram(text):
    letters = set(text.lower())
    return set(string.ascii_lowercase).issubset(letters)