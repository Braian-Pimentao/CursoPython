texto = input("Escribe un texto para analizar:\n")
print("Dime 3 letras a buscar")
letras = [input("Letra 1:").lower(),
          input("Letra 2:").lower(),
          input("Letra 3:").lower()]
contador_letras = [texto.lower().count(letras[0]),
                   texto.lower().count(letras[1]),
                   texto.lower().count(letras[2])]
print("-------------------------------------------------------------------")
for i in range(3):
    print(f"-Letra '{letras[i]}': {contador_letras[i]}")

print(f"-En el Texto hay {len(texto.split())} palabras")
print(f"-La primera letra del texto es {texto[0]} y la última es {texto[-1]}")
print(f"""-El texto del revés es: 
    {" ".join(texto.split()[::-1])}""")
print("-La palabra Python {}".format(("está en el texto.", "no está en el texto.")["python" not in texto.lower()]))
