# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

from random import randint
from itertools import product

class Matrix:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.data = [[None for _ in range(column)] for _ in range(row)]

    def len(self):
        print('Число строк ', len(self.data))
        print('Число столбцов ', len(self.data[0]))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.row!r}, {self.column!r})'

    def __str__(self):
        return "\n".join(map(str, self.data))

    def add(self, add_list):
        values = iter(add_list)

        indices = product(range(self.row), range(self.column))

        for (i, j), value in zip(indices, values):
            self.data[i][j] = value

        return values   
    
    def replace(self,row_index,column_index,value):
        
        self.data[row_index][column_index] = value


my_matrix = Matrix(10,10)
overflow = my_matrix.add([randint(1,9) for i in range(100)])

print(my_matrix)
my_matrix.len()
my_matrix.replace(3,3,63)
print(my_matrix)

