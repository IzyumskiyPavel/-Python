my_list = input("Введите целые числа через пробел: ").split()
my_list[:-1:2], my_list[1::2] = my_list[1::2], my_list[:-1:2]
print(my_list)