import os
import re
import datetime
import time
import math


def recorrer_directorios():
    lista_archivos_numeros = []
    for root, directorio, file in os.walk('Mi_Gran_Directorio', topdown=False):
        for archivo in file:
            devuelto = buscar_patron(root, archivo)
            if devuelto:
                lista_archivos_numeros.append(devuelto)
    return lista_archivos_numeros


def buscar_patron(path, archivo):
    patron = r'N\w{3}\-\d{5}'
    ruta = open(os.path.join(path, archivo))
    texto = ruta.read()
    expresion_encontrada = re.search(patron, texto)
    ruta.close()
    if expresion_encontrada:
        return archivo, expresion_encontrada.group()


def imprimir_lista(lista_archivos,tiempo):
    print('-'*50)
    hoy = datetime.date.today().strftime('%d/%m/%Y')
    print(f'Fecha de búsqueda: {hoy}\n')
    print('ARCHIVO'+'\t'*4 + 'NRO. SERIE')
    print('-------'+'\t'*4 + '----------')
    for archivo, n_serie in lista_archivos:
        print(f'{archivo}\t\t{n_serie}')
    print(f'\nNúmeros encontrados: {len(lista_archivos)}')
    print(f'Duración de la búsqueda: {tiempo} segundos')
    print('-'*50)


inicio = time.time()
lista_directorios = recorrer_directorios()
final = time.time()

imprimir_lista(lista_directorios, math.ceil(final - inicio))

