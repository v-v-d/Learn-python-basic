# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

dirs_qty = 9

try:
    [os.mkdir(os.getcwd() + f'/dir_{i}') for i in range(1, dirs_qty + 1)]
except FileExistsError:
    print('Can\'t make a dir cause it\'s already exists')

try:
    [os.rmdir(os.getcwd() + f'/dir_{i}') for i in range(1, dirs_qty + 1)]
except FileNotFoundError:
    print('Can\'t delete a dir cause it\'s not exists')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

[print(el) for el in os.listdir(os.getcwd()) if os.path.isdir(el)]

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

current_file_name, ext = os.path.basename(__file__).split('.')

try:
    shutil.copyfile(f'{current_file_name}.{ext}', f'{current_file_name}-copy.{ext}')
except FileNotFoundError:
    print('Can\'t make a copy cause source file not exists')
