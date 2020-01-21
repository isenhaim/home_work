# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# Записываем ряд чисел от 0 до 7
file = open('text_num.txt', 'w')

for i in range(0, 8):
    file.write(str(i) + ' ')

file.close()

# Читаем числа из файла и суммируем
file = open('text_num.txt')
list_num = file.read().split()

num_file = 0
for i in list_num:
    num_file = num_file + int(i)

print(f'Сумма чисел в файле равна: {num_file}')

file.close()
