# Написать программу, которая будет содержать функцию для получения имени
# файла из полного пути до него. При вызове функции в качестве аргумента должен
# передаваться путь до файла. В функции необходимо реализовать «выделение» из
# этого пути имени файла (без расширения).
import os


def get_filename_from_path(filepath):
    return os.path.basename(filepath).split('.')[0]


print(get_filename_from_path(__file__))


# Написать программу, которая запрашивает у пользователя ввод числа. На
# введенное число она отвечает сообщением, целое оно или дробное. Если дробное
# — необходимо далее выполнить сравнение чисел до и после запятой. Если они
# совпадают, программа должна возвращать значение True, иначе False.


def is_float_symmetric(float_num):
    frac, whole = str(float_num).split('.')
    return True if frac == whole else False


while True:
    try:
        user_num = float(input('Введите число: '))
    except ValueError as error:
        print(error)
    else:
        break
message = 'целое' if user_num.is_integer() else 'дробное'
print(user_num, message)

if message == 'дробное':
    cond = 'равны' if is_float_symmetric(user_num) else 'неравны'
    print('левая и правая части', cond)

# Создать два списка с различным количеством элементов. В первом должны быть
# записаны ключи, во втором — значения. Необходимо написать функцию, создающую
# из данных ключей и значений словарь. Если ключу не хватает значения, в
# словаре для него должно сохраняться значение None. Значения, которым не
# хватило ключей, необходимо отбросить.

from itertools import zip_longest


def get_dict_with_default_none(keys, values):
    return dict(zip_longest(keys, values))


list_1 = [1, 2, 3]
list_2 = [4, 5]

print(get_dict_with_default_none(list_1, list_2))

# Написать программу, в которой реализовать две функции. В первой должен
# создаваться простой текстовый файл. Если файл с таким именем уже существует,
# выводим соответствующее сообщение. Необходимо открыть файл и подготовить два
# списка: с текстовой и числовой информацией. Для создания списков использовать
# генераторы. Применить к спискам функцию zip(). Результат выполнения этой
# функции должен должен быть обработан и записан в файл таким образом, чтобы
# каждая строка файла содержала текстовое и числовое значение. Вызвать вторую
# функцию. В нее должна передаваться ссылка на созданный файл. Во второй
# функции необходимо реализовать открытие файла и простой построчный вывод
# содержимого. Вся программа должна запускаться по вызову первой функции.
import os
from string import ascii_letters
from random import randint, choice


def create_file(filename):
    filepath = os.path.join(os.getcwd(), filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w'):
            pass
        return filepath
    else:
        print('файл уже существует.')


def read_from_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read().splitlines()


def write_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(data)


filename = 'test.txt'
nums = [randint(1, 100) for _ in range(10)]
strs = [''.join([choice(ascii_letters) for _ in range(randint(5, 10))])
        for _ in range(10)]

filepath = create_file(filename)

if filepath:
    write_to_file(filepath, [f'{i} {j}\n' for i, j in zip(nums, strs)])

    for line in read_from_file(filepath):
        print(line)

# Усовершенствовать первую функцию из предыдущего примера. Необходимо
# просканировать текстовый файл, созданный на предыдущем задании и реализовать
# создание и запись нового текстового файла. В новый текстовый файл записать
# строки из первого текстового файла, где вместо чисел ставится строка.
import re

if filepath:
    result = [re.sub(r'^\d+', re.search(r'\w+$', line).group(), line)
              for line in read_from_file(filepath)]

    write_to_file(filepath, '\n'.join(result))
