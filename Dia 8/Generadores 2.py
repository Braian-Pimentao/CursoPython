def mi_generador():
    num = 1
    while True:
        yield 7 * num
        num += 1


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
