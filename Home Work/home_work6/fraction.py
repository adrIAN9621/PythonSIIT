
# ================================================First try============================================================
# class Fraction:
#     def __init__(self, numarator, numitor):
#         self.numa = numarator
#         self.numi = numitor
#
#     def __str__(self):
#         return f"Numarator is {self.numa} and nimitor is {self.numi}"
#
#     # @staticmethod
#     def __add__(self):
#         return f"Sum between {self.numa} and {self.numi} is = {self.numa + self.numi}"
#
#     # @staticmethod
#     def __sub__(self):
#         return f"The subtraction result between {self.numa} and {self.numi} is = {self.numa - self.numi}"
#
#     def __reversed__(self):
#         return f"This is the reversed Fraction {self.numi} and {self.numa}"
#
#
# my_fraction = Fraction(98, 55)
#
#
#
# print(my_fraction.__str__())
# print(my_fraction.__add__())
# print(my_fraction.__sub__())
# print(my_fraction.__reversed__())

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

import math


class Fraction:
    def __init__(self, numerator, denominator):
        try:
            numerator = int(numerator)
        except ValueError:
            raise ValueError('Numerator of a fraction should be an integer.')

        try:
            denominator = int(denominator)
        except ValueError:
            raise ValueError('Denominator of a fraction should be an integer.')

        if denominator == 0:
            raise ValueError('Fraction cannot have denominator equals to 0.')

        self._numerator, self._denominator = self._get_simplified(numerator, denominator)

    @staticmethod
    def _get_simplified(numerator, denominator):
        gcd = math.gcd(numerator, denominator)  # Greatest Common Divisor
        return numerator // gcd, denominator // gcd

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def __add__(self, other):
        lcm = math.lcm(self._denominator, other.denominator)
        first_fraction_numerator = self._numerator * (lcm // self._denominator)
        second_fraction_numerator = other.numerator * (lcm // other.denominator)

        return Fraction(first_fraction_numerator + second_fraction_numerator, lcm)

    def __sub__(self, other):
        lcm = math.lcm(self._denominator, other.denominator)
        first_fraction_numerator = self._numerator * (lcm // self._denominator)
        second_fraction_numerator = other.numerator * (lcm // other.denominator)

        return Fraction(first_fraction_numerator - second_fraction_numerator, lcm)

    def inverse(self):
        return Fraction(self._denominator, self._numerator)

    def __str__(self):
        return f'{self._numerator}/{self._denominator}'
