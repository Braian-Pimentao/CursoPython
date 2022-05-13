from collections import defaultdict

mi_diccionario = defaultdict(lambda : "Valor no hallado")

mi_diccionario['edad'] = 44

print(mi_diccionario.items())