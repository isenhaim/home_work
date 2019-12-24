# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (
# соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете
# на одного сотрудника.

cost = int(input('Введите издержки фирмы: '))
profit = int(input('Введите доход фирмы: '))

if profit > cost:
    print('Фирма имеет прибыль')

    profitability = profit / (profit - cost)
    print(f'Рентабельность: {profitability}')

    employee = int(input('Введите кол-во Ваших сотрудников: '))
    profit_emp = profit / employee
    print(f'Прибыль фирмы в расчете на одного сотрудника {profit_emp}')
else:
    print('Фирма терпит убытки')
