def mi_generador():
    x = 0
    while True:
        x += 1
        yield x


generador = mi_generador()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
