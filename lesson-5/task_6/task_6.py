subjects = {}
with open("my_file_6.txt", "r", encoding="utf-8") as file:
    for line in file:
        total_lesson = 0
        split_line = line.split(":")
        subject = split_line[0]
        for item in split_line[1].split():
            s = "".join([symbol for symbol in item if symbol.isdigit()])
            if s:
                num = int(s)
                total_lesson += num
        subjects[subject] = total_lesson
print(subjects)
