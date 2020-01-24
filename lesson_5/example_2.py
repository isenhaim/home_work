# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

list_string = [i for i in open('text.txt', 'r')]
print(f'В файле {len(list_string)} строки')

check = 1
for i in list_string:
    print(f'В строке {check}: {len(i.split())} слова')
    check += 1
