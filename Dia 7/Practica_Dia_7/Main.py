import Cliente
from random import *
import re


cliente1 = Cliente.Cliente("Pepito", "Grillo", "546546546465456", 500000)


def crear_cliente():
    pass


def comprobar_texto(texto):
    while True:
        x = re.findall("'r[^a-zA-Z]'", texto)
        if x is None:
            print("No debe de contener numeros ni caracteres especiales,")
            texto = input("Vuelve a intentarlo: ")
        else:
            return texto


nombre = comprobar_texto(input("Dime tu nombre: "))

print(nombre)