x = int(input("Введите целое положительное число: "))
y = int(input("Введите целое отрицательное число: "))

#Способ №1
def exponentiation(x, y):
    return x ** y

#Способ №2
def my_func(x, y):
    count = 1
    result = 1 /x
    while count != abs(y):
        count += 1
        result *= 1 / x
    return result

print(f"{x} в степени {y} = {exponentiation(x, y)}")
print(f"{x} в степени {y} = {my_func(x, y)}")
