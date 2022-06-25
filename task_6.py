products = []
data = {"название": "", "цена": "",
        "количество": "", "ед.": ""}

num = 0

while input("Для ввода данных нажмите - y," 
            "для аналитики нажмите - n: ") == 'y':
    num += 1
    for keys in data:
        data[keys] = input(f"Введите {keys}: ")
    products.append(tuple([num, data]))

print(products)
