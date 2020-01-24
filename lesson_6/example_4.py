# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed=60, color='Black', name='My_Car', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч')
        if self.speed > 60:
            print('Внимание корость превышена!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч')
        if self.speed > 60:
            print('Внимание корость превышена!')


class PoliceCar(Car):
    pass


if __name__ == '__main__':

    town_car = TownCar(80, 'Blue', 'Smart')
    print(town_car.speed, town_car.color, town_car.name, town_car.is_police)
    town_car.show_speed()
    print('-' * 100)

    sport_car = SportCar(250, 'Red', 'Ferrari')
    print(sport_car.speed, sport_car.color, sport_car.name, sport_car.is_police)
    sport_car.show_speed()
    print('-' * 100)

    work_car = WorkCar(45, 'Yellow', 'CAT')
    print(work_car.speed, work_car.color, work_car.name, work_car.is_police)
    work_car.show_speed()
    print('-' * 100)

    police_car = PoliceCar(90, 'White-Blue', 'Porsche', True)
    print(police_car.speed, police_car.color, police_car.name, police_car.is_police)
    police_car.show_speed()
