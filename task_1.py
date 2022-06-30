def my_func(arg_1, arg_2):
    return arg_1 / arg_2

try:
    arg_1 = int(input("Введите первое число: "))
    arg_2 = int(input("Введите второе число: "))

    print(f"Результат деления двух чисел - {my_func(arg_1, arg_2)}")

except ZeroDivisionError:
    print("На ноль делить нельзя!")