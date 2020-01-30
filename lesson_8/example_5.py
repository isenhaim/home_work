# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


class Warehouse:
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.inventory = {}

    def acceptance(self, other, count):
        value = {other.title: count}
        self.inventory.update(value)


class Appliances:
    """Класс оргтехника, содержит атрибуты общие для оргтехники"""
    def __init__(self, title, size, in_ware=False):
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
        self.copying = True


if __name__ == '__main__':

    ware = Warehouse('RUS', 100)
    printer_1 = Printer('HP LaserJet', False, 2)
    xerox_1 = Xerox('Xerox 2135', False, 2)

    print(printer_1.title)

    ware.acceptance(printer_1, 3)
    ware.acceptance(xerox_1, '3')

    print(ware.inventory)

