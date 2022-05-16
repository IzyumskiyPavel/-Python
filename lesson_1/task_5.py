revenue = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))
if revenue > cost:
    print("Финансовый результат - прибыль. Её величина: ", revenue-cost)
    print("Рентабельность выручки = ", revenue/cost)
    number = int(input("Введите численность сотрудников фирмы: "))
    print("Прибыль фирмы в расчёте на одного сотрудника =", (revenue-cost)/number)
if revenue < cost:
    print("Финансовый результат - убыток. Его размер: ", cost-revenue)

