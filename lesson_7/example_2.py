# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.

# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, title, param):
        self.param = param
        self.title = title

    # Метод который должен быть во всех дочерних классах.
    @abstractmethod
    def calculation(self, param):
        pass

    def __radd__(self, other):
        return self.calculation(self.param) + other

    @property
    def params(self):
        return f'Параметры {self.title}: {self.param} m.'


class Coat(Clothes):

    def calculation(self, param):
        return float('{:.4f}'.format(param / 6.5 + 0.5))


class Costume(Clothes):

    def calculation(self, param):
        return float('{:.4f}'.format(2 * param + 0.3))


if __name__ == '__main__':

    class_1 = Coat('пальто', 6)
    class_2 = Costume('костюм', 8)

    print(f'Общее количество ткани: {float("{:.4f}".format(class_1 + class_2))}')

    # Добавил для проверки
    print(f'Тест: {(class_1.calculation(6) + class_2.calculation(8)) == (class_2 + class_1)}')

    # Применение @property притянуто за уши.
    print(class_1.params)
