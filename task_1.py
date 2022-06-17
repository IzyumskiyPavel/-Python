
class Matrix:
    def __init__(self, *args):
        self.new_list = list(args)

    def __str__(self):
        result = '\n'.join(map(str, self.new_list))
        result = result.replace(',', '').replace('[', '').replace(']', '')
        return result

    def __add__(self, other):
        new_sum = []
        line_sum = []
        for x in range(len(self.new_list)):
            for y in range(len(self.new_list[x])):
                line_sum.append(self.new_list[x][y] + other.new_list[x][y])
            new_sum.append(line_sum)
            line_sum = []
        return Matrix('\n'.join(map(str, new_sum)))


M_OBJ_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(M_OBJ_1)
print()

M_OBJ_2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(M_OBJ_2)
print()

print(f'Сумма матриц:\n{M_OBJ_1 + M_OBJ_2}')
