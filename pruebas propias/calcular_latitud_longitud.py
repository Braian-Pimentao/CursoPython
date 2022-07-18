import math
latitud = 53
longitud = -95.1028208009999


#=SI($B4="";"";ABS(REDONDEAR.MENOS($B4;0)))
#=SI($B4="";"";REDONDEAR.MENOS(((ABS($B4)-$D4)*60);0))
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
    print(f"{grados}{minutos}{segundos}{orientacion}")

calcular_latitud(latitud)

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

    print(f"{grados}{minutos}{segundos}{orientacion}")

calcular_longitud(longitud)