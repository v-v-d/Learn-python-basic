# 3
# Реализовать базовый класс Worker (работник), в котором определить
# атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе
# Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income). Проверить
# работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы
# экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = wage
        self._bonus = bonus
        self.income = self._set_income()

    def _set_income(self):
        return {'wage': self._wage, 'bonus': self._bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        wage = self.income.get('wage')
        bonus = self.income.get('bonus')

        return wage + bonus if bonus else wage


if __name__ == '__main__':
    nuclear_safety_inspector = Position(
        'Homer', 'Simpson', 'nuclear_safety_inspector', 100
    )
    print(nuclear_safety_inspector.get_full_name())
    print(nuclear_safety_inspector.get_total_income())
