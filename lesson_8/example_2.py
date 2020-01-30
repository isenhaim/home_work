# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ZeroError(Exception):
    def __init__(self, text):
        self.txt = text


def division(num_1, num_2):
    try:
        num_1, num_2 = float(num_1), float(num_2)
        if float(num_2) == 0:
            raise ZeroError('На ноль делить нельзя!')
        print(num_1 / num_2)
    except ValueError:
        print('Введите только числа')

    except ZeroError as ze:
        print(ze)


if __name__ == '__main__':

    nums_1 = input('Введите 1 число для деления: ')
    nums_2 = input('Введите 2 число для деления: ')

    division(nums_1, nums_2)
