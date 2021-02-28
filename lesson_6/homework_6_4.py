'''
Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = []

    def go(self, speed):
        self.speed = speed
        print(f'Машина "{self.name}" начала движение со скроростью {speed}')

    def stop(self):
        self.speed = 0
        print(f'Машина "{self.name}" остановилась. Маршрут {self.direction}')

    def turn(self, direction):
        self.direction.append(direction)
        print(f'Машина "{self.name}" повернула {direction}')

    def show_speed(self):
        print(f'Машина "{self.name}" движется со скростью {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, speedmode=60):
        self.speedmode = speedmode
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(f'Машина "{self.name}" движется со скростью {self.speed}')

        if self.speed > self.speedmode:
            print(f'Машина "{self.name}" превысила скорость {self.speedmode}')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name, speedmode=40):
        self.speedmode = speedmode
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(f'Машина "{self.name}" движется со скростью {self.speed}')

        if self.speed > self.speedmode:
            print(f'Машина "{self.name}" превысила скорость {self.speedmode}')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


my_sportcar = SportCar(100, 'Красный', 'Audi')
my_towncar = TownCar(60, 'Белый', 'Oka')
my_workcar = WorkCar(70, 'Черный', 'Lada')
my_policecar = PoliceCar(110, 'Голубой', 'Ford')

my_cars = [my_sportcar, my_towncar, my_workcar, my_policecar]

for my_car in my_cars:
    print('#######################################')
    print(f"Машина: '{my_car.name}'")
    print(f"Цвет: '{my_car.color}'")
    print(f"Полицейская: '{my_car.is_police}'")
    print(f"Максимальная скорость: '{my_car.speed}'")

    my_car.go(30)
    my_car.show_speed()
    my_car.turn('Лево')
    my_car.turn('Право')
    my_car.go(60)
    my_car.show_speed()
    my_car.turn('Право')
    my_car.go(80)
    my_car.show_speed()
    my_car.stop()
    print('#######################################')
