from random import *

nombre = input("¿Cómo te llamas?\n")
numero_intentos = 8


def comprobarString(numero):
    while True:
        if numero.isdigit():
            numero = int(numero)
            if numero in range(1, 100):
                return numero
            else:
                print("--------------------------------------------------")
                print("El numero elegido no está en el rango permitido.")
                numero = input("Elige otro número: \n")
        else:
            print("--------------------------------------------------")
            print("Valor no permitido")
            print("--------------------------------------------------")
            numero = input("Elige otro número: \n")


def respuestaIntento():
    print("--------------------------------------------------")
    pregunta = input("¿Quieres seguir intentandolo?(s/n)").lower()
    if pregunta == "s":
        return False
    elif pregunta == "n":
        print("--------------------------------------------------")
        print(f"-Número correcto: {numero_random}")
        print("Que tenga un buen día!")
        return False, False
    else:
        print("--------------------------------------------------")
        print("Respuesta no permitida, vuelve a intentarlo")
        return True


def respuestaJuegoNuevo():
    print("--------------------------------------------------")
    pregunta = input("¿Quieres jugar de nuevo?(s/n)").lower()
    if pregunta == "s":
        return False, randint(1,100), 8
    elif pregunta == "n":
        print("--------------------------------------------------")
        print("Que tenga un buen día!")
        return False, False
    else:
        print("--------------------------------------------------")
        print("Respuesta no permitida, vuelve a intentarlo")
        return True


print("--------------------------------------------------")
print("""Vamos a jugar a un juego, a continuación te explico las reglas:
    -Vas a tener que adivinar un número entre el 1 y el 100
    -Tendrás 8 intentos
    -Si fallas se te dirá lo cerca que has estado""")
numero_random = randint(1, 100)
continuar_juego = True
while continuar_juego:
    while numero_intentos >= 1:
        print("--------------------------------------------------")
        numero_elegido = comprobarString(input("Dime un número: \n"))
        numero_intentos -= 1
        if numero_elegido == numero_random:
            print("--------------------------------------------------")
            print("Enhorabuena, has acertado el número")
            print(f"-Nombre jugador: {nombre}")
            print(f"-Intentos realizados: {8 - numero_intentos}")
            condition = True
            while condition:
                lista = respuestaJuegoNuevo()
                if type(lista) != bool:
                    if len(lista) == 3:
                        condition = lista[0]
                        numero_random = lista[1]
                        numero_intentos = lista[2]
                    elif len(lista) == 2:
                        condition = lista[0]
                        continuar_juego = lista[1]
                else:
                    condition = lista
        elif numero_elegido > numero_random:
            print("--------------------------------------------------")
            print(f"Lo siento, el número {numero_elegido} es mayor al número correcto")
            print(f"-Número de intentos restantes: {numero_intentos} ")
            if numero_intentos == 0:
                break
            condition = True
            while condition:
                lista = respuestaIntento()
                if type(lista) != bool:
                    if len(lista) == 2:
                        condition = lista[0]
                        continuar_juego = lista[1]
                else:
                    condition = lista
        elif numero_elegido < numero_random:
            print("--------------------------------------------------")
            print(f"Lo siento, el número {numero_elegido} es menor al número correcto")
            print(f"-Número de intentos restantes: {numero_intentos} ")
            if numero_intentos == 0:
                break
            condition = True
            while condition:
                lista = respuestaIntento()
                if type(lista) != bool:
                    if len(lista) == 2:
                        condition = lista[0]
                        continuar_juego = lista[1]
                else:
                    condition = lista
    else:
        print("--------------------------------------------------")
        print("-Se te han acabado los intentos")
        print(f"-Número correcto: {numero_random}")
        condition = True
        while condition:
            lista = respuestaJuegoNuevo()
            if type(lista) != bool:
                if len(lista) == 3:
                    condition = lista[0]
                    numero_random = lista[1]
                    numero_intentos = lista[2]
                elif len(lista) == 2:
                    condition = lista[0]
                    continuar_juego = lista[1]
            else:
                condition = lista


