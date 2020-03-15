# 3
# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить, кто
# из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
# сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


def get_emp_stats(stats_list, avg_income, richest_emp, total_emp, max_wage):
    emp_income = float(stats_list[1])
    avg_income += emp_income
    if emp_income < max_wage:
        richest_emp.append(stats_list[0])
    total_emp += 1

    return avg_income, richest_emp, total_emp


def get_emp_stats_from_file(filename, max_wage, encoding='utf-8'):
    with open(filename, encoding=encoding) as file:
        richest_emp, avg_income, total_emp = list(), 0, 0

        for line in file:
            emp_stats_list = line.split()
            avg_income, richest_emp, total_emp = get_emp_stats(
                emp_stats_list, avg_income, richest_emp, total_emp, max_wage
            )

        avg_income /= total_emp

        return richest_emp, avg_income


if __name__ == '__main__':
    wage_threshold = 20000

    richest_employee, average_income = get_emp_stats_from_file(
        'task_3.txt', wage_threshold
    )

    print(
        f'Сотрудники с окладом < {wage_threshold}: {", ".join(richest_employee)}, '
        f'средняя зп по сотрудникам: {average_income}'
    )
