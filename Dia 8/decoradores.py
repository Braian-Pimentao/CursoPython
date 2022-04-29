def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("holaa")
        funcion(palabra)
        print("adios")

    return otra_funcion


def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())


mayusculas_decoradas = decorar_saludo(mayusculas)

mayusculas_decoradas("Bryan")
