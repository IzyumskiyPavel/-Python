with open('my_file_2.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    print('Общее количество строк:', len(data))
    result = [f'Слов в {data.index(el) + 1} строке - {len(el.split())}' for el in data]
    for item in result:
        print(item)
