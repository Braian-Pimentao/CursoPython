import math

import openpyxl

excel_document_origen = openpyxl.load_workbook(f'D:\\Adaptaciones\\Canada\\obtención_puntos.xlsx')
excel_document_destino = openpyxl.load_workbook(f'D:\\Adaptaciones\\Canada\\PRUEBA_CANADA_V100.xlsx')

sheet_origen = excel_document_origen['Aerodromes']
sheet_destino = excel_document_destino['Aerodromes']

contador_columnas_aerodromos = len(sheet_origen["A"]) + 1

contador_destino = 2

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

for i in range(2,contador_columnas_aerodromos):
    sheet_destino[f"A{contador_destino}"].value = sheet_origen[f"A{i}"].value
    sheet_destino[f"B{contador_destino}"].value = sheet_origen[f"F{i}"].value
    sheet_destino[f"C{contador_destino}"].value = "N"
    sheet_destino[f"D{contador_destino}"].value = 10
    sheet_destino[f"E{contador_destino}"].value = 0
    sheet_destino[f"F{contador_destino}"].value = calcular_latitud(sheet_origen[f"D{i}"].value)
    sheet_destino[f"G{contador_destino}"].value = 30
    sheet_destino[f"H{contador_destino}"].value = 0
    sheet_destino[f"I{contador_destino}"].value = sheet_origen[f"C{i}"].value
    sheet_destino[f"J{contador_destino}"].value = calcular_longitud(sheet_origen[f"E{i}"].value)
    sheet_destino[f"K{contador_destino}"].value = "B"

    contador_destino += 1



print(contador_columnas_aerodromos)

excel_document_destino.save(f'D:\\Adaptaciones\\Canada\\PRUEBA_CANADA_V203.xlsx')
excel_document_destino.close()
excel_document_origen.close()


