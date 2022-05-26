words = input("Введите слова через пробел: ").split()
for a in range(len(words)):
    print(f"{a+1}. {words[a][:10]}")