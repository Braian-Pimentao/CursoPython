import os

archivo_lista_borrar = open(f'D:\\Adaptaciones\\Canada\\lista_borrar.txt')


lista_borrar = []

for mapa in archivo_lista_borrar.readlines():
    lista_borrar.append(mapa.rstrip('\n'))

print(lista_borrar)

for nombre in lista_borrar:
    try:
        os.remove(f'D:\\Adaptaciones\\Canada\\mapas_formateados\\{nombre}.txt')
    except FileNotFoundError:
        print("Archivo no encontrado")