# 7
# Создать вручную и заполнить несколькими строками текстовый файл, в
# котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить ее в словарь (со значением убытков).
# Пример списка:
# [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json
import re


def get_companies_stats_from_file(filename, re_pattern, encoding='utf-8'):
    with open(filename, encoding=encoding) as file:
        result = dict()
        avg_profit = 0
        profit_company_num = 0

        for line in file:
            found = re.search(re_pattern, line).groups()
            header = found[0]
            profit = float(found[4]) - float(found[6])

            if profit > 0:
                avg_profit += profit
                profit_company_num += 1

            result.update({header: profit})

        avg_profit = avg_profit / profit_company_num if profit_company_num else avg_profit

        return [result, {'average_profit': avg_profit}]


if __name__ == '__main__':
    pattern = r'(\w*)(\s*)(\w*)(\s*)(\d*)(\s*)(\d*)'

    companies_stats = get_companies_stats_from_file('task_7.txt', pattern)

    with open('task_7_output.json', 'w', encoding='utf-8') as file:
        json.dump(companies_stats, file)
