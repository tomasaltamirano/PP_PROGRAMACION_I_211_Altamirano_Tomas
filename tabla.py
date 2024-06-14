def mostrar_pokemones(diccionario_pokemones: list):
    print("*" * 60)
    print("\n")
    print(f"|{'Id':{3}}|{'Nombre':{10}}|{'Tipo':{10}}|{'Ataque':{10}}|{'Tamaño':{10}}|{'Defensa':{10}}|{'Habilidades':{10}}")
    print("-" * 60)
    print(f"{diccionario_pokemones["id_pokemon"]}\t|{diccionario_pokemones["nombre"]}\t|{diccionario_pokemones["tipo"]}\t|{diccionario_pokemones["poder_de_ataque"]}\t|{diccionario_pokemones["medida_pokemon"]}\t|{diccionario_pokemones["poder_de_defensa"]}\t|{diccionario_pokemones["habilidades"]}")