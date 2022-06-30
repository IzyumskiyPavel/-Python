
def user_info(name, surname, year_of_birth, city, email, phone):
    print(f"{name} {surname}, {year_of_birth} года рождения."
          f"Проживает в городе {city}. Email: {email}. Телефон: {phone}")

user_info(
    name=input("Имя: "),
    surname=input("Фамилия: "),
    year_of_birth=input("Год рождения: "),
    city=input("Город проживания: "),
    email=input("Электронная почта: "),
    phone=input("Телефон: ")
    )
