# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def user_info(fn, ln, birth_date='01.01.2001', residence='Russia', email='test@test.com', phone='+7-999-99-99'):
    return fn, ln, birth_date, residence, email, phone


print(user_info(ln='Petrov', fn='Vitaliy', phone='+7-111-11-11'))
