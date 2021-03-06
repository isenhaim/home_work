# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.

# Функция должна вызываться следующим образом: for el in fact(n).

# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def fact(n):
    # Функция расчета факториала
    if n == 0:
        return 1
    return fact(n - 1) * n


def gen(n):
    # Функция генератор
    my_list = range(1, n + 1)
    for i in my_list:
        yield fact(i)


# Цикл
c = 0

for el in gen(6):
    c += 1
    if c > 15:
        break
    print(el)
