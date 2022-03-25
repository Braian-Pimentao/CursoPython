from random import *


def lanzar_moneda():
    return choice(["Cara", "Cruz"])


def probar_suerte(moneda, lista_numero):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numero


print(probar_suerte(lanzar_moneda(),[1, 2, 3, 4, 6]))
print(sorted([2,1]))
