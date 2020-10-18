"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

season_list = ['зима', 'весна', 'лето', 'осень']

month = int(input('Введите месяц в виде целого числа от 1 до 12, мы покажем время года'))

if month == 1 or month == 2 or month == 12:
    print(season_list[0])
elif month == 3 or month == 4 or month == 5:
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_list[2])
elif month == 9 or month == 10 or month == 11:
    print(season_list[3])
else:
    print('Вы ввели неправильное значение')

season_dict = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8.), 'осень': (9, 10, 11)}

month = int(input('Введите месяц в виде целого числа от 1 до 12, мы покажем время года'))
for key in season_dict.keys():
    if month in season_dict[key]:
        print(key)




