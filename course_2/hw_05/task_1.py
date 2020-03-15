# 1
# Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных
# свидетельствует пустая строка.


def get_user_data():
    data = ''
    while True:
        user_data = input('Введите данные: ')
        if not user_data:
            break
        data += f'{user_data}\n'
    return data


def write_to_file(filename, data, encoding='utf-8'):
    with open(filename, 'w', encoding=encoding) as file:
        file.write(data)


if __name__ == '__main__':
    write_to_file('task_1.txt', get_user_data())
