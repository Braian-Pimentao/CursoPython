def numeros_persona(*args):
    return f"{args[0]}, la suma de tus números es {sum(args[1::])}"


print(numeros_persona("Bryan", 1, 3, 4, 5, 6))


