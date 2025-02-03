class Perro:
    def __init__(self,nombre, raza, peso, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__peso = peso
        self.__edad = edad
        self.__concentrado = None #variable concentrado
        
    def ladrar(self):
        return "!Guau, guau¡"
    
    def modificar_peso(self, nuevo_peso):
        self.__peso = nuevo_peso
    
    def dar_nombre(self):
        return self.__nombre
    
    def dar_informacion(self):
        return self.__nombre + "(" + self.__raza + "):"+ str(self.__peso) + "/"+str(self.__edad)
    
    def asignar_concentrado(self, concentrado):
        self.__concentrado = concentrado
    
    def dar_concentrado(self):
        if self.__concentrado:
            return self.__concentrado.dar_informacion()
        return "No le han asignado concentrado"
    