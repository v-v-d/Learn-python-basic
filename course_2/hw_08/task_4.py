# Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработать методы, отвечающие
# за приём оргтехники на склад и передачу в определенное подразделение
# компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую
# структуру, например словарь.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества
# принтеров, отправленных на склад, нельзя использовать строковый тип
# данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад
# оргтехники» максимум возможностей, изученных на уроках по ООП.


class WarehouseExceededLimitError(Exception):
    pass


class OutOfWarehouseError(Exception):
    pass


class NotAWarehouseUnitError(Exception):
    pass


class NotOfficeEquipmentError(Exception):
    pass


class NotWarehouseError(Exception):
    pass


class Warehouse:
    def __init__(self, name, value=None):
        self.name = name
        self.value = None
        self.units = list()
        self.create(value)

    def create(self, value):
        if self.is_params_valid(value):
            self.value = value
        else:
            raise NotWarehouseError(
                'Can\'t create NotWarehouseError object. Parameters must be a num type.'
            )

    @staticmethod
    def is_params_valid(*params):
        return all([isinstance(param, (float, int)) for param in params])

    def take_to(self, unit):
        if self.is_unit_valid(unit):
            unit_value = unit.get_value()
            if self.value > unit_value:
                self.units.append(unit)
                self.value -= unit.get_value()
            else:
                raise WarehouseExceededLimitError(
                    f'Can\'t add {unit} to warehouse. '
                    f'Warehouse "{self.name}" capacity exceeded the limit.'
                )

    def take_off(self, unit):
        try:
            unit_idx = self.units.index(unit)
        except ValueError as error:
            raise OutOfWarehouseError(
                'Can\'t remove unit from warehouse. Unit not exists.'
            )
        else:
            self.units.pop(unit_idx)
            self.value += unit.get_value()

    @staticmethod
    def is_unit_valid(unit):
        try:
            unit.get_value()
            return True
        except AttributeError:
            raise NotAWarehouseUnitError(
                'Can\'t take to warehouse. Unit not a warehouse unit.'
            )

    def __repr__(self):
        return f'{self.name}'


class OfficeEquipment:
    def __init__(self, name, weight, length, width, height):
        self.name = name
        self.weight = None
        self.length = None
        self.width = None
        self.height = None
        self.create(weight, length, width, height)

    def create(self, weight, length, width, height):
        if self.is_params_valid(weight, length, width, height):
            self.weight = weight
            self.length = length
            self.width = width
            self.height = height
        else:
            raise NotOfficeEquipmentError(
                'Can\'t create OfficeEquipment object. Parameters must be a num type.'
            )

    @staticmethod
    def is_params_valid(*params):
        return all([isinstance(param, (float, int)) for param in params])

    def __repr__(self):
        return f'{self.name}'

    def __add__(self, other):
        if self.is_object_valid(other):
            return self.get_value() + other.get_value()

    @staticmethod
    def is_object_valid(obj):
        if isinstance(obj, OfficeEquipment):
            return True
        raise ValueError(
            f'Object must be a OfficeEquipment instance, got {type(obj)}.'
        )

    def get_value(self):
        return self.length * self.width * self.height


class Printer(OfficeEquipment):
    def __init__(self, name, weight, length, width, height, is_color=False):
        super().__init__(name, weight, length, width, height)
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, name, weight, length, width, height, form='A3'):
        super().__init__(name, weight, length, width, height)
        self.form = form


class Xerox(OfficeEquipment):
    def __init__(self, name, weight, length, width, height, speed):
        super().__init__(name, weight, length, width, height)
        self.speed = speed


if __name__ == '__main__':
    WAREHOUSE_1 = Warehouse('warehouse #1', 20)
    WAREHOUSE_2 = Warehouse('warehouse #2', 13)

    print(f'{WAREHOUSE_1} created. Value: {WAREHOUSE_1.value}')
    print(f'{WAREHOUSE_2} created. Value: {WAREHOUSE_2.value}')

    PRINTER_PARAMS = (5, 0.5, 0.5, 0.3, True)
    SCANNER_PARAMS = (5, 0.5, 0.3, 0.1, 'A4')
    XEROX_PARAMS = (5, 0.5, 0.4, 0.2, 60)

    PRINTERS = [Printer(f'printer #{i}', *PRINTER_PARAMS) for i in range(100)]
    SCANNERS = [Scanner(f'scanner #{i}', *SCANNER_PARAMS) for i in range(70)]
    XEROXES = [Xerox(f'xerox #{i}', *XEROX_PARAMS) for i in range(120)]

    UNITS = (PRINTERS, SCANNERS, XEROXES)

    total_units_value = sum([unit.get_value() for unit_list in UNITS for unit in unit_list])
    print(f'Units created. Total units value: {total_units_value}')

    for unit_list in UNITS:
        for unit in unit_list:
            try:
                WAREHOUSE_1.take_to(unit)
            except WarehouseExceededLimitError as error:
                print(error)

    print(f'Units added to {WAREHOUSE_1}')
    print(f'{WAREHOUSE_1} free value: {WAREHOUSE_1.value}')

    for unit_list in UNITS:
        for unit in unit_list:
            try:
                WAREHOUSE_2.take_to(unit)
            except WarehouseExceededLimitError as error:
                print(error)

    print(f'Units added to {WAREHOUSE_2}')
    print(f'{WAREHOUSE_2} free value: {WAREHOUSE_2.value}')

    for unit in PRINTERS:
        WAREHOUSE_1.take_off(unit)

    print(f'Units removed from {WAREHOUSE_1}')
    print(f'{WAREHOUSE_1} value: {WAREHOUSE_1.value}')
