"""
@file test_classes.py
@brief Tests for Polynomial class
"""

from CLASSES import Polynomial


def test_create():
    polynomial = Polynomial(3, [1, 2, 3, 4])
    assert polynomial.dictionary == {3: 1, 2: 2, 1: 3, 0: 4}


def test_count():
    polynomial = Polynomial(3, [2, 0, 4, 10])
    assert polynomial.count_polynomial(3) == 76


def test_show():
    polynomial = Polynomial(6, [2, 0, 4, 5, 1])
    assert polynomial.show_polynomial() == "2x^6 + 4x^4 + 5x^3 + x^2"


def test_sum():
    pol1 = Polynomial(3, [1, 0, 3, 10])
    pol2 = Polynomial(6, [1, 0, 1])
    pol_sum = Polynomial.polynomial_operations(pol1, pol2, "s")
    assert pol_sum.show_polynomial() == "x^6 + x^4 + x^3 + 3x + 10"


def test_difference():
    pol1 = Polynomial(3, [1, 0, 3, 10])
    pol2 = Polynomial(6, [1, 0, 1])
    pol_sum = Polynomial.polynomial_operations(pol1, pol2, "d")
    assert pol_sum.show_polynomial() == "-x^6 - x^4 + x^3 + 3x + 10"


def test_multiplication():
    pol1 = Polynomial(3, [1, 2])
    pol2 = Polynomial(5, [1, 4])
    pol_multi = Polynomial.polynomial_multiplication(pol1, pol2)
    assert pol_multi.show_polynomial() == "x^8 + 6x^7 + 8x^6"


def test_division():
    pol1 = Polynomial(2, [1, 2, 3])
    pol2 = Polynomial(1, [1, 1])
    pol_div = Polynomial.polynomial_division(pol1, pol2)
    assert pol_div == "x + 1; 2"
