if __name__ == '__main__':
    from fraction import Fraction
    my_fraction1 = Fraction(4, 2)
    my_fraction2 = Fraction(2, 2)

    print("my_fraction1", my_fraction1)
    sum_ = my_fraction1 + my_fraction2
    print("sum", sum_)
    sub_ = my_fraction1 - my_fraction2
    print("sub", sub_)
    z = my_fraction1.inverse()
    print("inverse", z)
