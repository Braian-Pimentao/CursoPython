from collections import namedtuple

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])

ariel = Persona('Ariel', 1.78, 98)

print(ariel)


class Personaclase:
    def __init__(self):
        nombre = "Ariel"
        altura =1.78
        peso = 98


Persona2 = Personaclase()

print(type(Persona2))
print(type(ariel))