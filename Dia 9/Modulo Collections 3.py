from collections import deque

lista_ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

lista_deque = deque(lista_ciudades)

lista_deque.appendleft("Barcelona")

print(lista_deque)
