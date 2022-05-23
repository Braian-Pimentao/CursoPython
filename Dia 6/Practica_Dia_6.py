import os
from pathlib import Path


def pedir_numero(opciones):
    while True:
        print("-"*55)
        numero = input("Elige una opción: ")
        print("-"*55)
        if numero.isdigit():
            if int(numero) <= opciones:
                return int(numero)
            else:
                print("Opción fuera de rango.")
        else:
            print("Eso no es un numero.")


def preguntar_continuar():
    while True:
        print("-"*55)
        respuesta = input("¿Desea continuar? (y/n) \n ")
        print("-"*55)
        if respuesta == "y" or respuesta == "n":
            if respuesta == "y":
                return True
            else:
                return False
        else:
            print("Eso no es un respuesta correcta.")


def listarCategorias():
    categorias = tuple(archivo.iterdir())
    if len(categorias) == 0:
        print("No hay categorías")
        return
    os.system("cls")
    print("-"*55)
    print("----------------------CATEOGORÍAS----------------------")
    print("-"*55)
    for categoria in categorias:
        print(f"[{categorias.index(categoria) + 1}]{categoria.stem}")
    return categorias


def listarRecetas(categoria):
    recetas_recogidas = tuple(archivo.glob(f"{categoria.stem}/*.txt"))
    if len(recetas_recogidas) == 0:
        print("No hay recetas en esta categoría")
        return

    os.system("cls")
    print("-"*55)
    print("------------------------RECETAS------------------------")
    print("-"*55)
    for receta in recetas_recogidas:
        print(f"[{recetas_recogidas.index(receta) + 1}] - {receta.stem}")
    return recetas_recogidas


def elegirCategoria():
    categorias = listarCategorias()
    if categorias is None:
        return
    return categorias[pedir_numero(len(categorias)) - 1]


def elegirReceta(categoria_elegida):
    recetas_recogidas = listarRecetas(categoria_elegida)
    if recetas_recogidas is None:
        return
    receta = recetas_recogidas[pedir_numero(len(recetas_recogidas)) - 1]
    print(open(receta).read())

    return receta


def crearReceta(categoria):
    os.system("cls")
    nombre_receta = input("Dime el nombre de la receta: ")
    archivo = open(Path(categoria, nombre_receta + ".txt"), "w")
    print("-"*55)
    receta = input("Escribe el contenido de la receta: \n")
    print("-"*55)
    archivo.write(receta)
    archivo.close()


def crear_categoria():
    os.system("cls")
    nombre_categoria = input("Dime el nombre de la Categoría: ")
    Path("Recetas", nombre_categoria).mkdir()
    print("-"*55)
    print("Caregoría creada.")
    print("-"*55)


def eliminarReceta(categoria):
    recetas_recogidas = listarRecetas(categoria)
    if recetas_recogidas is None:
        return
    receta = recetas_recogidas[pedir_numero(len(recetas_recogidas)) - 1]
    receta.unlink()
    print("-"*55)
    print(f"La receta \"{receta.stem}\" ha sido eliminada.")
    print("-"*55)


def eliminar_categoria():
    categorias = listarCategorias()
    if categorias is None:
        return
    categoria = categorias[pedir_numero(len(categorias)) - 1]
    categoria.rmdir()
    print("-"*55)
    print(f"La categoría \"{categoria.stem}\" ha sido eliminada.")
    print("-"*55)


print("BIENVENIDO AL RECETARIO DE PYTHON")
archivo = Path("Recetas")
contador_archivos = 0

for aux in archivo.glob("**/*.txt"):
    contador_archivos += 1

print(f"La ruta de las recetas es: {archivo.absolute()}")
print(f"Hay un total de {contador_archivos} recetas")

lista_opciones = ("[1] - Leer receta",
                  "[2] - Crear receta",
                  "[3] - Crear Categoría",
                  "[4] - Eliminar Receta",
                  "[5] - Eliminar Categoría",
                  "[6] - Salir del programa")

while True:
    print("-"*55)
    print("-----------------------OPCIONES------------------------")
    print("-"*55)
    for opcion in lista_opciones:
        print(opcion)

    match pedir_numero(len(lista_opciones)):
        case 1:
            categoria_elegida = elegirCategoria()
            elegirReceta(categoria_elegida)
        case 2:
            categoria_elegida = elegirCategoria()
            crearReceta(categoria_elegida)
        case 3:
            crear_categoria()
        case 4:
            categoria_elegida = elegirCategoria()
            eliminarReceta(categoria_elegida)
        case 5:
            eliminar_categoria()
        case 6:
            break
    if not preguntar_continuar():
        break
    else:
        os.system("cls")

