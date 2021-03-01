'''
Реализовать проект расчета суммарного расхода ткани на
производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на
практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике
работу декоратора @property.
'''
from abc import ABC, abstractmethod


class Сlothes(ABC):
    _clothes = []

    def __init__(self, name, param):
        self.name = name
        self.param = param
        self.required = 0
        self._clothes.append(self)

    @abstractmethod
    def fabric_consumption(self):
        self.required = self.param
        return self.required

    @property
    def full_consumption(self):
        return str(f'Необходимо ткани: {round(sum([el.required for el in self._clothes]), 2)}')


class Coat(Сlothes):
    def __init__(self, name, param):
        super().__init__(name, param)

    @property
    def fabric_consumption(self):
        self.required = round(self.param / 6.5 + 0.5, 2)
        return self.required


class Сostume(Сlothes):
    def __init__(self, name, param):
        super().__init__(name, param)

    @property
    def fabric_consumption(self):
        self.required = round(self.param * 2 + 0.3, 2)
        return self.required


my_coat = Coat('Пальто 1', 2)
my_costume = Сostume('Куртка 1', 3)

print(f'Ткани для пальто "{my_coat.name}": {my_coat.fabric_consumption}')
print(f'Ткани для костюма "{my_costume.name}": {my_costume.fabric_consumption}')
print(my_coat.full_consumption)
