def mensaje(funcion):
    def otra_funcion():
        print("+" * 50)
        print("Su turno es:")
        print(next(funcion))
        print("Espere su turno, por favor")
        print("+" * 50)
    return otra_funcion


def generador_perfumeria():
    for n in range(1,10000):
        yield f"P- {n}"


def generador_farmacia():
    for n in range(1, 10000):
        yield f"F- {n}"


def generador_cosmetica():
    for n in range(1, 10000):
        yield f"C- {n}"




