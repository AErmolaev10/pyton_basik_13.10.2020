"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
"""

from itertools import count

c = 0
for el in count(int(input('Введите стартовое число '))):
    if c > 10:
        break
    print(el)
    c += 1

