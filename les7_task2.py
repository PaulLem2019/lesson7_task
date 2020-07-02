"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class ClothesAbstract(ABC):
    def __init__(self, razmer):
        self.size_clothes = razmer

    @abstractmethod
    def coat(self, razmer):
        pass

    @abstractmethod
    def suit(self, rost):
        pass


class Clothes(ClothesAbstract):
    def __init__(self, razmer):
        self.size_clothes = razmer

    @property
    def coat(self):
        self.tkan = self.size_clothes / 6.5 + 0.5
        return f'Необходимое количество ткани для пальто {self.size_clothes} размера: {"%.2f" % (self.tkan)}'

    @property
    def suit(self):
        self.tkan = self.size_clothes/100 * 2 + 0.3
        return f'Необходимое количество ткани для костюма на рост {self.size_clothes} см: {"%.2f" % (self.tkan)}'


a = Clothes(50)

print (a.coat)

b = Clothes(170)

print (b.suit)
