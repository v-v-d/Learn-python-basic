# 5
# Реализовать класс Stationery (канцелярская принадлежность). Определить
# в нем атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов метод должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Start drawing.'


class Pen(Stationery):
    def draw(self):
        return f'The {self.title} is drawing now.'


class Pencil(Stationery):
    def draw(self):
        return f'Start drawing by {self.title}.'


class Handle(Stationery):
    def draw(self):
        return f'Your {self.title} draw something now.'


if __name__ == '__main__':
    pen = Pen('pen')
    pencil = Pencil('pencil')
    handle = Handle('handle')

    stationery = (pen, pencil, handle)

    for item in stationery:
        print(item.draw())
