import os
from pathlib import Path


def pedir_numero(opciones):
    while True:
        print("-------------------------------------------------------")
        numero = input("Elige una opción: ")
        print("-------------------------------------------------------")
        if numero.isdigit():
            if int(numero) <= opciones:
                return int(numero)
            else:
                print("Opción fuera de rango.")
        else:
            print("Eso no es un numero.")


def elegirCategoria():
    if contador_archivos == 0:
        print("No hay categorias")
        return
    categorias = tuple(archivo.iterdir())
    os.system("cls")
    print("-------------------------------------------------------")
    print("----------------------CATEOGORÍAS----------------------")
    print("-------------------------------------------------------")
    for categoria in categorias:
        print(f"[{categorias.index(categoria) + 1}]{categoria.stem}")

    return categorias[pedir_numero(len(categorias)) - 1]


def elegirReceta(categoria_elegida):
    if contador_archivos == 0:
        print("No hay recetas")
        return
    recetas = tuple(archivo.glob(f"{categoria_elegida.stem}/*.txt"))

    os.system("cls")
    print("-------------------------------------------------------")
    print("------------------------RECETAS------------------------")
    print("-------------------------------------------------------")
    for receta in recetas:
        print(f"[{recetas.index(receta) + 1}] - {receta.stem}")

    receta = recetas[pedir_numero(len(recetas)) - 1]
    print(open(receta).read())

    return receta

def crearReceta(categiria_elegida):



print("BIENVENIDO AL RECETARIO DE PYTHON")
archivo = Path("Recetas")
contador_archivos = 0
recetas = None

for aux in archivo.glob("**/*.txt"):
    contador_archivos += 1

print(f"La ruta de las recetas es: {archivo.absolute()}")
print(f"Hay un total de {contador_archivos} recetas")

lista_opciones = ("[1] - Leer receta",
                  "[2] - Crear receta",
                  "[3] - Leer Categorías",
                  "[4] - Eliminar Receta",
                  "[5] - Eliminar Categoría",
                  "[6] - Salir del programa")

print("-------------------------------------------------------")
print("-----------------------OPCIONES------------------------")
print("-------------------------------------------------------")
for opcion in lista_opciones:
    print(opcion)

match pedir_numero(len(lista_opciones)):
    case 1:
        categoria_elegida = elegirCategoria()
        elegirReceta(categoria_elegida)
    case 2:
        categoria_elegida = elegirCategoria()
        crearReceta(categoria_elegida)
