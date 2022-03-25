import os
from pathlib import Path
from os import system


def pedir_numero():
    while True:
        numero = input("Elige una opción: ")
        if numero.isdigit():
            return int(numero)
        else:
            print("Eso no es un numero.")


def leerCategoria():
    if contador_archivos == 0:
        print("No hay categorias")
        return
    categorias = tuple(archivo.iterdir())
    for categoria in categorias:
        print(f"[{categorias.index(categoria) + 1}]{categoria.stem}")

    return categorias


def leerReceta():
    if contador_archivos == 0:
        print("No hay recetas")
        return
    recetas = tuple(archivo.glob("**/*.txt"))
    for receta in recetas:
        print(f"[{recetas.index(receta)+1}] - {receta.stem}")
    return recetas


def elegirReceta(elegido):
    os.system("cls")
    print(recetas[elegido].read_text())

print("BIENVENIDO AL RECETARIO DE PYTHON")
archivo = Path("Recetas")
contador_archivos = 0
recetas = None

for aux in archivo.glob("**/*.txt"):
    contador_archivos +=1
print(f"La ruta de las recetas es: {archivo.absolute()}")
print(f"Hay un total de {contador_archivos} recetas")
print("-------------------------------------------------------")

lista_opciones = ("[1] - Leer receta",
                  "[2] - Crear receta",
                  "[3] - Leer Categorías",
                  "[4] - Eliminar Receta",
                  "[5] - Eliminar Categoría",
                  "[6] - Salir del programa")

for opcion in lista_opciones:
    print(opcion)

print("-------------------------------------------------------")
match pedir_numero():
    case 1:
        categoriaElegida = leerCategoria()
        elegirReceta(pedir_numero())
        recetas = leerReceta()
    case 2:
        print("Caso 2")
