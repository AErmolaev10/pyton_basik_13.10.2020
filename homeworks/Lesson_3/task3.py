"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов.
"""


def my_min(*args):
    """ Возвращает наименьший элемент """

    minim = args[0]
    for el in args:
        if el < minim:
            minim = el
    return minim


print(my_min(5, 3, 99, 2))


def my_func(a, b, c):
    """ Cумма 2х наибольших аргументов"""
    return a + b + c - min(a, b, c)


print(my_func(24, 13, 8))
