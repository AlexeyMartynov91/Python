'''
Пользователь вводит строку из нескольких слов, разделённых
пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.
'''
import timeit

print("Введите строку")
my_str = input()
my_word = my_str.split()
num = 1
for el in my_word:
    print(f" {num} {el[0:10]}")
    num += 1
