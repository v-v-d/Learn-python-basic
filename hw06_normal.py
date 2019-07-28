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
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 0
        self.armor = 1 - random.randint(0, 20) / 100 + random.randint(0, 20) / 100

    def _get_total_damage(self, enemy_armor):
        self.damage = random.randint(0, 20) / enemy_armor
        return self.damage

    def attack(self, enemy_armor):
        self.health -= self._get_total_damage(enemy_armor)


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def _message_to_winner(self, player):
        return f'{player.name} победил!'

    def _is_dead(self, player):
        return player.health <= 0

    def attack(self, aggressor, victim):
        aggressor.attack(victim.armor)
        print(f'{aggressor.name} нанес {victim.name} урон. У {victim.name} осталось {victim.health} жизней')

    def _is_final_attack(self, aggressor, victim):
        self.attack(aggressor, victim)
        return True if self._is_dead(victim) else False

    def play(self):
        count = 1
        while True:
            if count % 2 == 0:
                if self._is_final_attack(self.player2, self.player1):
                    print(self._message_to_winner(self.player2))
                    break
            else:
                if self._is_final_attack(self.player1, self.player2):
                    print(self._message_to_winner(self.player1))
                    break
            count += 1


class Player(Person):
    pass


class Enemy(Person):
    pass


if __name__ == '__main__':
    player_1 = Player('player')
    player_2 = Enemy('enemy')

    game = Game(player_1, player_2)

    game.play()
