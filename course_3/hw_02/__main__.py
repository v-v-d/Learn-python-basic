# 1. Проверить механизм наследования в Python. Для этого создать два класса.
# Первый — родительский (ItemDiscount), должен содержать статическую информацию
# о товаре: название и цену. Второй — дочерний (ItemDiscountReport), должен
# содержать функцию (get_parent_data), отвечающую за отображение информации о
# товаре в одной строке. Проверить работу программы, создав экземпляр (объект)
# родительского класса.

class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'name: {self.name}, price: {self.price}'


item_1 = ItemDiscountReport('item_1', 1)
print(item_1.get_parent_data())


# 2. Инкапсулировать оба параметра (название и цену) товара родительского
# класса. Убедиться, что при сохранении текущей логики работы программы будет
# сгенерирована ошибка выполнения.

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'name: {self.__name}, price: {self.__price}'


item_2 = ItemDiscountReport('item_2', 2)


# print(item_2.get_parent_data()) -->
# AttributeError:
# 'ItemDiscountReport' object has no attribute '_ItemDiscountReport__name'


# 3. Усовершенствовать родительский класс таким образом, чтобы получить доступ
# к защищенным переменным. Результат выполнения заданий 1 и 2 должен быть
# идентичным.

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'name: {self.name}, price: {self.price}'


item_3 = ItemDiscountReport('item_3', 3)
print(item_3.get_parent_data())


# 4. Реализовать возможность переустановки значения цены товара. Необходимо,
# чтобы и родительский, и дочерний классы получили новое значение цены.
# Следует проверить это, вызвав соответствующий метод родительского класса и
# функцию дочернего (функция, отвечающая за отображение информации о товаре в
# одной строке).


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'name: {self.name}, price: {self.price}'


item_4 = ItemDiscountReport('item_4', 4)
print(item_4.get_parent_data())
item_4.price = 44
print(item_4.get_parent_data())


# 5. Реализовать расчет цены товара со скидкой. Величина скидки должна
# передаваться в качестве аргумента в дочерний класс. Выполнить перегрузку
# методов конструктора дочернего класса (метод init, в который должна
# передаваться переменная — скидка), и перегрузку метода str дочернего класса.
# В этом методе должна пересчитываться цена и возвращаться результат — цена
# товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать
# дочерний и родительский классы (вторая и третья строка после объявления
# дочернего класса).

class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        if self.discount:
            self.price -= self.price * self.discount * 0.01
        return f'price: {self.price}'


item_5 = ItemDiscountReport('item_5', 5, 10)
print(item_5)

# 6. Проверить на практике возможности полиморфизма. Необходимо разделить
# дочерний класс ItemDiscountReport на два класса. Инициализировать классы
# необязательно. Внутри каждого поместить функцию get_info, которая в первом
# классе будет отвечать за вывод названия товара, а вторая — его цены. Далее
# реализовать выполнение каждой из функции тремя способами.
from abc import ABC, abstractmethod


class ItemDiscount(ABC):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @abstractmethod
    def get_info(self):
        pass


class ItemDiscountReportName(ItemDiscount):
    def get_info(self):
        return self.name


class ItemDiscountReportPrice(ItemDiscount):
    def get_info(self):
        return self.price


item_6_1 = ItemDiscountReportName('item_6_1', 6.1)
item_6_2 = ItemDiscountReportPrice('item_6_2', 6.2)

print(item_6_1.get_info())
print(item_6_2.get_info())
