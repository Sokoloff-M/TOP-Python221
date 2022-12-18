"""Демонстратор прототипа: ссылочная зависимость"""
from copy import deepcopy
from dataclasses import dataclass

@dataclass()
class Address:
    city: str
    street: str
    building: str
    room: str
    def __str__(self):
        return f'{self.city}, {self.street},{self.building}-{self.room}'

@dataclass
class Person:
    name: str
    living_adress: Address

    def __str__(self):
        return f'{self.name} живет по адресу {self.living_adress}'



ivan = Person('Иван',Address('Екатеринбург','пр.Космонавтов','30б', '202'))
liza = deepcopy(ivan)
liza.name = 'Лиза'
liza.living_adress.room = '205'




print(ivan)
print(liza)
