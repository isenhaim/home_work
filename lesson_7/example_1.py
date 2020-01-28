# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод _init_()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода _str_() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода _add_() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:

    def __init__(self, list_matrix):
        self.list_matrix = [([j for j in i]) for i in list_matrix]

    def __str__(self):
        self.list_return = str(self.list_matrix)
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in self.list_matrix])

    def __add__(self, other):
        result = []
        num = []
        try:
            for i in range(len(self.list_matrix)):
                for z in range(len(self.list_matrix[0])):
                    amount_matrix = other.list_matrix[i][z] + self.list_matrix[i][z]
                    num.append(amount_matrix)

                    if len(num) == len(self.list_matrix):
                        result.append(num)
                        # print(num)
                        num = []

            return '\n'.join(['\t'.join([str(j) for j in i]) for i in result])
        except IndexError:
            return 'Решения не существует'


if __name__ == '__main__':

    matrix_1 = Matrix([[1, 0, 0], [1, 0, 1], [4, 0, 0]])
    matrix_2 = Matrix([[0, 1, 0], [2, 0, 1], [1, 2, 0]])

    print(matrix_1)
    print('-' * 10)

    print(matrix_2)
    print('*' * 10)

    print(matrix_1 + matrix_2)
