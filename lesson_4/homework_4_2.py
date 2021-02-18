'''
Представлен список чисел. Необходимо вывести элементы
исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить
в виде списка. Для формирования списка использовать генератор.
'''

from random import randrange

my_list = [randrange(0, 30, 3) for el in range(1, 10)]
my_list_new = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_list_new}')
