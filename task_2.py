
class DivisionByNull(Exception):
    def __init__(self, txt):
        self.txt = txt


def divide_by_null(divider, denominator):
    try:
        if denominator == 0:
            raise DivisionByNull("Деление на ноль недопустимо")
        print(divider / denominator)
    except DivisionByNull as err:
        print(err)


divide_by_null(100, 0)
