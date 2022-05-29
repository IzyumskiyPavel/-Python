def division(numb_1, numb_2):
    try:
        return numb_1 / numb_2
    except ZeroDivisionError:
        print("Вы что? Пытатетесь делить на ноль!")

numb_1 = int(input("Введите первое число: "))
numb_2 = int(input("Введите второе число: "))
print(division(numb_1, numb_2))
