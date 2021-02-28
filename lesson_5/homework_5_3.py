'''
Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
'''

my_file = open('hw53.txt', 'r', encoding='utf-8')
with my_file as my_file:
    oklad = []
    sotrudik = []
    for line in my_file:
        el = line.split()
        if float(el[1]) < 20000:
            sotrudik.append(el[0])
        oklad.append(el[1])
sred_oklad = sum(map(float, oklad)) / len(oklad)
print(f'Оклад меньше 20 тыс. у {sotrudik}')
print(f'Cредний оклад {sred_oklad:.2f}')
my_file.close()
