if __name__ == '__main__':
    # 1. Создать список и заполнить его элементами различных типов данных.
    # Реализовать скрипт проверки типа данных каждого элемента. Использовать
    # функцию type() для проверки типа. Элементы списка можно не запрашивать
    # у пользователя, а указать явно, в программе.

    elements = [
        'str', 1, 1.2, complex(), list(), tuple(),
        set(), dict(), True, b'bytes', None
    ]

    for el in elements:
        print(type(el))

    # 2. Для списка реализовать обмен значений соседних элементов, т.е.
    # Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При
    # нечетном количестве элементов последний сохранить на своем месте. Для
    # заполнения списка элементов необходимо использовать функцию input().

    list_1 = [input('enter some elem: ') for _ in range(9)]

    for idx in range(0, len(list_1), 2):
        if idx <= len(list_1) - 2:
            list_1[idx], list_1[idx + 1] = list_1[idx + 1], list_1[idx]

    print(list_1)

    # 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить
    # к какому времени года относится месяц (зима, весна, лето, осень).
    # Напишите решения через list и через dict.

    user_month = input('enter month number: ')

    try:
        month = int(user_month)

        winter_months = [12, 1, 2]
        spring_months = [3, 4, 5]
        summer_months = [6, 7, 8]
        autumn_months = [9, 10, 11]

        seasons = {
            'winter': winter_months,
            'spring': spring_months,
            'summer': summer_months,
            'autumn': autumn_months,
        }

        for key, val in seasons.items():
            if month in val:
                print(key)
                break

    except ValueError as error:
        print(error)

    # 4. Пользователь вводит строку из нескольких слов, разделённых
    # пробелами. Вывести каждое слово с новой строки. Строки необходимо
    # пронумеровать. Если в слово длинное, выводить только первые 10 букв в
    # слове.

    words = input('enter some words: ')

    for word in words.split(' '):
        print(word[:10]) if len(word) > 10 else print(word)

    # 5. Реализовать структуру «Рейтинг», представляющую собой не
    # возрастающий набор натуральных чисел. У пользователя необходимо
    # запрашивать новый элемент рейтинга. Если в рейтинге существуют
    # элементы с одинаковыми значениями, то новый элемент с тем же значением
    # должен разместиться после них.
    # Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
    # Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
    # Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
    # Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
    # Набор натуральных чисел можно задать непосредственно в коде, например,

    my_list = [7, 5, 3, 3, 2]

    user_rating_element = input('enter some rating element: ')

    try:
        rating_element = int(user_rating_element)
        my_list.append(rating_element)
        my_list.sort(reverse=True)

        print(my_list)

    except ValueError as error:
        print(error)

    # 6. *Реализовать структуру данных «Товары». Она должна представлять
    # собой список кортежей. Каждый кортеж хранит информацию об отдельном
    # товаре. В кортеже должно быть два элемента — номер товара и словарь с
    # параметрами (характеристиками товара: название, цена, количество,
    # единица измерения). Структуру нужно сформировать программно, т.е.
    # запрашивать все данные у пользователя.
    # Пример готовой структуры:
    # [
    # (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    # (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    # (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
    # ]
    # Необходимо собрать аналитику о товарах. Реализовать словарь, в котором
    # каждый ключ — характеристика товара, например название, а значение —
    # список значений-характеристик, например список названий товаров.
    # Пример:
    # {
    # “название”: [“компьютер”, “принтер”, “сканер”],
    # “цена”: [20000, 6000, 2000],
    # “количество”: [5, 2, 7],
    # “ед”: [“шт.”]
    # }

    products = list()

    product_keys = ['name', 'price', 'qty', 'unit']

    user_products_qty = input('enter products qty you want: ')

    try:
        products_qty = int(user_products_qty)

        for product_number in range(1, products_qty + 1):
            product = dict.fromkeys(product_keys)
            for key, val in product.items():
                product[key] = input(f'enter product {key}: ')
            products.append((product_number, product))

        products_stats = {
            'name': [],
            'price': [],
            'qty': [],
            'unit': [],
        }

        for product in products:
            for key, val in product[1].items():
                if key == 'unit' and val in products_stats[key]:
                    continue
                products_stats[key].append(val)

        print(products_stats)

    except ValueError as error:
        print(error)
