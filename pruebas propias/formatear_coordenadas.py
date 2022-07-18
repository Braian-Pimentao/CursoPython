import math
import pathlib
import openpyxl
import os

def calcular_latitud(latitud):
    grados = abs(math.trunc(latitud))
    minutos = math.floor(((abs(latitud)-grados)*60))
    segundos = round((abs(latitud)-(grados+minutos/60))*(60*60))

    if segundos == 60:
        segundos = 0
        minutos +=1
        if minutos == 60:
            minutos=0
            grados +=1

    grados = str(grados)
    minutos = str(minutos)
    segundos = str(segundos)
    minutos = minutos if len(minutos) == 2 else "0"+minutos
    segundos = segundos if len(segundos) == 2 else "0"+segundos

    orientacion = "N" if latitud >= 0 else "S"
    return f"{grados}{minutos}{segundos}{orientacion}"

def calcular_longitud(longitud):
    grados = math.floor(abs(longitud))
    minutos = math.floor(((abs(longitud) - grados) * 60))
    segundos = round((abs(longitud) - (grados + minutos / 60)) * (60 * 60))

    if segundos == 60:
        segundos = 0
        minutos +=1
        if minutos == 60:
            minutos=0
            grados +=1

    grados = str(grados)
    minutos = str(minutos)
    segundos = str(segundos)
    grados = grados if len(grados) == 3 else "0" + grados if len(grados) == 2 else "00" + grados
    minutos = minutos if len(minutos) == 2 else "0" + minutos
    segundos = segundos if len(segundos) == 2 else "0" + segundos

    orientacion = "E" if longitud >= 0 else "W"

    return f"{grados}{minutos}{segundos}{orientacion}"

columna = 4

for i in range(1,413):
    mapa = open(f'D:\\Adaptaciones\\Canada\\mapas_sin_formatear\\coordenadas_sin_formatear_{i}.txt')
    mapa_copiar = open(f'D:\\Adaptaciones\\Canada\\mapas_formateados\\coordenadas_formateadas_{i}.txt',
                       'w')
    coordenadas = mapa.readlines()[0].split(",0 ")
    for coordenada in coordenadas:
        print(coordenada)
        coordenadas_separadas = coordenada.split(",")
        mapa_copiar.write(calcular_latitud(float(coordenadas_separadas[1])) +
                          calcular_longitud(float(coordenadas_separadas[0]))+"\n")

    mapa.close()
    mapa_copiar.close()
    '''sheet[f"C{columna}"].value = float(coordenadas_separadas[0])
    sheet[f"B{columna}"].value = float(coordenadas_separadas[1])
    sheet[f"L{columna}"].value = pathlib.Path(mapa.name).stem

    columna += 1'''
'''
longitud = []
latitud = []
cambio = True


print(f"Total Coordenadas: {len(coordenadas)}")

for coordenada in coordenadas:
    print(coordenada)
    coordenadas_separadas = coordenada.split(",")
    print(f"Longitud coordenada{len(coordenadas_separadas)}")
    sheet[f"C{columna}"].value = float(coordenadas_separadas[0])
    sheet[f"B{columna}"].value = float(coordenadas_separadas[1])

    columna += 1
'''
#conversor.save("D:\\Adaptaciones\\Canada\\conversor_coordenadas_obtenidas.xlsx")
#os.startfile("D:\\Adaptaciones\\Canada\\conversor_coordenadas_obtenidas.xlsx")

