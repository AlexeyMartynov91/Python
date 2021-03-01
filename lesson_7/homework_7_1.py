'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку
конструктора класса (метод __init__()), который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для
вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации
операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять
поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
'''


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):

        result = []
        for sublist in zip(self.matrix, other.matrix):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            result.append(temp)
        return result



my_matrix1 = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]])

my_matrix2 = Matrix([[5, 12, 19],
                    [4, 13, 17],
                    [9, 40, 21]])

print(f'Матрица 1\n{my_matrix1}')
print(f'Матрица 2\n{my_matrix2}')

my_matrix = Matrix(my_matrix1 + my_matrix2)

print(f' Сумма матриц\n{my_matrix}')