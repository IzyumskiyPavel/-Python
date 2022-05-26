season_list = ['Зима', 'Весна', 'Лето', 'Осень']
season_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите номер месяца: "))
season = 0

if 1 <= month <= 12:
    if month < 3 or month == 12:
        season = 1
    elif month < 6:
        season = 2
    elif month < 9:
        season = 3
    else:
        season = 4

    print(f"Результат через список: {season_list[season-1]}")
    print(f"Результат через словарь: {season_dict.get(season)}")

else:
    print("Неправильный ввод")
    
