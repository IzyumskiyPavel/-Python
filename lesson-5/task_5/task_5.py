with open('my_file_5.txt', 'w', encoding='utf-8') as f_num:
    f_num.write('1 2 3 4 5 6 7 8 9 10')

with open('my_file_5.txt', encoding='utf-8') as f_num:
    f = f_num.read().split()
    result = sum(map(int, f))
    print(f'Сумма чисел - {result}')
