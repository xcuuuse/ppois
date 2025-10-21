"""
@file classes.py
@brief Polynomial realisation
@author Yevik A. 421702
@see Polynomial
"""


class Polynomial:
    def __init__(self, degree: int, coefficients: list):
        """
        @brief Constructor
        :param degree: Polynomial degree
        :param coefficients: Polynomial coefficients
        @see Polynomial.degree
        @see Polynomial.coefficients
        @see Polynomial.dictionary
        """
        self.__degree = degree
        self.__coefficients = coefficients
        self.__dictionary = {}
        for index, value in enumerate(self.__coefficients):
            free = self.__degree - index
            if value != 0:
                self.__dictionary[free] = value

    @property
    def degree(self):
        """
        @brief Degree getter
        :return: polynomial degree
        @see Polynomial.coefficients
        @see Polynomial.dictionary
        """
        return self.__degree

    @property
    def dictionary(self):
        """
        @brief Dictionary getter
        :return: operation dictionary
        """
        return self.__dictionary

    @property
    def coefficients(self):
        """
        @brief Coefficients getter
        :return: the list of coefficients
        """
        return self.__coefficients

    def __getitem__(self, degree):
        """
        @brief Get item method
        @details A method that allows to use () operator to get the value of a coefficient
        :param degree: Polynomial element degree
        :return: Polynomial coefficient
        """
        return self.dictionary.get(degree, 0)

    def __call__(self, number):
        """
        @brief Call method
        @details A method that allows to count polynomial value using ()
        :param number: A number to count polynomial value with
        :return: The result of an operation
        """
        result = 0
        for degree, coefficient in self.dictionary.items():
            result += coefficient * (number ** degree)
        return result

    def __add__(self, other):
        """
        @brief Add method
        @details A method that allows using "+" operator on polynomials
        :return: A polynomial sum method
        """
        return Polynomial.__polynomial_operations(self, other, "s")

    def __iadd__(self, other):
        """
        @brief Add and update method
        @details A method that allows using "+=" operator on polynomials
        :return: Updated polynomial
        """
        final = Polynomial.__polynomial_operations(self, other, "s")
        self.__init__(final.degree, final.coefficients)
        return self

    def __sub__(self, other):
        """
        @brief Difference method
        @details A method that allows using "-" operator on polynomials
        :return: A polynomial difference method
        """
        return Polynomial.__polynomial_operations(self, other, "d")

    def __isub__(self, other):
        """
        @brief Subtract and update method
        @details A method that allows using "-=" operator on polynomials
        :return: Updated polynomial
        """
        final = Polynomial.__polynomial_operations(self, other, "d")
        self.__init__(final.degree, final.coefficients)
        return self

    def __mul__(self, other):
        """
        @brief Multiplication method
        @details A method that allows using "*" operator on polynomials
        :return: A polynomial multiplication method
        """
        return Polynomial.__polynomial_multiplication(self, other)

    def __imul__(self, other):
        """
        @brief Multiply and update method
        @details A method that allows using "*=" operator on polynomials
        :return: Updated polynomial
        """
        final = Polynomial.__polynomial_multiplication(self, other)
        self.__init__(final.degree, final.coefficients)
        return final

    def __truediv__(self, other):
        """
        @brief Division method
        @details A method that allows using "/" operator on polynomials
        :return: A polynomial division method
        """
        return Polynomial.__polynomial_division(self, other)

    def __itruediv__(self, other):
        """
        brief Divide and update method
        @details A method that allows using "/=" operator on polynomials
        :return: Updated polynomial
        """
        final = Polynomial.__polynomial_division(self, other)
        self.__init__(final.degree, final.coefficients)
        return final

    def show_polynomial(self):
        """
        @brief A method used to show the polynomial in math form
        :return: A string that represents the polynomial
        @see Polynomial.count_polynomial
        @see Polynomial.polynomial_operations
        """
        final = ""
        for degree, value in self.__dictionary.items():
            if value == 0:
                continue
            final += f"{value}x^{degree} + "
            if degree == 0:
                final = final.replace(f"{value}x^0", f"{value}")
        for old, new in [("1x", "x"), ("-1x", "-x"), ("x^1", "x"), ("+ -", "- ")]:
            final = final.replace(old, new)
        final = final[:-3]
        return final

    @classmethod
    def __polynomial_operations(cls, pol1, pol2, choice):
        """
        @brief A method that allows to make operations sum and difference
        :param pol1: First polynomial
        :param pol2: Second polynomial
        :param choice: Str "s" or "d" depends on operation
        :return: Result of an operation
        @see Polynomial.polynomial_multiplication
        @see Polynomial.polynomial_division
        """
        result = {}
        for degree, value in pol1.dictionary.items():
            result[degree] = value
        for degree, value in pol2.dictionary.items():
            if choice == "s":
                if degree in result.keys():
                    result[degree] += value
                else:
                    result[degree] = value
            if choice == "d":
                if degree in result.keys():
                    result[degree] -= value
                else:
                    result[degree] = -value
        new_degree = max(result.keys())
        new_coefficients = [result.get(i, 0) for i in range(new_degree, -1, -1)]
        final_sum = Polynomial(new_degree, new_coefficients)
        return final_sum

    @classmethod
    def __polynomial_multiplication(cls, pol1, pol2):
        """
        @brief A method that allows to multiply polynomials
        :param pol1: First polynomial
        :param pol2: Second polynomial
        :return: Multiplication
        @see Polynomial.polynomial_operations
        @see Polynomial.polynomial_division
        """
        result = {}
        max_degree = max(pol1.dictionary.keys()) + max(pol2.dictionary.keys())
        for i in range(max_degree, -1, -1):
            result[i] = 0
        for key, value in pol1.dictionary.items():
            for degree, amount in pol2.dictionary.items():
                if (key + degree) in result.keys():
                    result[key + degree] += value * amount
        new_degree = max(result.keys())
        new_coefficients = [result.get(i, 0) for i in range(new_degree, -1, -1)]
        final = Polynomial(new_degree, new_coefficients)
        return final

    @classmethod
    def __polynomial_division(cls, pol1, pol2):
        """
        @brief A method that allows to divide polynomials
        :param pol1: First polynomial
        :param pol2: Second polynomial
        :return: Division
        @see Polynomial.polynomial_operations
        @see Polynomial.polynomial_multiplication
        """
        dividend = pol1.dictionary.copy()
        divisor = pol2.dictionary.copy()
        final = {}
        while dividend and max(dividend.keys()) >= max(divisor.keys()):
            deg_diff = max(dividend.keys()) - max(divisor.keys())
            factor = dividend[max(dividend.keys())] // divisor[max(divisor.keys())]
            final[deg_diff] = factor
            for d, coef in divisor.items():
                power = d + deg_diff
                dividend[power] = dividend.get(power, 0) - coef * factor
                if abs(dividend[power]) < 1e-10:
                    del dividend[power]
        quotient_degree = max(final.keys()) if final else 0
        quotient_coefficients = [final.get(i, 0) for i in range(quotient_degree, -1, -1)]
        return Polynomial(quotient_degree, quotient_coefficients)
