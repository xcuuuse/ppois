class Polynomial:
    def __init__(self, degree: int, coefficients: list):
        self.degree = degree
        self.coefficients = coefficients
        self.dictionary = {}
        for index, value in enumerate(self.coefficients):
            free = self.degree - index
            if value != 0:
                self.dictionary[free] = value

    def show_polynomial(self):
        final = ""
        for degree, value in self.dictionary.items():
            if value == 0:
                continue
            final += f"{value}x^{degree} + "
            if degree == 0:
                final = final.replace(f"{value}x^0", f"{value}")
        for old, new in [("1x", "x"), ("-1x", "-x"), ("x^1", "x"), ("+ -", "- ")]:
            final = final.replace(old, new)
        final = final[:-3]
        return final

    def count_polynomial(self, number):
        result = 0
        for key, value in self.dictionary.items():
            result += value * (number ** key)
        return result

    @classmethod
    def polynomial_operations(cls, pol1, pol2, choice):
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
    def polynomial_multiplication(cls, pol1, pol2):
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
    def polynomial_division(cls, pol1, pol2):
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
        quotient = Polynomial(quotient_degree, quotient_coefficients)
        if dividend:
            remainder_degree = max(dividend.keys())
            remainder_coefficients = [dividend.get(i, 0) for i in range(remainder_degree, -1, -1)]
            remainder = Polynomial(remainder_degree, remainder_coefficients)
        else:
            remainder = Polynomial(0, [0])
        return f"{quotient.show_polynomial()}; {remainder.show_polynomial()}"
