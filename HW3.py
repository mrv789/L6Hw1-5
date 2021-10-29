class Worker:
    name = None
    surname = None
    position = None
    _income = {
        'wage': 'wage',
        'bonus': 'bonus'
    }

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


pos = Position('Иван', 'Иванов', 'Специалист', 23000, 13500)

print(pos.get_full_name())
print(pos.get_total_income())