from sys import argv

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


def salary_staff(hour, rate, premium):
    hour, rate, premium = map(lambda x: int(x), [hour, rate, premium])
    salary = (hour * rate) + premium
    print(f'Заработная плата сотрудника: {salary}')


if __name__ == '__main__':

        script_name, hour, rate, premium = argv

        salary_staff(hour, rate, premium)