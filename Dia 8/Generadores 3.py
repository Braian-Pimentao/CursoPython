def mi_generador():
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te queda 1 vida"
    yield "Game Over"


perder_vida = mi_generador()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))

