import re


def verificar_saludo(frase):
    patron = r'Hola?\w+'
    if re.search(patron, frase) is not None:
        print("Ok")
    else:
        print("No has saludado")


verificar_saludo("Que talHola")