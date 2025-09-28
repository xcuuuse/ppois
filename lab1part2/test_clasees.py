"""
@file test_classes.py
@brief Tests for Polynomial class
"""
from classes import Polynomial


def test_polynomial_degree():
    polynomial = Polynomial(3, [1, 2, 3])
    assert polynomial.degree == 3


def test_polynomial_coefficients():
    polynomial = Polynomial(4, [2, 8])
    assert polynomial.coefficients == [2, 8]


def test_polynomial_dictionary():
    polynomial = Polynomial(5, [6, 0, 4, 2])
    assert polynomial.dictionary == {5: 6, 3: 4, 2:2}


def test_call():
    polynomial = Polynomial(4, [3, 2, 1, 3])
    assert polynomial(3) == 315


def test_get_item():
    polynomial = Polynomial(5, [3, 6, 7])
    assert polynomial[4] == 6


def test_sum():
    pol1 = Polynomial(5, [1, 2])
    pol2 = Polynomial(4, [8, 7])
    final = pol1 + pol2
    assert final.dictionary == {5: 1, 4: 10, 3: 7}


def test_sum_equal():
    polynomial = Polynomial(5, [6, 4, 3])
    polynomial += Polynomial(4, [5, 6, 7, 8])
    assert polynomial.dictionary == {5: 6, 4: 9, 3: 9, 2: 7, 1: 8}


def test_difference():
    pol1 = Polynomial(5, [1, 2])
    pol2 = Polynomial(4, [8, 7])
    final = pol1 - pol2
    assert final.dictionary == {5: 1, 4: -6, 3: -7}


def test_difference_equal():
    polynomial = Polynomial(5, [6, 4, 3])
    polynomial -= Polynomial(4, [5, 6, 7, 8])
    assert polynomial.dictionary == {5: 6, 4: -1, 3: -3, 2: -7, 1: -8}


def test_multiplication():
    pol1 = Polynomial(5, [1, 2])
    pol2 = Polynomial(4, [8, 7])
    final = pol1 * pol2
    assert final.dictionary == {9: 8, 8: 23, 7: 14}


def test_multiplication_equal():
    polynomial = Polynomial(5, [6, 4, 3])
    polynomial *= Polynomial(4, [5, 6, 7, 8])
    assert polynomial.dictionary == {9: 30, 8: 56, 7: 81, 6: 94, 5: 53, 4: 24}


def test_division():
    pol1 = Polynomial(2, [1, 2, 1])
    pol2 = Polynomial(1, [1, 1])
    final = pol1 / pol2
    assert final.dictionary == {1: 1, 0: 1}


def test_division_equal():
    polynomial = Polynomial(3, [1, 3, 3, 1])
    polynomial /= Polynomial(1, [1, 1])
    assert polynomial.dictionary == {2: 1, 1: 2, 0: 1}


def test_show():
    polynomial = Polynomial(7, [4, 0, -1, 2, 3])
    assert polynomial.show_polynomial() == "4x^7 - x^5 + 2x^4 + 3x^3"


def test_zero():
    polynomial = Polynomial(0, [5])
    assert polynomial.show_polynomial() == "5"


def test_empty():
    polynomial = Polynomial(3, [])
    assert polynomial.dictionary == {}
    assert polynomial.show_polynomial() == ""


def test_wrong_coefficient():
    polynomial = Polynomial(5, [1, 2])
    assert polynomial[10] == 0


def test_divide_bigger():
    pol1 = Polynomial(2, [1, 2, 1])


def test_invalid_coefficient():
    polynomial = Polynomial(5, [1, 2])
    assert polynomial[-1] == 0


def test_first_degree():
    polynomial = Polynomial(1, [1])
    assert polynomial.show_polynomial() == "x"


def test_first_degree_negative():
    polynomial = Polynomial(1, [-1])
    assert polynomial.show_polynomial() == "-x"


def test_empty_polynomial():
    polynomial = Polynomial(0, [])
    assert polynomial.show_polynomial() == ""

