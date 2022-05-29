#Вариант №1 (используя функцию sort)
def get_max(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))

get_max(150, 50, 75)

#Вариант №2 (без функции sort)
def get_max(arg_1, arg_2, arg_3):
    print(f"Сумма наибольших двух аргументов равна: "
          f"{arg_1 + arg_2 + arg_3 - min([arg_1, arg_2, arg_3])}")

get_max(
    int(input("Введите первый аргумент: ")),
    int(input("Введите второй аргумент: ")),
    int(input("Введите третий аргумент: "))
)
