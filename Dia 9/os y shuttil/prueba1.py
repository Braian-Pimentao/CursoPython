import os
import send2trash

ruta = "D:\\Curso_Python\\CursoPython\\Dia 9\\os y shuttil\\Carpeta"

print(os.getcwd())

for carpeta, subdirectorios, archivos in os.walk(ruta):
    print(f"-Carpeta: {carpeta}")
    for sub in subdirectorios:
        print(f"\t- Subdirectorio : {sub}")
    for archivo in archivos:
        if archivo.endswith("txt"):
            print(f"\t- Archivo : {archivo}")
