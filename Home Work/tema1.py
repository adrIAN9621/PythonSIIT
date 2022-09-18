# 1
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("This is my list>>")
print(my_list)

# 2 Ascendent
my_list1 = sorted(my_list)
print("This is my ascendant list >>")
print(my_list1)

# 3 Reversed
my_list2 = my_list1[:: -1]
print("This is my descendant list >>")
print(my_list2)

# 4 Par
print("This is my even list >>")
print(my_list1[1:len(my_list1):2])

# 5 Impar
print("This is my odd numbers list>>")
print(my_list1[0:len(my_list)-1:2])


# 6 multiple of 3
print("This is my  list >>")
print(my_list1[2:len(my_list1)-1:3])
