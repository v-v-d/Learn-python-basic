if __name__ == '__main__':
    # 1. Поработайте с переменными, создайте несколько, выведите на
    # экран, запросите у пользователя несколько чисел и строк и
    # сохраните в переменные, выведите на экран.

    var_1 = 'test'
    var_2 = 123
    var_3 = 123.123
    var_4 = None
    var_5 = input('enter something: ')

    print('Результат выполнения задания #1:')
    print(var_1, var_2, var_3, var_4, var_5)

    # 2. Пользователь вводит время в секундах. Переведите время в часы,
    # минуты и секунды и выведите в формате чч:мм:сс. Используйте
    # форматирование строк.

    user_time = input('enter time in seconds: ')

    print('Результат выполнения задания #2:')
    try:
        seconds = int(user_time)
        seconds = seconds % (24 * 3600)
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        print(f'{hours}:{minutes}:{seconds}')

    except ValueError as error:
        print(error)

    # 3. Узнайте у пользователя число n. Найдите сумму чисел
    # n + nn + nnn. Например, пользователь ввёл число 3. Считаем
    # 3 + 33 + 333 = 369.

    user_digit = input('enter some positive digit: ')

    print('Результат выполнения задания #3:')
    try:
        digit = int(user_digit)

        if 0 < digit < 10:
            print(digit + digit * 11 + digit * 111)
        else:
            raise ValueError(f'Positive digit needed. Got {digit}.')

    except ValueError as error:
        print(error)

    # 4. Пользователь вводит целое положительное число. Найдите самую
    # большую цифру в числе. Для решения используйте цикл while и
    # арифметические операции.

    user_number = input('enter some positive number: ')

    print('Результат выполнения задания #4:')
    try:
        number = int(user_number)
        max_digit = 0

        while number:
            digit = number % 10
            max_digit = digit if digit > max_digit else max_digit
            number //= 10

        print(max_digit)

    except ValueError as error:
        print(error)

    # 5. Запросите у пользователя значения выручки и издержек фирмы.
    # Определите, с каким финансовым результатом работает фирма (прибыль
    # — выручка больше издержек, или убыток — издержки больше выручки).
    # Выведите соответствующее сообщение. Если фирма отработала с
    # прибылью, вычислите рентабельность выручки (соотношение прибыли к
    # выручке). Далее запросите численность сотрудников фирмы и
    # определите прибыль фирмы в расчете на одного сотрудника.

    company_income = input('enter company income: ')
    company_costs = input('enter company costs: ')
    company_employee_amount = input('enter company employee amount: ')

    print('Результат выполнения задания #5:')
    try:
        income = float(company_income)
        costs = float(company_costs)
        employee_amount = int(company_employee_amount)

        if income < costs:
            print('The company have losses.')
        else:
            profit = income - costs

            print('The company have no losses.')
            print(f'Profitability: {income / profit}')
            print(f'Profit by employee: {profit / employee_amount}')

    except ValueError as error:
        print(error)

    # 6. Спортсмен занимается ежедневными пробежками. В первый день его
    # результат составил a километров. Каждый день спортсмен увеличивал
    # результат на 10 % относительно предыдущего. Требуется определить
    # номер дня, на который общий результат спортсмена составит не
    # менее b километров. Программа должна принимать значения параметров
    # a и b и выводить одно натуральное число — номер дня.

    user_first_day_result = input('enter first day result: ')
    user_needed_result = input('enter needed result: ')

    print('Результат выполнения задания #6:')
    try:
        first_day_result = float(user_first_day_result)
        needed_result = float(user_needed_result)
        needed_days = 1

        while first_day_result < needed_result:
            first_day_result += first_day_result * 1.1
            needed_days += 1

        print(f'Needed days: {needed_days}')

    except ValueError as error:
        print(error)
