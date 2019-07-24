# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4


number = int(input('Insert a number: '))
lower_bound = 0
upper_bound = 10

while not lower_bound < number < upper_bound:
    print(f'Number is incorrect. You need input a number in a bounds from {lower_bound} to {upper_bound}')
    number = int(input('Insert a number: '))

print(f'Square of input number: {number ** 2}')


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;


number_1 = int(input('Input a number 1: '))
number_2 = int(input('Input a number 2: '))

number_1, number_2 = number_2, number_1

print(f'Number 1: {number_1}, number 2: {number_2}')
