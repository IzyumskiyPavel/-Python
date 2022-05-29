def my_func(x, y):
    a = 1
    res = 1 / x
    while a < abs(y):
        res = res * (1 / x)
        a += 1
    return res


print(f'Результат: '
      f'{my_func(int(input("x =  ")), int(input("y =  ")))}')
