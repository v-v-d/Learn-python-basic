# Реализовать проект расчета суммарного расхода ткани на производство
# одежды. Основная сущность (класс) этого проекта — одежда, которая
# может иметь определенное название. К типам одежды в этом проекте
# относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить
# работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике
# полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора
# @property.
from abc import ABC, abstractmethod


class Wear(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calc_raws(self):
        pass

    def __add__(self, other):
        return self.calc_raws() + other.calc_raws()

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_value_or_raise_error(value):
        if isinstance(value, (int, float)) and value > 0:
            return value
        else:
            raise ValueError(f'Value must be greater than 0, got {value}.')


class Coat(Wear):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = self.get_value_or_raise_error(size)

    def calc_raws(self):
        return self._size / 6.5 + 0.5

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = self.get_value_or_raise_error(value)

    @size.deleter
    def size(self):
        self._size = 1


class Costume(Wear):
    def __init__(self, name, height):
        super().__init__(name)
        self._height = self.get_value_or_raise_error(height)

    def calc_raws(self):
        return 2 * self.height + 0.3

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = self.get_value_or_raise_error(value)

    @height.deleter
    def height(self):
        self._height = 1


if __name__ == '__main__':
    coat = Coat('coat_1', 45)
    costume = Costume('costume_1', 46)

    print('******************', coat, '******************')
    print(f'{coat} size: {coat.size}')
    coat.size = 12
    print(f'{coat} size after reset: {coat.size}')
    print(f'Calc {coat} raws: {coat.calc_raws()}')

    print('******************', coat, '******************')
    print(f'{costume} size: {costume.height}')
    costume.height = 25
    print(f'{costume} size after reset: {costume.height}')
    print(f'Calc {costume} raws: {costume.calc_raws()}')

    print()

    print(f'Total raws: {coat.calc_raws() + costume.calc_raws()}')

    print(f'Delete {coat} size attr')
    del coat.size
    print(f'{coat} size after deleting: {coat.size}')

    print(f'Delete {costume} size attr')
    del costume.height
    print(f'{costume} height after deleting: {costume.height}')
