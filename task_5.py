from functools import reduce

my_list = [i for i in range(100, 1001, 2)]

print(my_list)

res = reduce(lambda i, i2: i * i2, my_list)

print(res)
