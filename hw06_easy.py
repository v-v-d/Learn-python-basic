# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is went'

    def stop(self):
        return f'{self.name} is stopped'

    def turn(self, direction):
        return f'{self.name} is turned to the {direction}'


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass


town_car_1 = TownCar(120, 'black', 'audi', False)
sport_car_1 = SportCar(350, 'red', 'ferrari', False)
work_car_1 = WorkCar(80, 'yellow', 'kamaz', False)
police_car_1 = PoliceCar(120, 'white-blue', 'mercedes', True)

print(town_car_1.go())
print(town_car_1.stop())
print(town_car_1.turn('right'))

print(sport_car_1.go())
print(sport_car_1.stop())
print(sport_car_1.turn('left'))

print(work_car_1.go())
print(work_car_1.stop())
print(work_car_1.turn('right'))

print(police_car_1.go())
print(police_car_1.stop())
print(police_car_1.turn('left'))
