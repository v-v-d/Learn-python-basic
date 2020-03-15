# 1
# Создать класс TrafficLight (светофор) и определить у него один атрибут
# color (цвет) и метод running (запуск). Атрибут реализовать как
# приватный. В рамках метода реализовать переключение светофора в
# режимы: красный, желтый, зеленый. Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.
from time import sleep


class TrafficLight:
    def __init__(self, red_interval=7, yellow_interval=2, green_interval=15):
        self.__color = None
        self.red_interval = red_interval
        self.yellow_interval = yellow_interval
        self.green_interval = green_interval

    def run(self):
        while True:
            for color, interval in self._get_color_interval_resolver().items():
                self._set_color(color)
                self._interval_print_color(interval)

    def _get_color_interval_resolver(self):
        return {
            'red': self.red_interval,
            'yellow': self.yellow_interval,
            'green': self.green_interval,
        }

    def _set_color(self, color):
        self.__color = color

    def _interval_print_color(self, interval):
        print(self.__color)
        sleep(interval)


if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.run()
