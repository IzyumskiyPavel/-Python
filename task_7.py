from itertools import count
from math import factorial

def func():
    for i in count(1):
        yield factorial(i)

gen = func()

x = 0
for i in gen:
    if x > 10:
        break
    else: print(i)
    x += 1
