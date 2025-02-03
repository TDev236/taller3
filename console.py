from guarderia import Guarderia
from perro import Perro
from concentrado import Concentrado

guarderia_1 = Guarderia("canine Zen")

perro_1 = Perro("Zeus", "Rottweiler", 45.8, 3)
perro_2 = Perro("Nala", "Golden R." , 8.5, 0)
perro_3 = Perro("Atila", "Alabai", 58.9, 5)

concentrado_1 = Concentrado("Dog Chow", 34.500, 1342, "564INV")
concentrado_2 = Concentrado("Purina", 54.400, 2300, "321INV")
concentrado_3 = Concentrado("Royal Canine", 120.432, 3400, "987INV")

guarderia_1.agregar_concentrado(concentrado_1)
guarderia_1.agregar_concentrado(concentrado_2)
guarderia_1.agregar_concentrado(concentrado_3)


perro_2.asignar_concentrado(concentrado_1)

print(perro_2.dar_informacion())
