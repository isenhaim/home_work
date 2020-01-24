# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('text.txt') as file:
    lists = [i for i in file]
    salary_list = []

    k = 0
    for i in lists:
        salary = float(lists[k].split()[1])
        salary_list.append(salary)
        sum_sal = 0

    for j in salary_list:
        sum_sal += j
        if salary > 20000:
            print(f'З/П выше 20к у сотрудника: {lists[k].split()[0]} ({lists[k].split()[1]})')
        k += 1

    print(f'Средняя ЗП сотрудника: {int(sum_sal / len(lists))}')
