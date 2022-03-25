def comprobar_ceros(*args):
    for n in range(len(args)-1):
        if args[n] == 0 and args[n] == args[n + 1]:
            return True
    return False


print(comprobar_ceros(5, 6, 1, 0, 0, 9, 3, 5, 0))
