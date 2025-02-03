from concentrado import Concentrado
from perro import Perro


class Guarderia:
    def __init__(self, nombre):
        self.__nombre= nombre
        self.__concentrados = []
        
    def agregar_concentrado(self, concentrado):
        self.__concentrados.append(concentrado)
        


concentrado_1 = Concentrado("DogChow", 50000, 1900, "432INV")
concentrado_2 = Concentrado("Pedigree", 55000, 2300, "432INV")
concentrado_3 = Concentrado("Purina", 60500, 3060, "432INV")

