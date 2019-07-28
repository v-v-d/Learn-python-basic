# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random


class Person:
    def __init__(self, name, health=100):
        self._name = name
        self._health = health
        self._armor = round(1 - random.randint(0, 20) / 100 + random.randint(0, 20) / 100, 2)
        self._damage = random.randint(15, 20)
        self._lvl = 1

    def get_health(self):
        return self._health

    def get_armor(self):
        return self._armor

    def get_damage(self):
        return self._damage

    def _set_health(self, value):
        self._health = value

    def hit(self, damage):
        self._set_health(self._health - damage)

    def _calculate_damage(self, enemy):
        return round(self._damage / enemy.get_armor(), 2)

    def attack(self, enemy):
        damage = self._calculate_damage(enemy)
        enemy.hit(damage)

    def is_alive(self):
        return self._health > 0


class Player(Person):

    def __init__(self, name, health):
        super().__init__(name, health)
        self._experience = 1
        self._exp_to_next_lvl = 100

    def get_experience(self):
        return self._experience

    def _is_next_level(self):
        if self._experience >= self._exp_to_next_lvl:
            self._lvl += 1
            self._exp_to_next_lvl *= 2

    def increase_experience(self, value):
        if value > 0:
            self._experience += value
            self._is_next_level()


class Enemy(Person):

    def __init__(self, name, lvl):
        super().__init__(name)
        self._lvl = lvl
        self._health *= lvl
        self._armor *= lvl
        self._damage *= lvl


class Game:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def start(self):
        last_attacker = self._player
        while self._player.is_alive() and self._enemy.is_alive():
            if last_attacker == self._player:
                self._enemy.attack(self._player)
                print(f'Враг dmg: {self._enemy._calculate_damage(self._player)}, armor: {self._enemy.get_armor()}, HP: {self._enemy.get_health()}')
                last_attacker = self._enemy
            else:
                self._player.attack(self._enemy)
                print(f'Игрок dmg: {self._player._calculate_damage(self._enemy)}, armor: {self._player.get_armor()}, HP: {self._player.get_health()}')
                last_attacker = self._player
        if self._player.is_alive():
            print('Игрок победил.')
        else:
            print('Враг победил.')


if __name__ == '__main__':
    player = Player('Igor', 100)
    enemy = Enemy('Vasya', 1)
    game = Game(player, enemy)
    game.start()

# import random
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#         self.damage = 0
#         self.armor = 1 - random.randint(0, 20) / 100 + random.randint(0, 20) / 100
#
#     def _get_total_damage(self, enemy_armor):
#         self.damage = random.randint(0, 20) / enemy_armor
#         return self.damage
#
#     def attack(self, enemy_armor):
#         self.health -= self._get_total_damage(enemy_armor)
#
#
# class Game:
#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2
#
#     def _message_to_winner(self, player):
#         return f'{player.name} победил!'
#
#     def _is_dead(self, player):
#         return player.health <= 0
#
#     def attack(self, aggressor, victim):
#         aggressor.attack(victim.armor)
#         print(f'{aggressor.name} нанес {victim.name} урон. У {victim.name} осталось {victim.health} жизней')
#
#     def _is_final_attack(self, aggressor, victim):
#         self.attack(aggressor, victim)
#         return True if self._is_dead(victim) else False
#
#     def play(self):
#         count = 1
#         while True:
#             if count % 2 == 0:
#                 if self._is_final_attack(self.player2, self.player1):
#                     print(self._message_to_winner(self.player2))
#                     break
#             else:
#                 if self._is_final_attack(self.player1, self.player2):
#                     print(self._message_to_winner(self.player1))
#                     break
#             count += 1
#
#
# class Player(Person):
#     pass
#
#
# class Enemy(Person):
#     pass
#
#
# if __name__ == '__main__':
#     player_1 = Player('player')
#     player_2 = Enemy('enemy')
#
#     game = Game(player_1, player_2)
#
#     game.play()
