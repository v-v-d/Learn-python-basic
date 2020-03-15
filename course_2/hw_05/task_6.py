# 6
# Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и
# лабораторных занятий по этому предмету и их количество. Важно, чтобы
# для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика:   100(л)   50(пр)   20(лаб).
# Физика:   30(л)   —   10(лаб)
# Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re


def get_num_from_found(item, split_symbol='(', none_symbol='—'):
    if item:
        val = item.split(split_symbol)
        if val != none_symbol:
            try:
                return int(val[0])
            except:
                pass


if __name__ == '__main__':
    pattern = r'(.*:)(\s*)(\d*\(л\)|—)(\s*)(\d*\(пр\)|—)(\s*)(\d*\(лаб\)|—)'

    with open('task_6.txt', encoding='utf-8') as file:
        result = dict()

        for line in file:
            found = re.search(pattern, line).groups()
            header = found[0]
            nums = list()

            for item in found:
                num = get_num_from_found(item)
                if num:
                    nums.append(num)

            result.update({header: sum(nums)})

        print(result)
