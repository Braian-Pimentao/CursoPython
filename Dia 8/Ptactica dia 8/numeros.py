def mensaje(funcion):
    def otra_funcion():
        print("Su turno es:")
        funcion()
        print("Espere su turno, por favor")

    return otra_funcion


def generador_perfumeria():
    x = 1
    #while True:
    print("P-" + str(x))
    #    x += 1


def generador_farmacia():
    x = 1
    while True:
        yield "F-" + str(x)
        x += 1


def generador_cosmetica():
    x = 1
    while True:
        yield "C-" + str(x)
        x += 1


perfumeria_decorada = mensaje(generador_perfumeria)

perfumeria_decorada()



