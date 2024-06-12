from inputs import *

def crear_pokemon(id_pokemon: int, nombre: str, tipo: str, poder_de_ataque: int, poder_de_defensa: int, habilidades: str, medida_pokemon: str) -> dict:
    diccionario_pokemon = {
        "id_pokemon": id_pokemon,
        "nombre": nombre,
        "tipo": tipo,
        "poder_de_ataque": poder_de_ataque,
        "poder_de_defensa": poder_de_defensa,
        "habilidades": habilidades,
        "medida_pokemon": medida_pokemon
    }
    
    return diccionario_pokemon
    
def ingresar_pokemon(lista_pokemones: list):
    for i in range(len(lista_pokemones)):
        id_pokemon = len(lista_pokemones) + 1
        #LLAMAR a las funciones para las validaciones aca
        nombre = input("ingrese el nombre:")
        tipo = input("Ingrese el tipo (agua, bicho, dragón, eléctrico, fantasma, fuego,)")
        poder_de_ataque = get_int(mostrar_mensaje, "El poder de ataque debe estar entre 0 y 150, por favor intenta de nuevo:", 1, 150, 3)
        poder_de_defensa = get_int(mostrar_mensaje, "El poder de ataque debe estar entre 0 y 150, por favor intenta de nuevo:", 1, 150, 3)
        habilidades = input("Ingrese las habilidades: ")
        medida_pokemon = input("Ingrese el tamaño de su pokemon: ")
        
        diccionario_pokemones = crear_pokemon(id_pokemon, nombre, tipo, poder_de_ataque, poder_de_defensa, habilidades, medida_pokemon)
        lista_pokemones.append(diccionario_pokemones)
        id_pokemon += 1
        break

def editar_pokemon(lista_pokemones: list, id_pokemon: int):
    for pokemon in lista_pokemones:
        if id_pokemon == pokemon["id_pokemon"]:
            mensaje = input("Está por editar un pokemon, desea continuar? ingrese 1 para si - 2 para no: ")
            if mensaje == "2":
                break
            elif mensaje == "1":
                
                menu_ediciones = int(input("1. Modificar nombre \n 2. Modificar tipo \n 3. Modificar poder de ataque \n 4. Modificar poder de defensa \n 5. Modificar habilidades \n 6. Modificar tamaño del pokemon \n 7. Salir"))
                
                match menu_ediciones:
                    case 1:
                        nombre_nuevo = input("ingrese un nuevo nombre para su pokemon:")
                        pokemon["nombre"] = nombre_nuevo
                    case 2:
                        tipo_nuevo = input("Ingrese el nuevo tipo: ")
                        pokemon["tipo"] = tipo_nuevo
                    case 3:
                        poder_nuevo = int(input("Ingrese el nuevo poder de ataque: "))
                        pokemon["poder_de_ataque"] = poder_nuevo
                    case 4:
                        defensa_nuevo = int(input("Ingrese el nuevo poder de defensa: "))
                        pokemon["poder_de_defensa"] = defensa_nuevo
                    case 5:
                        habilidad_nueva = input("Ingrese la habilidad nueva: ")
                        pokemon["habilidad"] = habilidad_nueva
                    case 6:
                        medida_nueva = input("Ingrese el nuevo tamaño: ")
                        pokemon["medida_pokemon"] = medida_nueva
                    case 7:
                        break

#eliminar
def eliminar_pokemon(lista_pokemones: list, id_pokemon: int):
    pokemon_a_eliminar = None
    for pokemon in lista_pokemones:
        if id_pokemon == pokemon["id_pokemon"]:
            print(f"el pokemon asociado a ese id es: {pokemon["nombre"]}")
            mensaje = input("Está por eliminar un pokemon, desea continuar? ingrese 1 para si - 2 para no: ")
            if mensaje == "2":
                break
            elif mensaje == "1":
                pokemon_a_eliminar = pokemon
                print("pokemon eliminado!!")
                mensaje = input("desea ver los datos del pokemon eliminado?: ingrese 1 para si - 2 para no: ")
                if mensaje == "2":
                    break
                elif mensaje == "1":
                    print(f"{'Id':{3}}|{'Nombre':{20}}|{'Tipo':{20}}|{'Ataque':{20}}|{'Tamaño':{20}}|{'Defensa':{20}}|{'Habilidades':{20}}")
                    print(f"{pokemon["id_pokemon"]}\t|{pokemon["nombre"]}\t|{pokemon["tipo"]}\t|{pokemon["poder_de_ataque"]}\t|{pokemon["poder_de_defensa"]}\t|{pokemon["habilidades"]}\t|{pokemon["medida_pokemon"]} ")
                    
                break
        
    if pokemon_a_eliminar != None:
        lista_pokemones.remove(pokemon_a_eliminar)
    return pokemon_a_eliminar
    
#mostrar la lista de pokemons
def mostrar_pokemones(diccionario_pokemones: list):
    # for pokemon in lista_pokemones:
    print("*" * 60)
    print("\n")
    print(f"|{'Id':{3}}|{'Nombre':{10}}|{'Tipo':{10}}|{'Ataque':{10}}|{'Tamaño':{10}}|{'Defensa':{10}}|{'Habilidades':{10}}")
    print("-" * 60)
    print(f"{diccionario_pokemones["id_pokemon"]}\t|{diccionario_pokemones["nombre"]}\t|{diccionario_pokemones["tipo"]}\t|{diccionario_pokemones["poder_de_ataque"]}\t|{diccionario_pokemones["poder_de_defensa"]}\t|{diccionario_pokemones["habilidades"]}")
        
