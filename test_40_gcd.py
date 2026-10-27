import importlib

module = importlib.import_module("40_gcd")


def test_gcd_common_numbers():
    assert module.gcd(12, 18) == 6


def test_gcd_prime_numbers():
    assert module.gcd(7, 13) == 1


def test_gcd_with_zero():
    assert module.gcd(10, 0) == 10
