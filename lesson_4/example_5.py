from functools import reduce
# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


def my_func(num_1, num_2):
    return num_1 * num_2


gen_list = [i for i in range(1, 1001) if i % 2 == 0]

result = reduce(my_func, gen_list)

print(result)

