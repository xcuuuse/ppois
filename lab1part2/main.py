"""
@file main.py
@brief Program file that is executed
"""

from classes import Polynomial


def check_size(degree: int, coefficients: list):
    return len(coefficients) - degree <= 1


def input_polynomial(name: str):
    while True:
        degree = int(input(f"Enter degree for {name} polynomial: "))
        coefficients = list(map(int, input(f"Enter coefficients for {name} polynomial: ").split()))
        polynomial = Polynomial(degree, coefficients)
        if not check_size(degree, coefficients) or degree <= 0:
            print("Wrong input, try again")
        else:
            return polynomial


def operation(polynomial1: Polynomial, polynomial2: Polynomial, operator: str):
    final = Polynomial
    match operator:
        case "+":
            final = polynomial1 + polynomial2
        case "-":
            final = polynomial1 - polynomial2
        case "*":
            final = polynomial1 * polynomial2
        case "/":
            final = polynomial1 / polynomial2
    return final.show_polynomial()


def i_operation(pol: Polynomial,  operator: str):
    match operator:
        case "+=":
            plus = input_polynomial("added")
            pol += plus
        case "-=":
            minus = input_polynomial("deducted")
            pol -= minus
        case "*=":
            multi = input_polynomial("multiplied")
            pol *= multi
        case "/=":
            div = input_polynomial("divided")
            pol /= div
    return pol


pol1 = input_polynomial("first")
pol2 = input_polynomial("second")
print(f"{pol1.show_polynomial()}\n{pol2.show_polynomial()}")
while True:
    print("1. Get polynomial coefficient\n"
          "2. Count polynomial value\n"
          "3. Polynomial sum\n"
          "4. Polynomial sum(+=)\n"
          "5. Polynomial difference\n"
          "6. Polynomial difference(-=)\n"
          "7. Polynomial multiplication\n"
          "8. Polynomial multiplication(*=)\n"
          "9. Polynomial division\n"
          "10. Polynomial division(/=)\n"
          "11. Exit\n")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            degree1 = int(input("Enter degree (pol1): "))
            degree2 = int(input("Enter degree (pol2): "))
            print(f"pol1[{degree1}] == {pol1[degree1]}")
            print(f"pol2[{degree2}] == {pol2[degree2]}")
        case 2:
            value = int(input("Enter your value: "))
            print(f"first: {pol1(value)}")
            print(f"second: {pol2(value)}")
        case 3:
            print(operation(pol1, pol2, "+"))
        case 4:
            i_operation(pol1, "+=")
            i_operation(pol2, "+=")
            print(pol1.show_polynomial())
            print(pol2.show_polynomial())
        case 5:
            print(operation(pol1, pol2, "-"))
        case 6:
            i_operation(pol1, "-=")
            i_operation(pol2, "-=")
            print(pol1.show_polynomial())
            print(pol2.show_polynomial())
        case 7:
            print(operation(pol1, pol2, "*"))
        case 8:
            i_operation(pol1, "*=")
            i_operation(pol2, "*=")
            print(pol1.show_polynomial())
            print(pol2.show_polynomial())
        case 9:
            print(operation(pol1, pol2, "/"))
        case 10:
            i_operation(pol1, "/=")
            i_operation(pol2, "/=")
            print(pol1.show_polynomial())
            print(pol2.show_polynomial())
        case 11:
            print("Goodbye")
            break
        case _:
            print("Invalid choice, try again")
