# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import hw05_easy as my_scripts
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создание копии указанного файла")
    print("rm <file_name> - удаление указанного файла")
    print("cd <full_path or relative_path> - изменение текущей директории на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f'директория {dir_name} создана')
    except FileExistsError:
        print(f'директория {dir_name} уже существует')


def ping():
    print("pong")


def cp():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
    else:
        print(my_scripts.get_copyfile(file_name))


def rm():
    if not file_name:
        return print("Необходимо указать имя файла вторым параметром")
    answer = input(f'Вы уверены, что хотите удалить {file_name}? [y/n]: ')
    if answer.lower() == 'y':
        try:
            os.remove(file_name)
            print('Файл удален')
        except FileNotFoundError as e:
            print(f'{e}')


def is_relative_path():
    list_dirs = my_scripts.list_dirs(os.getcwd())
    return True if path in list_dirs else False


def cd():
    if not path:
        return print("Необходимо указать путь вторым параметром")
    try:
        os.chdir(os.path.join(os.getcwd(), path)) if is_relative_path() else os.chdir(path)
        return print(os.getcwd())
    except FileNotFoundError:
        print('Нет такой директории')


def ls():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    path = sys.argv[2]
except IndexError:
    path = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
