'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''


def def_func(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])


lambda_func = lambda name, surname, year, city, email, phone: ' '.join([name, surname, year, city, email, phone])

print(def_func(phone='+7(901)-234-56-78', surname="Martynov", name="Alexey", year='1991', city='Ekaterinburg',
               email='spamlexa@mail.ru'))
print(lambda_func(phone='+7(901)-234-56-78', surname="Martynov", name="Alexey", year='1991', city='Ekaterinburg',
                  email='spamlexa@mail.ru'))
