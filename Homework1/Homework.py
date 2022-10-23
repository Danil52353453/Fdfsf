# Задание 1.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
# который должен принимать данные (список списков) для формирования матрицы.
#[[], [], []]
# Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add()__ для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
# Пример:
# 1 2 3
# 4 5 6
# 7 8 9
# 1 2 3
# 4 5 6
# 7 8 9
# Сумма матриц:
# 2 4 6
# 8 10 12
# 14 16 18


import copy

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str,self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):                                    
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


lst1 = [[1,2,4],[3,4,5],[5,6,6]]
lst2 = [[35,21,11],[13,14,43],[12,3,2]]
m = Matrix(lst1)
s = Matrix(lst2)
print(m)
print(s)
z = m + s
print("Сумма матриц:")
print(z)
