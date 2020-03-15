# 4
# Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).  А также методы: go,
# stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для
# классов TownCar и WorkCar переопределите метод show_speed. При
# значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните
# доступ к атрибутам, выведите результат. Выполните вызов методов и
# также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'You go.'

    def stop(self):
        return 'You stop.'

    def turn(self, direction):
        possible_directions = ('left', 'right')
        if direction not in possible_directions:
            result = (
                'Wrong direction. '
                f'Expected: {", ".join(possible_directions)}, '
                f'got: {direction}'
            )
        else:
            result = f'You turn to {direction}.'

        return result

    def show_speed(self):
        return self.speed

    def __str__(self):
        return f'{self.name}'


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.speed_limit = 60

    def show_speed(self):
        if self.speed_limit and self.speed > self.speed_limit:
            print(
                f'Over speed detected. Expected: {self.speed_limit}, '
                f'got: {self.speed}.'
            )
            return -1
        return self.speed


class SportCar(Car):
    pass


class WorkCar(TownCar, Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.speed_limit = 40


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


def test_run(obj):
    print(f'*************** {obj} ***************')
    print('Car name:', obj.name)
    print('Car color:', obj.color)
    print('Car is police status:', obj.is_police)
    print('Test car go method:', obj.go())
    print('Test car turn method (valid):', obj.turn('left'))
    print('Test car turn method (invalid):', obj.turn(666))
    print('Test car stop method:', obj.stop())
    print('Test car speed method:')
    print(obj.show_speed())


if __name__ == '__main__':
    town_car = TownCar(60, 'black', 'town_car_#1')
    sport_car = SportCar(170, 'red', 'sport_car_#1')
    work_car = WorkCar(60, 'yellow', 'work_car_#1')
    police_car = PoliceCar(110, 'blue', 'police_car_#1')

    cars = (town_car, sport_car, work_car, police_car)

    for car in cars:
        test_run(car)
