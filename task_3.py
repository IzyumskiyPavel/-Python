
def my_func(*args):
    my_list = list(args)
    my_list.sort()
    return my_list[1] + my_list[2]

print(f"Сумма двух наибольших значений - {my_func(123, 3, 13)}")