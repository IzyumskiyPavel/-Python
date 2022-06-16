class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_total_income(self):
        return sum(self._income.values())
ivan = Position('Иван', 'Иванов', 'Тестировщик', 120000, 30000)
print(ivan.get_full_name())
print(ivan.position)
print(ivan.get_total_income())
