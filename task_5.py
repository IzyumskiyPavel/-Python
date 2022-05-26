my_list = [7, 5, 3, 3, 2]
num = int(input("Введите число: "))
while num >= 0:
    el = len(my_list)
    for i in range(el):
        if num > my_list[i]:
            el = i
            break
    my_list.insert(el, num)
    print(f"Пользователь ввёл число {num}. Результат: {my_list}")
    num = int(input("Введите число: "))
