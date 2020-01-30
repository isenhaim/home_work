# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class Warehouse:
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.inventory = {}

    # Использовал перегрузку оператора сложения для добавления на склад экземпляров оргтехники
    def __add__(self, other):
        if self.capacity > 0:
            self.capacity -= other.size
            other.in_ware = True
            other.location = self.location
        else:
            print('Склад переполнен')

    # Использовал перегрузку оператора вычитания для извлечения со склада экземпляров оргтехники
    def __sub__(self, other):
        if self.capacity > 0:
            self.capacity += other.size
            other.in_ware = False
            other.location = ''
        else:
            print('На складе нет оборудования')

    def acceptance(self, other, count):
        if isinstance(count, int):
            value = {other.title: count}
            self.inventory.update(value)
        else:
            print('Количество укажите числом')

    def shipment(self, other, count):
        if isinstance(count, int):
            count = self.inventory.get(other.title) - count
            if count > 0:
                value = {other.title: count}
                self.inventory.update(value)
            else:
                print(f'Такого количества {other.title} на складе нет')
        else:
            print('Количество укажите числом')


class Appliances:
    """Класс оргтехника, содержит атрибуты общие для оргтехники"""
    def __init__(self, title, in_ware, size):
        # Наименование
        self.title = title
        # Атрибут отражающий нахождение техники на складе или вне.
        self.in_ware = in_ware
        # Гео-позиция расположения техники
        self.location = None
        # Кол-во мест занимаемых техникой в случае размещения на складе
        self.size = size

    # Метод отвечающий за передачу экземпляра в любое место вне склада,
    # требует указания конечной локации
    def shipment(self, location):
        self.location = location
        self.in_ware = False


class Printer(Appliances):
    def __init__(self, title, in_ware, size):
        super().__init__(title, in_ware, size)
        self.printing = True


class Scanner(Appliances):
    def __init__(self, title, in_ware, size):
        super().__init__(title, in_ware, size)
        self.scanning = True


class Xerox(Appliances):
    def __init__(self, title, in_ware, size):
        super().__init__(title, in_ware, size)
        self.scanning = True


if __name__ == '__main__':

    ware = Warehouse('RUS', 100)
    printer_1 = Printer('HP', False, 2)
    printer_2 = Printer('XER', False, 2)

    ware + printer_1
    ware + printer_2

    ware - printer_2

    ware.acceptance(printer_1, 3)
    ware.acceptance(printer_2, 5)

    ware.shipment(printer_1, 2)

    print(ware.inventory)
    print(printer_1.__dict__)
    print(printer_2.__dict__)
    print(ware.__dict__)



