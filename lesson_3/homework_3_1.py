'''
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
'''


def funcdelete(div1, div2):
    """Возвращает результат деления.

   Именованные параметры:
   div1 -- делимое
   div2 -- делитель

   """

    try:
        result = div1 / div2
    except ZeroDivisionError:
        return "Деление на ноль"
    except:
        return 'Ошибка в значениях'
    return result


print(funcdelete(1, 10))
print(funcdelete(1, '0'))
print(funcdelete(1, 0))
