import re


def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    if re.search(patron,cp) is not None:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

verificar_cp("XX2222")