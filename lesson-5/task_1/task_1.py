with open('my_file_1.txt', 'w', encoding='utf-8') as f_obj:
    while f_obj:
        result = input('Введите данные: ')
        f_obj.write(result + '\n')
        if not result:
            break
