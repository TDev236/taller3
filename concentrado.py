class Concentrado:
    def __init__(self, nombre, precio, calorias, registro_invima):
        self.__nombre = nombre
        self.__precio = precio
        self.__calorias = calorias
        self.__registro_invima = registro_invima # sin getter
        
    def dar_informacion(self):
        return f"{self.__nombre} (${self.__precio})"

    def calcular_rentabilidad(self):
        return round(self.__precio / self.__calorias, 2)