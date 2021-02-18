'''
Создать текстовый файл (не программно), сохранить
в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

my_file = open('hw52.txt', 'r', encoding='utf-8')
with my_file as file_obj:
    letters = 0
    count = 0
    for line in file_obj:
        letters = len(line) - 1
        count += 1
        print(f"{letters} символов в строке.   {line[:-1]}")
    print(f"{count} количество строк в файле.")
my_file.close()
