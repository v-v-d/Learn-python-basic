# # Задача-1:
# # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# # из которой запущен данный скрипт.
# # И второй скрипт, удаляющий эти папки.

import os


def make_dir(dirname):
    try:
        os.mkdir(os.path.join(os.getcwd(), dirname))
        return 'Папка создана'
    except FileExistsError as e:
        return f'{e}'


def delete_dir(dirname):
    try:
        os.rmdir(os.path.join(os.getcwd(), dirname))
        return 'Папка удалена'
    except FileNotFoundError as e:
        return f'{e}'


# # Задача-2:
# # Напишите скрипт, отображающий папки текущей директории.

def list_dirs(path):
    return [el for el in os.listdir(path) if os.path.isdir(el)]


def list_files(path):
    return [el for el in os.listdir(path) if os.path.isfile(el)]


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil


def get_copyfile(filename):
    try:
        file_name, ext = filename.split('.')
        shutil.copyfile(f'{file_name}.{ext}', f'{file_name}-copy.{ext}')
        return 'Копия файла создана'
    except FileNotFoundError as e:
        return f'{e}'
    except ValueError as e:
        return f'{e}'
    except AttributeError and NameError as e:
        return f'{e}'


if __name__ == '__main__':
    dirs_qty = 9

    [print(make_dir(f'dir_{i}')) for i in range(1, dirs_qty + 1)]
    [print(delete_dir(f'dir_{i}')) for i in range(1, dirs_qty + 1)]

    print(*list_dirs(os.getcwd()))

    print(get_copyfile(os.path.basename(__file__)))
