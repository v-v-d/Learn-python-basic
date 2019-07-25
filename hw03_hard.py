# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

import random


def get_player(name, health, damage, armor):
    key_list = ['name', 'health', 'damage', 'armor']
    value_list = [name, health, damage, armor]
    return dict(zip(key_list, value_list))


def write_player_data_to_file(player):
    with open(f"{player['name']}.txt", "w") as file:
        for key, value in player.items():
            file.write(f'{key} - {value}\n')


def get_dict_from_file(player_1):
    with open(f"{player_1['name']}.txt", "r") as file:
        player_dict = {}
        for line in file:
            stripped_line = line.strip().split(' - ')
            player_dict.update({stripped_line[0]: stripped_line[1]})
        return player_dict


def get_total_damage(aggressor, victim):
    aggressor['damage'] = random.randint(0, 20) / victim['armor']
    return aggressor['damage']


def attack(aggressor, victim):
    victim['health'] -= get_total_damage(aggressor, victim)


def victim_is_alive(victim):
    return victim['health'] >= 0


def attack_is_victorious(aggressor, victim):
    attack(aggressor, victim)
    if not victim_is_alive(victim):
        print(f"{aggressor['name']} is winner!\nTotal HP: {aggressor['health']}")
    return False if victim_is_alive(victim) else True


player_1 = []
player_2 = []

for i in range(1, 3):
    person_name = str(input(f'Player {i} name: '))
    person_health = 100
    person_damage = 0
    person_armor = 1 + random.randint(0, 20) / 100
    if i == 1:
        player_1 = get_player(person_name, person_health, person_damage, person_armor)
    else:
        player_2 = get_player(person_name, person_health, person_damage, person_armor)

write_player_data_to_file(player_1)
write_player_data_to_file(player_2)

player_1_data = get_dict_from_file(player_1)
player_2_data = get_dict_from_file(player_2)

while True:
    if attack_is_victorious(player_1, player_2) or attack_is_victorious(player_2, player_1):
        break
