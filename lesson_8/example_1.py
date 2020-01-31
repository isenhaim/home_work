# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def convert_num(cls, date):
        cls.date = [int(i) for i in date.split('-')]
        return cls.date

    @staticmethod
    def validation_date(date):
        date = Date.convert_num(date)
        error = []
        if date[0] > 31:
            error.append('Некорекктное число месяца')
        if date[1] > 12:
            error.append('Некорректный месяц')
        if len(str(date[2])) > 4:
            error.append('Некорректный год')
        if len(error) == 0:
            error.append('Все ок')
        return error


if __name__ == '__main__':

    # Проверяем ошибку
    print(Date.validation_date('39-19-202000'))
    # Проверяем корректность
    print(Date.validation_date('29-12-2020'))
