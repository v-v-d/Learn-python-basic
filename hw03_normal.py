# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


names = ['ivan', 'Fedor', 'John', 'Lucia']
salaries = [200, 150, 50, 550000]

names_salaries_dict = dict(zip(names, salaries))

with open('salary.txt', 'w') as file:
    [file.write(f'{key.capitalize()} - {value}\n') for key, value in names_salaries_dict.items()]

with open('salary.txt', 'w') as file:
    dict_items = names_salaries_dict.items()
    for key, value in dict_items:
        name = key.capitalize()
        salary = value
        file.write(f'{name} - {salary}\n')

salary_display_threshold = 500000

with open('salary.txt', 'r') as file:
    [print(line.strip()) for line in file if int(line.split()[2]) < salary_display_threshold]

with open('salary.txt', 'r') as file:
    for line in file:
        salary = int(line.split()[2])
        if salary < salary_display_threshold:
            print(line.strip())
