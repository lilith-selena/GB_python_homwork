#Урок 6. Объектно-ориентированное программирование
'''1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.'''
import time
class traffic_light:
    light = {'red':7, 'yellow':2, 'green':10}
    def __init__(self, color, time):
        self.color = color
        self.time = time

    def Light(self):
        for key in light.keys():
            time.sleep(self.light.values(key))
            print(key)

'''2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.'''

class Road:
    #Квадратный метр асфальта толщиной 5 см весит 125 кг. В среднем один сантиметр - это 25 кг. =>1см асфальта 2500 кгна метр.кубический
    #или 2,5 т. на м.куб.
    density = 2.5

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_mass(self):
      print(f'требуется {self.width * self.length * Road.density} тон асфальта')

road = Road(500, 20)
road.calc_mass()

'''3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
и дохода с учётом премии (get_total_income); проверить работу примера на реальных данных: 
создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.'''

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return (f' позиция {self.position} \n имя {self.name}\n фамилия {self.surname}')

    def get_total_income(self):
        return (f'\n оклад = {self._income["wage"]} \n премия = { self._income["bonus"]} \n итого: {self._income["wage"] + self._income["bonus"]}')


p = Position('Николай', 'Николаев','IT', '45000', '5000')
print(p.get_full_name(), p.get_total_income())

'''4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
  остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(shelf):
        print("машина поехала")

    def stop(self):
        print("машина остановилась")

    def turn(self, direction):
        self.direction = direction
        if self.direction == 'лево':
            print('машина повернула на лево')
        else:
            print('машина повернула на право')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if self.speed > 60:
            print('Превышение скорости!')
        print(f'Текущая скорость {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        print(f'Текущая скорость {self.speed} км/ч')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if self.speed > 40:
            print('Превышение скорости!')
        print(f'Текущая скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        print(f'Текущая скорость {self.speed} км/ч')


this_car = WorkCar(100, 'белая', 'не разбираюсь', False)
this_car.go()
this_car.show_speed(40)
this_car.turn('направо')
this_car.stop()
print()

'''5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки \n{self.title}'


class Pen(Stationery):
    def draw(self):
        return f'нарисуем линию {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'выполним штриховку {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'закрасим {self.title}'

stationary = Stationery ('КЛАСС: \nканцелярские принадлежности')
print(stationary.draw())
pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())