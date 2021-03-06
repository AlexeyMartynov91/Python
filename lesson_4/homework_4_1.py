'''
Реализовать скрипт, в котором должна быть предусмотрена
 функция расчета заработной платы сотрудника. В расчете
 необходимо использовать формулу:
 (выработка в часах*ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо
 запускать скрипт с параметрами.
'''

from sys import argv

virabotka, stavka, premya = argv
try:
    result = (float(virabotka) * float(stavka)) + float(premya)
    print(f'заработная плата сотрудника  {result}')
except ValueError:
    print('Введены не корретные данные')
