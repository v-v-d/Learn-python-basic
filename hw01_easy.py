# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран


user_age = int(input('Insert your age: '))
valid_user_age = 18

some_string = 'some string'

print(f'user_age: {user_age}, valid_user_age: {valid_user_age}, some_string: {some_string}')


# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.


number = int(input('Insert number: '))

print(f'Inserted number + 2: {number + 2}')


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"


user_age = int(input('Insert your age: '))
valid_user_age = 18

print('Доступ разрешен') if user_age >= valid_user_age else print('Доступ запрещен')
