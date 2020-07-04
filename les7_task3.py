"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы
методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
 аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""

class Cell:
    def __init__(self, numb):
        self.numb_cells = numb

    def __str__(self):
        return f'Количество клеток: {str(self.numb_cells)}'

    def __add__(self, other):
        return Cell(self.numb_cells + other.numb_cells)

    def __sub__(self, other):
        if self.numb_cells - other.numb_cells > 0:
            return Cell(self.numb_cells - other.numb_cells)
        return f'Невозможно, исходных клеток меньше'

    def __mul__(self, other):
        return Cell(self.numb_cells * other.numb_cells)

    def __truediv__(self, other):
        return Cell(int(self.numb_cells/other.numb_cells))

    def make_order(self, numb_columb):
        return '\n'.join(['*' * numb_columb for _ in range (self.numb_cells // numb_columb)]) + '\n' + '*' * (self.numb_cells % numb_columb)

c1 = Cell(10)
c2 = Cell(17)

print(c1)
print(c2)

c3 = c1+c2
c4 = c1 - c2
c5 = c2/c1

print (c1+c2)

print (c3.make_order(5))
print (c4)
print (c5)

c6 = c3*c1
print(c6.make_order(20))


