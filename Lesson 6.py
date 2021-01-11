"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт."""
print("Task № 1 ")
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    @staticmethod
    def running():
        i = 0
        while i < 3:
            print(f'Режим светофора: \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: 
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. 
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т"""
print("Task № 2 ")


class Road:

    def __init__(self, length, width, weight, height):
        self._length = length
        self._width = width
        self.weight = weight
        self.height = height

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия дороги асфальтом, нужно: {round(asphalt_mass)} тонн асфальта.')


r = Road(5000, 20, 25, 5)
r.asphalt_mass()
"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, 
вызвать методы экземпляров)."""
print("Task № 3 ")


class Worker:
    _first_name: str
    _second_name: str
    _position: int
    _wade: int
    _bonus: int

    def __init__(self, first_name, second_name, position, wage, bonus):
        self.first_name = first_name
        self.second_name = second_name
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, first_name, second_name, position, wage, bonus):
        super().__init__(first_name, second_name, position, wage, bonus)

    def get_full_name(self):
        return f"Сотрудник: {self.first_name} {self.second_name};"

    def get_total_income(self):
        return f'Доход: {self._income["wage"] + self._income["bonus"]} руб.'


p = Position('Евлампий', 'Дормидонт', 'ИБ', '50000', '100000')
print(p.get_full_name(), p.get_total_income())

"""4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
должно выводиться сообщение о превышении скорости."""
"""5. Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат."""
print("Task № 4 и № 5 ")


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'\nМашина {self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула на {direction}.'

    def show_speed(self):
        return f'\nТекущая скорость автомобиля: {self.speed} км/ч.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость автомобиля больше 60 км/ч !!! Текущая скорость: {self.speed} км/ч'
        else:
            return f'\n{self.name} Текущая скорость: {self.speed} км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость автомобиля больше 40 км/ч !!! Текущая скорость: {self.speed} км/ч'
        else:
            return f'\n{self.name} Текущая скорость: {self.speed} км/ч'


class PoliceCar(Car):
    pass


town = TownCar(80, 'красный', 'AUDI', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('Лево'), town.turn('Право'), town.stop())

sport = SportCar(275, 'серый', 'Jaguar F-Type', True)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('Лево'), sport.stop())

work = WorkCar(41, 'желтый', 'КАМАЗ', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('Право'), work.stop())

police = PoliceCar(150, 'черный', 'BMW', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('Право'), police.stop())
"""6. Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” 
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов метод должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""
print("Task № 6 ")


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки: {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки: {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки: {self.title}'


pen = Pen('ручка')
print(pen.draw())
pencil = Pencil('карандаш')
print(pencil.draw())
handle = Handle('маркер')
print(handle.draw())
