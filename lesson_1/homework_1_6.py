'''
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
'''

start = int(input("Пробежка в первый день: "))
end = int(input("Лимит: "))
count = 1
print(f"{count}-й день: {start:.2f}")
while start <= end:
    count += 1
    start = start + start * 0.1
    print(f"{count}-й день: {start:.2f}")
print(f"На {count}-й день спортсмен достиг результата — не менее {end} км")