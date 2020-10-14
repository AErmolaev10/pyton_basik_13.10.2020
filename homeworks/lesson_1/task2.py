"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

hour_include_seconds = 3600
minute_include_seconds = 60

seconds = int(input('Введите количество секунд, мы переведём их в формат чч:мм:cc.\n>>>'))

hours = seconds // hour_include_seconds
minute = (seconds % hour_include_seconds) // minute_include_seconds
sec = (seconds % hour_include_seconds) % minute_include_seconds

print(hours,minute,sec, sep=':')
