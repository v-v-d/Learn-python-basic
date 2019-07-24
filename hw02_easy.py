# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]

# max_fruit_chars = len(fruits[0])
#
# for fruit in fruits:
#     if len(fruit) > max_fruit_chars:
#         max_fruit_chars = len(fruit)

max_fruit_chars = len(max(fruits, key=len))

# [print(f'{num}. {fruit:>{max_fruit_chars}}') for num, fruit in enumerate(fruits, start=1)]
[print(f'{num}. {fruit.rjust(max_fruit_chars)}') for num, fruit in enumerate(fruits, start=1)]

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

lst_1 = [1, 23, 546, 7, 8, 9]
lst_2 = [2, 23, 8, 7, 19, 50]

lst_1 = [num for num in lst_1 if num not in lst_2]

print(lst_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num_list_2 = [num/4 if num % 2 == 0 else num*2 for num in num_list]

print(num_list_2)
