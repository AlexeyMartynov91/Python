"""
Создать (не программно) текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности,
выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой
компании, а также среднюю прибыль. Если фирма получила убытки,
в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила
убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""

from json import dumps

results = [{}, {}]

with open("hw57.txt", 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        name, ownership, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)

results[1]['average_profit'] = round(
    sum(profit for ownership, profit in results[0].items() if profit > 0) / len(results[0])
    )

with open("hw57.json", "w", encoding='utf-8') as file_obj:
    file_obj.write(dumps(results))
