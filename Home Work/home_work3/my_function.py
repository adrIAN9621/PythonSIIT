def my_program():
    global number
    number = input("Choose a number >>>")
    try:
        number = int(number)
        return number
    except ValueError:
        print("you must enter an int")
        my_program()
        return number


def pal():
    global number
    number = str(number)
    if str(number) == str(number[::-1]):
        return "is_palindrome", True
    else:
        return "is_palindrome", False


def prime():
    global number
    flag = False
    number = int(number)
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break
    if flag:
        return "is_not_prime ", False
    else:
        return "is_prime ", True


def div():
    global number

    n = int(number)
    my_list = []
    for i in range(1, n + 1):

        if n % i == 0:
            my_list.append(i)

    print("divisor", (my_list[:-1]))
    return "max_div :", my_list[-2]


def dig():
    count = 0
    n = number
    while n != 0:
        n //= 10
        count += 1
    return "digits", count
