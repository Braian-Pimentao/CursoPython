import re
from random import *

print("Vamos a jugar al ahorcado, yo elijo una palabra y tú me vas diciendo una letra, tienes 6 vidas")
vidas = 6
palabras = ["Ordenador", "Teclado", "Cargador", "Marvel", "Monitor", "Oficina", "Empresa"]

palabra_elegida = choice(palabras).lower()
palabra_oculta = re.sub('[A-Za-z]', "_", palabra_elegida)


def pedir_letra():
    while True:
        letra = input("Dime una letra: ")
        if validar_letra(letra):
            return comprobar_acierto(letra)


def validar_letra(letra):
    if letra.isalpha():
        if len(letra) == 1:
            return True
        else:
            print("Solo tienes que decir una letra.")
    else:
        print("Eso no es una letra.")

    return False


def comprobar_acierto(letra):
    indices = []
    for pos, char in enumerate(palabra_elegida):
        if char == letra:
            indices.append(pos)

    if len(indices) >= 1:
        print("Has Encontrado la letra")
        return cambiar_palabra_oculta(indices, letra)
    else:
        print("Has perdido una vida")
        return 1


def cambiar_palabra_oculta(indices, letra):
    lista = list(palabra_oculta)
    for n in range(len(indices)):
        lista[indices[n]] = letra

    return "".join(lista)


print(palabra_oculta)


while vidas > 0 and palabra_oculta != palabra_elegida:
    devuelto = pedir_letra()
    if type(devuelto) == int:
        vidas -= devuelto
        print(f"Te quedan {vidas} vidas")
    else:
        palabra_oculta = devuelto
        print(palabra_oculta)
if vidas == 0:
    print(f"Has perdido todas las vidas, la palabra oculta era {palabra_elegida}")
else:
    print("Enhorabuena, has acertado la palabra oculta")