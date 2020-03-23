# Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число», реализуйте перегрузку методов сложения и
# умножения комплексных чисел. Проверьте работу проекта, создав
# экземпляры класса (комплексные числа) и выполнив сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = None
        self.imag = None
        self.create(real, imag)

    def create(self, real, imag):
        if self.is_args_valid(real, imag):
            self.real = real
            self.imag = imag
        else:
            raise ValueError(
                'Can\'t create ComplexNumber object. Values must be an int type.'
            )

    @staticmethod
    def is_args_valid(real, imag):
        return all((isinstance(real, int), isinstance(imag, int)))

    def __add__(self, other):
        if self.is_complex(other):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)

    @staticmethod
    def is_complex(obj):
        if isinstance(obj, ComplexNumber):
            return True
        raise ValueError(f'Object must be a complex number, got {type(obj)}.')

    def __mul__(self, other):
        if self.is_complex(other):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real, imag)

    def __str__(self):
        imag = f'+{self.imag}' if self.imag > 0 else self.imag
        return f'{self.real}{imag}i'


if __name__ == '__main__':
    complex_1 = ComplexNumber(3, 5)
    complex_2 = ComplexNumber(-1, 1)

    complex_3 = complex_1 + complex_2
    complex_4 = complex_1 * complex_2

    print(complex_1)
    print(complex_2)
    print(complex_3)
    print(complex_4)
