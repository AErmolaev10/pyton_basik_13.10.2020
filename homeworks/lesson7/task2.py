"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:
    cloth = []

    def __init__(self, v=0, h=0):
        self.v = v
        self.h = h

    @property
    def get_sq_full(self):
        return f'Общий расход ткани \n {Clothes.cloth}'

    def __str__(self):
        return f'Общий расход ткани {self.square_c}'


class Coat(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_c = round(self.v / 6.5 + 0.5)
        Clothes.cloth.append(self.square_c)


class Jacket(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_j = round(self.h * 2 + 0.3)
        Clothes.cloth.append(self.square_j)

    def __str__(self):
        return f'Расход ткани на костюм {self.square_j}'


coat = Coat(36, 0)
coat2 = Coat(44, 0)
jacket = Jacket(0, 166)
jacket2 = Jacket(0, 177)
print(coat)
print(jacket)
print(coat2)
print(jacket2)
print(f'Общий расход ткани {sum(Clothes.cloth)}')


