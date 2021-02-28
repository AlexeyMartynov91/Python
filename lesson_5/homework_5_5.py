'''
Создать (программно) текстовый файл, записать в него программно
набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randrange

with open('hw55.txt', 'w', encoding='utf-8') as file_obj:
    line = ' '.join(map(str, [randrange(0, 30, 1) for el in range(1, 10)]))
    print(line)
    file_obj.writelines(line)

with open('hw55.txt', 'r', encoding='utf-8') as file_obj:
    my_sum = 0
    for line in file_obj:
        my_sum = my_sum + sum([int(el) for el in line.split()])

print(f'Сумма чисел = {my_sum}')
