# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_second = int(input('Введите кол-во секунд для конвертации: '))

return_hrs = int(user_second / 3600)
return_min = int((user_second % 3600) / 60)
return_sec = int((user_second % 3600) % 60)

print('{:02}:{:02}:{:02}'.format(return_hrs, return_min, return_sec))