def mostrar_lista_pokemones(lista_pokemones: list):
    for pokemon in lista_pokemones:
        mostrar_pokemones(pokemon)

def ordernar_pokemones_ascendente(lista_pokemones: list, seleccion: str):
    lista = len(lista_pokemones)
    for i in range(0, lista - 1):
        for j in range(i + 1, lista):
            if lista_pokemones[i][seleccion] > lista_pokemones[j][seleccion]:
                swapeo = lista_pokemones[i][seleccion]
                lista_pokemones[i][seleccion] = lista_pokemones[j][seleccion]
                lista_pokemones[j][seleccion] = swapeo                

def ordernar_pokemones_descendente(lista_pokemones: list, seleccion: str):
    lista = len(lista_pokemones)
    for i in range(0, lista - 1):
        for j in range(i + 1, lista):
            if lista_pokemones[i][seleccion] < lista_pokemones[j][seleccion]:
                swapeo = lista_pokemones[i][seleccion]
                lista_pokemones[i][seleccion] = lista_pokemones[j][seleccion]
                lista_pokemones[j][seleccion] = swapeo                

def ordenar_pokemones(lista_pokemones: list):
    mensaje_usuario = int(input("1. por Nombre \n 2. por Tipo \n 3. por Ataque \n 4. por Defensa\n Seleccione una opcion para ordenar los pokemones: "))
    ordenar = int(input("1. Ascendente \n 2. Descendente\n Seleccione el orden en el que se mostrará: "))
    seleccion = ""
    
    if mensaje_usuario == 1:
        seleccion = "nombre"
    elif mensaje_usuario == 2:
        seleccion = "tipo"
    elif mensaje_usuario == 3:
        seleccion = "poder_de_ataque"
    elif mensaje_usuario == 4:
        seleccion = "poder_de_defensa"
    
    match ordenar:
        case 1:
            ordernar_pokemones_ascendente(lista_pokemones, seleccion)
        case 2:
            ordernar_pokemones_descendente(lista_pokemones, seleccion)
            

def buscar_pokemon_id(lista_pokemones: list, id_pokemon: int):
    for pokemon in lista_pokemones:
        if id_pokemon == pokemon["id_pokemon"]:
            print(f"el pokemon asociado a ese ID es: {pokemon["nombre"]} y sus atributos son: \n {pokemon["id_pokemon"]}\t|{pokemon["tipo"]}\t|{pokemon["poder_de_ataque"]}\t|{pokemon["poder_de_defensa"]}\t|{pokemon["habilidades"]}\t|{pokemon["medida_pokemon"]}")

def calcular_promedios(lista_pokemones: list):
    total_electricos = 0
    total_psiquicos = 0
    total_tierra = 0
    
    suma_electricos = 0
    suma_psiquicos = 0
    suma_tierra = 0
    
    for pokemon in lista_pokemones:
        tipo = pokemon["tipo"]
        if tipo == "Eléctrico":
            total_electricos += 1
            suma_electricos += pokemon["poder_de_ataque"]
        elif tipo == "Psíquico":
            total_psiquicos += 1
            suma_psiquicos += pokemon["poder_de_ataque"]
        elif tipo == "Tierra":
            total_tierra += 1
            suma_tierra += pokemon["poder_de_defensa"]
        
    promedios = {"promedio_electricos": 0, "promedio_psiquicos": 0, "promedio_tierra": 0}
    if total_electricos > 0:
        promedios["promedio_electricos"] = suma_electricos / total_electricos
    if total_psiquicos > 0:
        promedios["promedio_psiquicos"] = suma_psiquicos / total_psiquicos
    if total_tierra > 0:
        promedios["promedio_tierra"] = suma_tierra / total_tierra
        
    return promedios

def mostrar_promedios(lista_pokemones: list):
    mensaje_usuario = int(input("1. Ataque de los pokemones eléctricos \n 2. Ataque de los pokemones psíquicos \n 3. Defensa de los pokemones tierra\n Seleccione una opcion para calcular el promedio de los pokemones: "))
    promedios = calcular_promedios(lista_pokemones)
        
    match mensaje_usuario:
        case 1:
            if "promedio_electricos" in promedios:
                print("Promedio de ataque de los pokemones eléctricos:", promedios["promedio_electricos"])
            else:
                print("No hay pokemones eléctricos en la lista.")
        case 2:
            if "promedio_psiquicos" in promedios:
                print("Promedio de ataque de los pokemones psíquicos:", promedios["promedio_psiquicos"])
            else:
                print("No hay pokemones psíquicos en la lista.")
        case 3:
            if "promedio_tierra" in promedios:
                print("Promedio de defensa de los pokemones tierra:", promedios["promedio_tierra"])
            else:
                print("No hay pokemones de tierra en la lista.")
        case _:
            print("Opción inválida")
        
    