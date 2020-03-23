# Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год». В рамках
# класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу
# «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class NotDateError(Exception):
    pass


class Date:
    day = None
    month = None
    year = None

    def __init__(self, date_str):
        self.date_str = date_str
        self.set_date_values(self.date_str)
        self.convert_date_values()

    @classmethod
    def set_date_values(cls, date_str):
        date_values = date_str.split('-')
        if cls.is_date_format_valid(date_values):
            cls.day, cls.month, cls.year = date_values

    @staticmethod
    def is_date_format_valid(date_values):
        if len(date_values) == 3:
            return True
        raise ValueError(
            'Wrong date format. Date format must be "{day}-{month}-{year}"'
        )

    @classmethod
    def convert_date_values(cls):
        try:
            cls.day = int(cls.day)
            cls.month = int(cls.month)
            cls.year = int(cls.year)
        except ValueError:
            raise NotDateError(
                'Can\'t create Date object. Passed args must be a valid integers.'
            )

    @staticmethod
    def is_date_valid(day, month, year):
        if all((isinstance(day, int), isinstance(month, int), isinstance(year, int))):
            return all((1 <= day <= 31, 1 <= month <= 12, year > 0))
        raise NotDateError(
            'Can\'t create Date object. Passed args must be a valid integers.'
        )


if __name__ == '__main__':
    date = Date('23-03-2020')
    print('Day:', date.day)
    print('Month:', date.month)
    print('Year:', date.year)
