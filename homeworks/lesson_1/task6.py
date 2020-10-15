"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения
параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

a = int(input('Введите Ваш результат в первый день, в км'))
b = int(input('Введите цель, в км'))
day: int = 1

while a <= b:
    a = a * 1.1
    day = day + 1

print('на ' + str(day) + '-й день спортсмен достиг результата — не менее ' + str(b) + ' км.')
