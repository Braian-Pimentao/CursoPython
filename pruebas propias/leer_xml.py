import math
from xml.dom import minidom
contador_mapa = 1
circulo ="V"
doc = minidom.parse(f"D:\\Adaptaciones\\Canada\\circulos\\Circulo{circulo}.xml")


coordenadas = doc.getElementsByTagName("coordinates")[0].firstChild.data
print(coordenadas)
coordenadas = coordenadas.strip()
coordenadas = coordenadas[:-2]
print(coordenadas)

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

'''for coordenada in coordenadas:
    string_coor = coordenada.firstChild.data
    string_coor = string_coor.strip()
    mapa_copiar = open(f'D:\\Adaptaciones\\Canada\\mapas_sin_formatear\\coordenadas_sin_formatear_{contador_mapa}.txt', 'w')
    mapa_copiar.write(string_coor[:-2])
    mapa_copiar.close()

    contador_mapa += 1'''

print(len(coordenadas))

coordenadas = coordenadas.split(",0 ")
mapa_copiar = open(f'D:\\Adaptaciones\\Canada\\circulos\\circulo_formateado_{circulo}.txt',
                       'w')
todas_coordenadas = []
for coordenada in coordenadas:
    coordenadas_separadas = coordenada.split(",")
    if len(coordenadas_separadas) > 2:
        coordenada_rara = coordenada.split("-7.081154781429788e-10")
        for coordenada_rara in coordenadas:
            todas_coordenadas.append(coordenada_rara)
            coordenadas_separadas = coordenada.split(",")
            mapa_copiar.write(calcular_latitud(float(coordenadas_separadas[1])) +
                              calcular_longitud(float(coordenadas_separadas[0])) + "\n")
    else:
        todas_coordenadas.append(coordenada)
        mapa_copiar.write(calcular_latitud(float(coordenadas_separadas[1])) +
                        calcular_longitud(float(coordenadas_separadas[0])) + "\n")

mapa_copiar.close()

print(len(todas_coordenadas))
