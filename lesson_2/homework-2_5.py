'''
Реализовать структуру «Рейтинг», представляющую собой
не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться
после них.
'''

my_list = [7, 5, 3, 3, 2]
print("Пустая строка для завершения ввода")
print(f"Рейтинг - {my_list}")
while True:
    my_str = input("Введите элемент рейтинга ")
    if not my_str.isdigit():
        break
    my_int = int(my_str)
    my_list.append(my_int)
    my_list.sort(reverse=True)
    print(f"текущий список - {my_list}")
