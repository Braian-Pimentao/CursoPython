archivo_alturas = open('alturas.txt','r')

personas = []

for linea in archivo_alturas.readlines():
    personas.append(linea.rstrip('\n').split(','))

personas_encontradas = []
for iter in range(1, len(personas)):
    if personas[iter][0] > personas[iter - 1][0] and personas[iter][1] > personas[iter - 1][1]:
        personas_encontradas.append(personas[iter])

print(personas)
print(personas_encontradas)

archivo_alturas.close()




