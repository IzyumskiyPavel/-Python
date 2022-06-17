class Cell():
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return str(self.size)

    def __add__(self, cell):
        new_size = self.size + cell.size
        return Cell(new_size)
    def __sub__(self, cell):
        new_size = self.size - cell.size
        if new_size <= 0:
            return 'Операция не выполнена: разность отрицательная.'
        else:
            return Cell(new_size)
    def __mul__(self, cell):
        new_size = self.size * cell.size
        return Cell(new_size)
    def __truediv__(self, cell):
        new_size = self.size // cell.size
        return Cell(new_size)
    def make_order(self, row_size):
        counter = self.size
        result = ''
        for item in range(1, counter + 1):
            result += '*'
            if item % row_size == 0:
                result += '\n'
        return result

# Клиентский код:

print("Создаем объекты клеток")
cell1 = Cell(30)
cell2 = Cell(25)

cell3 = Cell(10)
cell4 = Cell(15)

print()

print("Складываем")
print(cell1 + cell2)

print()

print("Вычитаем")
print(cell2 - cell1)
print(cell4 - cell3)

print()

print("Умножаем")
print(cell2 * cell1)

print()

print("Делим")
print(cell1 / cell2)

print()

print("Организация ячеек по рядам")
print(cell1.make_order(5))
print(cell2.make_order(10))
