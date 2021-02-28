'''
    Необходимо создать (не программно) текстовый файл, где
    каждая строка описывает учебный предмет и наличие лекционных,
    практических и лабораторных занятий по этому предмету и их
    количество. Важно, чтобы для каждого предмета не обязательно
    были все типы занятий. Сформировать словарь, содержащий
    название предмета и общее количество занятий по нему.
    Вывести словарь на экран.
'''


def my_strtoint(str):
    my_int = ''
    for el in str:
        if el.isdigit():
            my_int += el
        else:
            break
    return 0 if my_int == '' else int(my_int)


subj = {}
with open('hw56.txt', 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        subject, lecture, practice, lab = line.split()
        subj[subject] = my_strtoint(lecture) + my_strtoint(practice) + my_strtoint(lab)

print(f'Общее количество часов по предмету\n{subj}')
