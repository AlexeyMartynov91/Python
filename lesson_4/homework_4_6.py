'''
Реализовать два небольших скрипта:
*   бесконечный итератор, генерирующий целые числа,
начиная с указанного,
*   бесконечный итератор, повторяющий элементы
некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle()
модуля itertools.
'''

from itertools import count
from itertools import cycle


def my_generate_count(my_count=0):
    for el in count(my_count):
        if el == 20:
            break
        yield el


def my_generate_cycle(my_iterable, my_count):
    for el in cycle(my_iterable):
        if my_count > 0:
            my_count -= 1
            yield el
        else:
            break


my_gen = my_generate_count(6)
print(list(my_gen))

my_list = "QWERTY"
my_gen = my_generate_cycle(my_list, 10)
print(list(my_gen))
