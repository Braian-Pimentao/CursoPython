def devolver_distintos(*args):
    suma = sum(args)
    if suma > 15:
        return max(args)
    elif suma < 10:
        return min(args)

    if suma in range(10, 16):

        for n in range(len(args)):
            if args[n] < args[(len(args)-1) - n]:
                continue
            else:
                return args[n]


print(devolver_distintos(1,4,3))
