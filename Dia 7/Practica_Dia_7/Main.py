import os
import random
from Cliente import *
import re



def crear_cliente():
    nombre = comprobar_texto(input("Dime tu nombre: "))
    apellido = comprobar_texto(input("Dime tu apellido: "))
    numero_cuenta = random.randint(100000000000000, 999999999999999)
    return Cliente(nombre, apellido, numero_cuenta)


def comprobar_numero(numero):
    while True:
        if str.isdigit(numero):
            return float(numero)
        else:
            print("No debe de contener números ni caracteres especiales,")
            numero = input("Vuelve a intentarlo: ")


def comprobar_texto(texto):
    while True:
        if re.search("[^a-zA-Z]", texto) is None:
            return texto
        else:
            print("No debe de contener números ni caracteres especiales,")
            texto = input("Vuelve a intentarlo: ")


def opciones():
    while True:
        listar_opciones()
        match comprobar_numero(input("Elige una opción: ")):
            case 1:
                os.system("cls")
                print(cliente)
            case 2:
                os.system("cls")
                cliente.ingresar(comprobar_numero(input("Cuanto quieres ingresar: ")))
            case 3:
                os.system("cls")
                cliente.retirar(comprobar_numero(input("Cuanto quieres retirar: ")))
            case 4:
                print("Ha salido del sistema, que pase buen día")
                break


def listar_opciones():
    print("-" * 55)
    print("[1] - Información cuenta")
    print("[2] - Ingresar dinero")
    print("[3] - Retirar dinero")
    print("[4] - Salir")
    print("-" * 55)


cliente = crear_cliente()
opciones()



