'''
Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

my_file = open('hw51.txt', 'w', encoding='utf-8')
print('Введите текст')
my_line = True
while True:
    line = input()
    if not line:
        break
    my_file.writelines(f'{line}\n')
my_file.close()
