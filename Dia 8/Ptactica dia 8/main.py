import numeros


def pedir_numero():
    while True:
        print("[1] - Perfumeria\n[2] - Farmacia\n[3] - Cosmetica\n[4] - Salir")
        try:
            eleccion = int(input("Elige una opción:"))
        except ValueError:
            print("Opción no valida, vuelva a intentarlo")
        else:
            return eleccion


def preguntar_continuar():
    while True:
        respuesta = input("¿Desea Continuar? (y/n):")
        if respuesta == 'y' or respuesta == 'n':
            print("Que pase un buen día!!")
            return respuesta
        else:
            print("Valor no permitido, vuelve a intentarlo")


def opciones():
    print("Bienvenido a la farmacia Python")
    respuesta_continuar = "y"
    while respuesta_continuar == "y":
        match pedir_numero():
            case 1:
                perfumeria_decorada()
                respuesta_continuar = preguntar_continuar()
            case 2:
                farmacia_decorada()
                respuesta_continuar = preguntar_continuar()
            case 3:
                cosmetica_decorada()
                respuesta_continuar = preguntar_continuar()
            case 4:
                break
            case _:
                print("Opción no válida")


perfumeria_decorada = numeros.mensaje(numeros.generador_perfumeria())
farmacia_decorada = numeros.mensaje(numeros.generador_farmacia())
cosmetica_decorada = numeros.mensaje(numeros.generador_cosmetica())
opciones()
