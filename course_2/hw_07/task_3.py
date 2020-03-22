# Реализовать программу работы с органическими клетками, состоящими из
# ячеек. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству ячеек клетки
# (целое число). В классе должны быть реализованы методы перегрузки
# арифметических операторов: сложение (__add__()), вычитание
# (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные
# методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого)
# деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки
# должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
# если разность количества ячеек двух клеток больше нуля, иначе выводить
# соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как целочисленное деление количества ячеек этих двух
# клеток.
# В классе необходимо реализовать метод make_order(), принимающий
# экземпляр класса и количество ячеек в ряду. Данный метод позволяет
# организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где
# количество ячеек между \n равно переданному аргументу. Если ячеек на
# формирование ряда не хватает, то в последний ряд записываются все
# оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в
# ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, nucleus_qty):
        self.nucleus_qty = self.get_value_or_raise_error(nucleus_qty)

    @staticmethod
    def get_value_or_raise_error(value):
        if isinstance(value, int) and value > 0:
            return value
        else:
            raise ValueError(f'Value must be greater than 0, got {value}.')

    def __add__(self, other):
        return Cell(self.nucleus_qty + other.nucleus_qty)

    def __sub__(self, other):
        if self.nucleus_qty > other.nucleus_qty:
            return Cell(self.nucleus_qty - other.nucleus_qty)
        else:
            print('Can\'t subtract. Diminished must be greater than subtracted.')

    def __mul__(self, other):
        return Cell(self.nucleus_qty * other.nucleus_qty)

    def __truediv__(self, other):
        try:
            return Cell(self.nucleus_qty // other.nucleus_qty)
        except ZeroDivisionError as error:
            print(error)

    def make_order(self, row_len):
        if isinstance(row_len, int):
            result = ''
            nucleus_qty = self.nucleus_qty
            while nucleus_qty > 0:
                if nucleus_qty < row_len:
                    row_len = nucleus_qty
                result += f'{"*" * row_len}\n'
                nucleus_qty -= row_len

            return result
        else:
            return f'Value must be integer type, got {type(row_len)}.'


if __name__ == '__main__':
    cell_1 = Cell(12)
    cell_2 = Cell(3)

    cell_3 = cell_1 + cell_2
    print(cell_3.nucleus_qty)

    cell_4 = cell_1 - cell_2
    print(cell_4.nucleus_qty)

    cell_5 = cell_1 * cell_2
    print(cell_5.nucleus_qty)

    cell_6 = cell_1 / cell_2
    print(cell_6.nucleus_qty)

    print(cell_1.make_order(5))
