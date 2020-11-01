"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} go'

    def stop(self):
        return f'{self.name} stop'

    def turn(self, direction):
        return f'{self.name} turn {direction}'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed <= 60:
            return self.speed
        else:
            return 'the speed limit is exceeded'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed <= 40:
            return self.speed
        else:
            return 'the speed limit is exceeded'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


kia = TownCar(70, 'red', 'Rio', True)
audi = SportCar(120, 'black', 'R-8', True)
volvo = WorkCar(80, 'grey', 'XC-90', True)
ford = PoliceCar(100, 'white', 'Focus', True)

print(kia.show_speed())
print(audi.speed)
print(volvo.go())
print(ford.stop())
print(kia.is_police)
print(audi.name)
print(volvo.turn('left'))
print(ford.show_speed())
