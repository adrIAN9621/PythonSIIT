# 1 Functie cu parametri nedefiniti
def paran_ned(*args, **kwargs):
    s = 0
    if type(kwargs) == int:
        s += kwargs
    for x in args:
        if type(x) == int or type(x) == float:
            s += x
    return s


print(paran_ned(1, 5, -3, 'abc', [12, 56, 'cad']))
print(paran_ned())
print(paran_ned(2, 4, 'abc', kwargs=2))


# 2 Functie Recursiva


def my_function(n):
    if n == 0:
        return 0

    return n + my_function(n - 1)


# The sum of the numbers from 0 to n


sum_1 = my_function(88)
print("The sum of the numbers from 0 to n is >>")
print(">>", sum_1)


# The sum of even numbers from 0 to n


def my_sum_par(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + my_sum_par(n - 2)
    else:
        return my_sum_par(n - 1) + my_sum_par(n - 3)


# print(my_sum_par(8))


sum_2 = my_sum_par(88)
print("The sum of even numbers from 0 to n is >>")
print(">>", sum_2)


# The sum of odd numbers from 0 to n
def sum_of_inp(n):
    if type(n) == int:
        if n <= 0:
            return 0
        if n % 2 == 1:
            return n + sum_of_inp(n - 2)
        else:
            return sum_of_inp(n - 1)


print("The sum of odd numbers from 0 to n is >>")
print(sum_of_inp(88))

# 3 Input and except function
try:
    number = (int(input("Choose a number <><> @  ")))
    print(number)

except ValueError:
    print(0)
