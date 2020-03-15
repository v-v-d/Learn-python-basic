# 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.


def translate(data_dict, translation):
    result = dict()
    for key, val in data_dict.items():
        new_key = translation.get(key.lower())
        if new_key:
            result.update({new_key.capitalize(): val})

    return result


def get_num_dict_from_file(filename, encoding='utf-8'):
    with open(filename, encoding=encoding) as file:
        num_dict = dict()
        for line in file:
            line_list = line.split()
            num_dict.update({line_list[0]: line_list[2]})

    return num_dict


def get_nums_list(data_dict):
    return [f'{key} — {val}' for key, val in data_dict.items()]


def write_list_to_file(filename, data, encoding='utf-8'):
    with open(filename, 'w', encoding=encoding) as file:
        file.write('\n'.join(data))


if __name__ == '__main__':
    TRANSLATION = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }

    DATA = get_num_dict_from_file('task_4.txt')
    write_list_to_file('task_4_output.txt', get_nums_list(translate(DATA, TRANSLATION)))
