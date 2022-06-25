my_list = input("Ввести слова через пробел: ").split()

for i in range(len(my_list)):
    print(f"{i+1}. {my_list[i][:10]}")

