"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
должен контролировать типы данных элементов списка
"""


class My_class(Exception):
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        try:
            val = int(input('Введите числа'))
            self.my_list.append(val)
            return f'Текущий список - {self.my_list}'
        except ValueError:
            return f"Недопустимое значение - строка или булево"


try_except = My_class(132)
print(try_except.my_input())
