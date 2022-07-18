import openpyxl
version = 21

nombres = open('D:\\Adaptaciones\\Canada\\nombres.txt')
excel_document = openpyxl.load_workbook(f'D:\\Adaptaciones\\Canada\\prueba_canada.xlsx')

lista_nombres = []
nombres_figuras = []


contador_puntos = 1
contador_figura = 1

lista_coordenadas = []


for mapa in nombres.readlines():
    lista_nombres.append(mapa.rstrip('\n'))


print(lista_coordenadas)

sheet_polylines = excel_document['Map Polylines']
sheet_figures = excel_document['Map Figures']

posicion_columnas_polylines = len(sheet_polylines["C"]) + 1

for i in range(1, len(lista_nombres)+1):
    try:
        mapa_formateado = open(f'D:\\Adaptaciones\\Canada\\mapas_formateados\\coordenadas_formateadas_{i}.txt','r')
        lista_coordenadas = []
        for coordenada in mapa_formateado.readlines():
            lista_coordenadas.append(coordenada.rstrip('\n'))
        nombre_figura = lista_nombres[i-1]
        nombres_figuras.append(f"{nombre_figura}{contador_figura}")
        for i in range(1, len(lista_coordenadas)):
            sheet_polylines[f"F{posicion_columnas_polylines}"].value = lista_coordenadas[i - 1]
            sheet_polylines[f"H{posicion_columnas_polylines}"].value = lista_coordenadas[i]
            sheet_polylines[f"C{posicion_columnas_polylines}"].value = contador_puntos
            sheet_polylines[f"B{posicion_columnas_polylines}"].value = f"{nombre_figura}{contador_figura}"
            sheet_polylines[f"A{posicion_columnas_polylines}"].value = "COASTL"
            sheet_polylines[f"D{posicion_columnas_polylines}"].value = "G"
            sheet_polylines[f"E{posicion_columnas_polylines}"].value = "G"
            sheet_polylines[f"I{posicion_columnas_polylines}"].value = "S"

            posicion_columnas_polylines +=1

            if contador_puntos < 90:
                contador_puntos +=1
            else:
                contador_puntos = 1
                contador_figura += 1
                nombres_figuras.append(f"{nombre_figura}{contador_figura}")

        contador_figura=1
        contador_puntos=1
    except FileNotFoundError:
        print("El archivo No existe")

posicion_columnas_figures=2
for i in range(len(nombres_figuras)):
    sheet_figures[f"A{posicion_columnas_figures}"].value = "COASTL"
    sheet_figures[f"B{posicion_columnas_figures}"].value = nombres_figuras[i]
    sheet_figures[f"C{posicion_columnas_figures}"].value = "T"
    sheet_figures[f"D{posicion_columnas_figures}"].value = "1"
    sheet_figures[f"E{posicion_columnas_figures}"].value = "3"
    sheet_figures[f"F{posicion_columnas_figures}"].value = "LIN"

    posicion_columnas_figures +=1


print(nombres_figuras)

excel_document.save(f'D:\\Adaptaciones\\Canada\\PRUEBA_CANADA_V100.xlsx')