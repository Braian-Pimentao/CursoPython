def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


describir_persona("María", color_ojos = "azules", color_pelo = "rubio")
