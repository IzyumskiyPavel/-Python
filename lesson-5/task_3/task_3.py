dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('my_file_3.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    keys = dictionary.keys()
    for item in data:
        for key in keys:
            if key in item:
                line_out = item.replace(key, dictionary[key])
                with open('output_file_3.txt', 'a', encoding='utf-8') as f_out:
                     f_out.write(line_out)
