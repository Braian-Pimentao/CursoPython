from pathlib import Path
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
mi_archivo = open('registro.txt', 'a')

for linea in registro_ultima_sesion:
    mi_archivo.writelines(linea + "\t")

mi_archivo.close()
mi_archivo = open('registro.txt').read()
print(Path("D:","Curso_Python","CursoPython","Dia 6","registro.txt").stem)
