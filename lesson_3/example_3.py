# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.


def my_func(num_a, num_b, num_c):
    my_list = [num_a, num_b, num_c]
    my_list.remove(min(my_list))
    print(my_list[0] + my_list[1])


my_func(12, 12, 78)
