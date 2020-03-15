# 2
# Создать текстовый файл (не программно), сохранить в нем несколько
# строк, выполнить подсчет количества строк, количества слов в каждой
# строке.
import re


def get_word_qty_per_line(line, word_pattern=r'\w\S*'):
    words = line.split()
    words_qty = 0
    for word in words:
        if re.search(word_pattern, word):
            words_qty += 1

    return words_qty


def get_word_qty_list_from_file(filename, encoding='utf-8'):
    with open(filename, encoding=encoding) as file:
        return [get_word_qty_per_line(line) for line in file]


if __name__ == '__main__':
    word_qty_list = get_word_qty_list_from_file('task_2.txt')

    print(f'Всего строк в файле: {len(word_qty_list)}')

    for idx, word_qty in enumerate(word_qty_list, 1):
        print(f'{word_qty} слов(а) в строке: {idx}.')
