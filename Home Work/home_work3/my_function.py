def my_program():
    number = input("Choose a number >>>")
    try:
        number = int(number)
        print(number)
    except ValueError:
        print("You must enter an int")
        my_program()
        print(number)
    number = str(number)
    if number == str(number[::-1]):
        print("is_palindrome", True)
    else:
        print("is_palindrome", False)

    flag = False
    number = int(number)
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break
    if flag:
        print("is_not_prime ", False)
    else:
        print("is_prime ", True)

    n = int(number)
    my_list = []
    for i in range(1, n + 1):

        if n % i == 0:
            my_list.append(i)
    print("divisor", (my_list[:-1]))
    print("max_div :", my_list[-2])
# def dig():
    count = 0
    n = number
    while n != 0:
        n //= 10
        count += 1
    print("digits", count)
