from modules.inputs import *
import json
import csv

def crear_csv(nombre_archivo):
    """
    Crea un archivo CSV vacío con el nombre especificado.

    Args:
        nombre_archivo (str): Nombre del archivo CSV a crear.
    """
    with open(nombre_archivo, 'w') as archivo:
        print("lista creada con exito")
        

# crear_csv(nombre_archivo)

def guardar_pokemones(nombre_archivo, lista_pokemones):
    """
    Guarda la lista de pokémones en un archivo CSV con el nombre especificado.

    Args:
        nombre_archivo (str): Nombre del archivo CSV donde se guardarán los pokémones.
        lista_pokemones (list): Lista de pokémones a guardar.
    """
    
    with open(nombre_archivo, 'w') as archivo:
        for pokemon in lista_pokemones:
            linea = f"{pokemon['id_pokemon']}, {pokemon['nombre']}, {pokemon['tipo']}, {pokemon['poder_de_ataque']}, {pokemon['poder_de_defensa']}, {pokemon['habilidades']}, {pokemon['medida_pokemon']}\n"
            archivo.write(linea)
        print("lista guardada con exito")


def guardar_json(lista_pokemones: list):
    """
    Guarda los pokémones de un tipo específico en un archivo JSON con el formato 'tipo_pokemones.json'.

    Args:
        lista_pokemones (list): Lista de pokémones a filtrar y guardar.
    """
    tipo = get_tipo("ingresa el tipo de pokemon", lista_tipos)
    pokemones_especificos = []
    
    for pokemon in lista_pokemones:
        if tipo in pokemon["tipo"]:
            nombre = pokemon["nombre"]
            ataque = pokemon["poder_de_ataque"]
            defensa = pokemon["poder_de_defensa"]
            
            if ataque > defensa:
                habilidad_tipo = "Ataque"
            elif defensa > ataque:
                habilidad_tipo = "Defensa"
            else:
                habilidad_tipo = "Ambos"
            
            insertar_datos = f"{nombre}-{max(ataque, defensa)}-{habilidad_tipo}"
            pokemon_json = {
                "Pokemon": insertar_datos
            }
            
            pokemones_especificos.append(pokemon_json)
            
    nombre_archivo = f"{tipo}_pokemones.json"
    with open(nombre_archivo, "w") as archivo:
        json.dump(pokemones_especificos, archivo, indent=4)
    print(f"se guardaron los pokemones del tipo {tipo} en el archivo {nombre_archivo}")