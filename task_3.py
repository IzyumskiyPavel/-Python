my_list = ['Зима', 'Весна', 'Лето', 'Осень']
my_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

month = int(input("Введите номер месяца: "))

if 0 < month <= 12:
    if month == 12 or month < 3:
        season = 1
    elif month < 6:
        season = 2
    elif month < 9:
        season = 3
    else:
        season = 4

else:
    print("Такого месяца нет")

print(f"Результат через список: {my_list[season - 1]}")
print(f"Результат через словарь: {my_dict.get(season)}")