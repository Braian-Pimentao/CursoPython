texto = input("Escribe un texto para analizar:\n")
print("Dime 3 letras a buscar")
letras = [input("Letra 1:"), input("Letra 2:"), input("Letra 3:")]
contador_letras = [texto.lower().count(letras[0]),
                   texto.lower().count(letras[1]),
                   texto.lower().count(letras[2])]
print("-------------------------------------------------------------------")
print(f"-Letra {letras[0]}: {contador_letras[0]}")
print(f"-Letra {letras[1]}: {contador_letras[1]}")
print(f"-Letra {letras[2]}: {contador_letras[2]}")

print(f"-En el Texto hay {len(texto.split())} palabras")
print(f"-La primera letra del texto es {texto[0]} y la última es {texto[-1]}")
print(f""""-El texto del revés es: 
    {" ".join(texto.split()[::-1])}""")
print("-La palabra Python {}".format("está en el texto." if "python" in texto.lower() else "no está en el texto."))

