"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, *args):
        self.lists = args
        # print (self.lists)

    def __str__(self):
        string = ''
        for iter in self.lists:
            # print (iter)
            for iter1 in iter:
                # print (iter1)
                string += '|'
                for iter2 in iter1:
                    string += str(iter2) + ' '
                string += '|\n'
            # string += '|'
        return f'Matrix is: \n{string}'

    def __add__(self, other):
        NumStr = len(self.lists[0])
        NumCol = len(other.lists[0])
        for i in range(NumStr):
            for j in range(NumCol):
                self.lists[0][i][j] = self.lists[0][i][j] + other.lists[0][i][j]
            Result = self.lists[0]
        return Matrix(Result)

m = Matrix([[10, 11, 12], [20, 21, 22], [30, 31, 32]])
m1 = Matrix([[0, 1, 2], [10, 11, 12], [20, 21, 22]])

print(m)
print(m1)
print(m + m1)
