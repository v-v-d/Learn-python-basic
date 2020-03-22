# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список
# списков) для формирования матрицы. Следующий шаг — реализовать
# перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый
# элемент первой строки первой матрицы складываем с первым элементом
# первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        new_matrix = [
            [el + other.matrix[row_idx][col_idx] for col_idx, el in enumerate(row)]
            for row_idx, row in enumerate(self.matrix)
        ]
        return Matrix(new_matrix)


if __name__ == '__main__':
    matrix_1 = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])
    matrix_2 = Matrix([
        [7, 8, 9],
        [10, 11, 12],
    ])

    print('******************', 'Matrix #1', '******************')
    print(matrix_1)
    print('******************', 'Matrix #2', '******************')
    print(matrix_2)

    matrix_3 = matrix_1 + matrix_2

    print('******************', 'Matrix #3', '******************')
    print(matrix_3)
