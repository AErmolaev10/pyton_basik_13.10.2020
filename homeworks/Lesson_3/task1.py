"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division():
    """ Функция деления 2х чисел """
    try:
        a = float(input('Введите число которое необходимо поделить'))
        b = float(input('Введите число на которое необходимо поделить'))
    except ValueError:
        return 'Нужно вводить числа!'
    try:
        c = a / b
    except ValueError:
        return 'Нужно вводить числа!'
    except ZeroDivisionError:
        return 'Делить на ноль нельзя'
    return c


print(division())
