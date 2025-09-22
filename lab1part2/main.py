"""
@file main.py
@brief Program file that is executed
"""

from CLASSES import Polynomial


def check_size(degree: int, coefficients: list):
    return len(coefficients) - degree <= 1


def input_polynomial(name: str):
    while True:
        degree = int(input(f"Enter degree for {name} polynomial: "))
        coefficients = list(map(int, input(f"Enter coefficients for {name} polynomial: ").split()))
        pol = Polynomial(degree, coefficients)
        if not check_size(degree, coefficients) or degree <= 0:
            print("Wrong input, try again")
        else:
            return pol


pol1 = input_polynomial("first")
pol2 = input_polynomial("second")
print(f"{pol1.show_polynomial()}\n{pol2.show_polynomial()}")
while True:
    print("1. Count polynomial value\n"
          "2. Polynomial sum\n"
          "3. Polynomial difference\n"
          "4. Polynomial multiplication\n"
          "5. Polynomial division\n"
          "6. Exit\n")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            value = int(input("Enter your value: "))
            print(f"first: {pol1.count_polynomial(value)}")
            print(f"second: {pol2.count_polynomial(value)}")
        case 2:
            pol_sum = Polynomial.polynomial_operations(pol1, pol2, "s")
            print(f"({pol1.show_polynomial()}) + ({pol2.show_polynomial()}) == {pol_sum.show_polynomial()}")
        case 3:
            pol_difference = Polynomial.polynomial_operations(pol1, pol2, "d")
            print(f"({pol1.show_polynomial()}) - ({pol2.show_polynomial()}) == {pol_difference.show_polynomial()}")
        case 4:
            pol_multiplication = Polynomial.polynomial_multiplication(pol1, pol2)
            print(f"({pol1.show_polynomial()}) * ({pol2.show_polynomial()}) == {pol_multiplication.show_polynomial()}")
        case 5:
            pol_division = Polynomial.polynomial_division(pol1, pol2)
            print(f"({pol1.show_polynomial()}) / ({pol2.show_polynomial()}) == {pol_division}")
        case 6:
            print("Goodbye")
            break
        case _:
            print("Invalid choice, try again")
