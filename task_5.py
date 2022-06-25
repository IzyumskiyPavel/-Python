my_list = [7, 5, 3, 3, 2]
el = int(input("Введите число: "))

while el >= 0:
    pos = len(my_list)
    for i in range(pos):
        if el > my_list[i]:
            pos = i
            break
    my_list.insert(pos, el)
    print(f"Пользователь ввел число {el}. Результат: {my_list}")
    el = int(input("Введите число: "))
