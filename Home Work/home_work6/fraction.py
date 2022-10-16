
class Fraction:
    def __init__(self, numarator, numitor):
        self.numa = numarator
        self.numi = numitor

    def __str__(self):
        return f"Numarator is {self.numa} and nimitor is {self.numi}"

    # @staticmethod
    def __add__(self):
        return f"Sum betwen {self.numa} and {self.numi} is = {self.numa + self.numi}"

    # @staticmethod
    def __sub__(self):
        return f"The subtraction result betwen {self.numa} and {self.numi} is = {self.numa - self.numi}"

    def __reversed__(self):
        return f"This is the reversed Fraction {self.numi} and {self.numa}"


my_fraction = Fraction(98, 55)



print(my_fraction.__str__())
print(my_fraction.__add__())
print(my_fraction.__sub__())
print(my_fraction.__reversed__())
