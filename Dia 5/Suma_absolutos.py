def suma_absolutos(*args):
    suma = 0
    for n in args:
        suma += abs(n)
    return suma


print(suma_absolutos(2, 3, 4, 5, -2, 3, -565))
