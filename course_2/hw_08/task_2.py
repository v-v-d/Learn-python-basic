# Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на нуль. Проверьте его работу на данных, вводимых пользователем. При
# вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyZeroDivisionError(Exception):
    pass


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as error:
        raise MyZeroDivisionError(error)


if __name__ == '__main__':
    x = 1
    y = 0

    try:
        print(division(x, y))
    except MyZeroDivisionError as error:
        print(f'Something going wrong. Error: {error}')
