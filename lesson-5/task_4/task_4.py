from functools import reduce


with open('my_file_4.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    data_dict = {el.split()[0]: el.split()[1] for el in data}
    print('Оклад более 20 тыс. имеют:')
    for item in data_dict:
        if int(data_dict[item]) < 20000:
            print(item)
        average = reduce(lambda a, b: int(a) + int(b), data_dict.values()) / len(data_dict.values())
    print(f'Cредняя величина дохода: {average}')
