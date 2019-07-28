# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть указанной папки
# 3. Удалить папку
# 4. Создать папку
# При выборе любых пунктов печатается статус "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import hw05_easy as my_scripts
import os


def return_to_back_dir():
    dir_path = os.path.split(os.getcwd())
    os.chdir(dir_path[0])
    return dir_path[0]


def change_dir():
    if os.getcwd() != BASE_DIR:
        question_for_back = input("Вернуться в предыдущую папку? [Y/N] ")
        if question_for_back.lower() == "y":
            return return_to_back_dir()
    dir_name = input("Введите имя папки, в которую хотите перейти: ")
    dir_path = os.path.join(BASE_DIR, dir_name)
    try:
        os.chdir(dir_path)
        return dir_path
    except FileNotFoundError as e:
        return f'{e}'


def list_dir():
    return os.listdir(os.getcwd())


def print_menu(menu):
    print('Консольное меню: ')
    [print(f'{num}. {key}') for num, key in enumerate(menu, start=1)]
    print('----------------')


def get_command(limit):
    command = int(input('Выберите действие: '))
    return command if 1 <= command <= limit else None


def my_exit():
    exit(0)


def run_console_menu():
    while True:
        print_menu(menu)
        try:
            command = get_command(len(menu))
            if command:
                key = list(menu.keys())[command - 1]
                if command in (3, 4):
                    dir_name = input('Введите имя папки: ')
                    print(menu[key](dir_name))
                else:
                    print(menu[key]())
            else:
                print('Ошибка! Такого действия нет')
        except ValueError:
            print('Ошибка! Введите число')


menu = {
    'Перейти в папку': change_dir,
    'Просмотр указанной папки': list_dir,
    'Удалить папку': my_scripts.delete_dir,
    'Создать папку': my_scripts.make_dir,
    'Выйти из консольного меню': my_exit,
}


if __name__ == '__main__':
    BASE_DIR = os.getcwd()

    run_console_menu()
