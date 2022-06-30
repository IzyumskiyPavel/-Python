def my_func(my_sum):
    my_list = input("Введите числа через пробел (для выхода введите 'q'): ").split()
    for i in range(len(my_list)):
        if my_list[i] != 'q':
            my_sum += int(my_list[i])
        else:
            break
    print(f"Сумма чисел равна {my_sum}")
    if 'q' in my_list:
        print(f"Результат: {my_sum}")
    else:
        my_func(my_sum)

my_func(0)










