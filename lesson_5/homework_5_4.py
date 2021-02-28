'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные. При этом английские
числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []

with open('hw54.txt', 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        el = line.split(' — ')
        my_list.append(f'{translate[el[0]]} — {el[1]}')

with open('hw54_new.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(my_list)
