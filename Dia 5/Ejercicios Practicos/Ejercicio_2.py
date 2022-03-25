def letras_palabras_ordenadas(palabra):
    palabra = list(set(palabra))
    palabra.sort()
    return palabra


print(letras_palabras_ordenadas("entretenido"))