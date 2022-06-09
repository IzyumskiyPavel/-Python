from itertools import count, cycle

for item in count(int(input("Введите число: "))):
    if item > 10:
        break
    else:
        print(item)

count = 0
for item in cycle(['a', 'b', 'c', 'd']):
    if count > 10:
        break
    else:
        print(item)
        count += 1
