def reducir_lista(lista_numeros):
    lista_numeros.sort()
    lista_numeros = list(set(lista_numeros))
    lista_numeros.pop()
    return lista_numeros


def promedio(lista_numeros):
    suma = 0
    for n in lista_numeros:
        suma += n
    return suma/len(lista_numeros)


lista = [2, 4, 5, 6, 7, 2, 1, 2, 1, 4]
print(lista)

lista = reducir_lista(lista)
print(lista)
print(promedio(lista))

