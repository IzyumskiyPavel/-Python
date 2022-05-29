def my_func(my_sum):
    my_list = input("Введите числа через пробел (для выхода введите q): ").split()
    for a in range(len(my_list)):
        if my_list[a] != "q":
            my_sum = my_sum + int(my_list[a])
        else:
            break
    print(my_sum)
    if "q" in my_list:
        print(f"Итоговый результат: {my_sum}")
    else:
        my_func(my_sum)

my_func(0)