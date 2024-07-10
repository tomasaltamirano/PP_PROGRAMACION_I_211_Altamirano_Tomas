def batalla_pokemon(lista_pokemones: list):
    """
    Simula una batalla Pokémon basada en ciertos criterios de habilidades, tipo, tamaño y poder de ataque.

    Args:
        lista_pokemones (list): Lista de pokémones participantes en la batalla.
    """
    
    
    ganador = []
    for pokemon in lista_pokemones:
        if pokemon["tipo"] == "Fuego" and pokemon["medida_pokemon"] == "XL" and "Lanzallamas" in pokemon["habilidades"] and pokemon["poder_de_ataque"] > 80:
            ganador.append(pokemon)
        elif pokemon["tipo"] == "Agua" and pokemon["medida_pokemon"] == "L" and "Hidrobomba" in pokemon["habilidades"] and pokemon["poder_de_ataque"] > 80:
            ganador.append(pokemon)
    if len(ganador) >= 3:
        print("Ganaste la batalla")
    else:
        print("Perdiste! Logia ganó la batalla")