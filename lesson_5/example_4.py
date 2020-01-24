# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_2.txt') as file:
    for i in file:
        file_write = open('text_rus.txt', 'a')
        word = translate.get(str(i.split()[0]))
        string = (word + ' ' + i.split()[1] + ' ' + i.split()[2] + '\n')
        file_write.write(string)