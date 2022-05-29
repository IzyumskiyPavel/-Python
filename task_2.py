def user_info(name, surname, year_of_birth, city, email, phone):
    print(f"{name} {surname} {year_of_birth} года рождения, проживает в городе {city}, "
          f"email: {email}, телефон: {phone}")

user_info(
    name=input("Введите Ваше имя: "),
    surname=input("Введите Вашу фамилию: "),
    year_of_birth=input("Год рождения: "),
    city=input("Город проживания: "),
    email=input("Почтовый ящик: "),
    phone=input("Телефон: ")
)
