# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.


class Complex:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        num_1 = self.num_1 + other.num_1
        num_2 = self.num_2 + other.num_2
        result = (num_1, str(num_2) + 'i')
        return str(result)

    def __mul__(self, other):
        num_1 = self.num_1 * other.num_1
        num_2 = self.num_2 * other.num_2
        result = (num_1, str(num_2) + 'i')
        return result


if __name__ == '__main__':

    a1 = Complex(2, 4)
    a2 = Complex(3, 5)

    print(a1 + a2)
    print(a1 * a2)

