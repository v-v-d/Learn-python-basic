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


def return_back(base_dir):
    if os.getcwd() != base_dir:
        dir_path = os.path.split(os.getcwd())
        os.chdir(dir_path[0])
        return f"\nУспешный переход в папку {dir_path[0]}"
    else:
        return "\nВы находитесь в корневой директории. Назад перейти невозможно"


def change_dir(base_dir, dir_name):
    dir_path = os.path.join(base_dir, dir_name)
    try:
        os.chdir(dir_path)
        return f"\nУспешный переход в папку {dir_name}\nТекущая директория: {os.getcwd()}"
    except FileNotFoundError:
        return f'\nНевозможно перейти в папку {dir_name}. Такой папки не существует.'


def console_menu():
    while True:
        print("""
Консольное меню

1. Перейти в папку
2. Просмотр указанной папки
3. Удалить папку
4. Создать папку
5. Выйти из консольного меню
        """)

        try:
            do = int(input("Выберите действие: "))
        except ValueError:
            print('Введите число')
            continue

        if do == 1:
            print(my_scripts.list_dirs(os.getcwd()))
            question_for_back = input("\nВернуться в предыдущую папку? [Y/N] ")
            question_for_back.lower()
            if question_for_back == "y":
                print(return_back(BASE_DIR))
            else:
                dir_name = input("\nВведите имя папки, в которую хотите перейти: ")
                print(change_dir(os.getcwd(), dir_name))

        elif do == 2:
            print(', '.join(my_scripts.list_dirs(os.getcwd())))
            print(', '.join(my_scripts.list_files(os.getcwd())))

        elif do == 3:
            print(my_scripts.list_dirs(os.getcwd()))
            dir_name = input("\nВведите имя папки, которую хотите удалить: ")
            dir_path = os.path.join(os.getcwd(), dir_name)
            print(my_scripts.delete_dir(dir_path))

        elif do == 4:
            dir_name = input("\nВведите имя папки, которую хотите создать: ")
            print(my_scripts.make_dir(dir_name))

        elif do == 5:
            print("Успешный выход из консольного меню.")
            break

        else:
            if do != range(1, 5):
                print("Действие не найдено. Попробуйте еще раз.")


BASE_DIR = os.getcwd()

if __name__ == '__main__':
    console_menu()
