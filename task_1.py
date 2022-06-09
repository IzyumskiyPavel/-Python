from sys import argv

name, time, salary, extra = argv

time = int(time)
salary = int(salary)
extra = int(extra)

res = (time * salary) + extra
print(f'Заработная плата сотрудника - {res}')
