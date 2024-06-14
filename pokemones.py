from inputs import *
from tabla import mostrar_pokemones
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
    
def ingresar_pokemon(lista_pokemones: list) -> list:
    for i in range(len(lista_pokemones)):
        id_pokemon = len(lista_pokemones) + 1
        #LLAMAR a las funciones para las validaciones aca
        nombre = get_string("ingrese el nombre: ", "error", 20, 3)
        
        tipos_pokemon = print("los tipos de pokemon que podes ingresar son: Agua, Bicho, Dragon, Electrico, Fantasma, Fuego,Hielo, Lucha, Normal, Planta, Psiquico, Roca,Tierra, Veneno, Volador")
        
        tipo = get_tipo(tipos_pokemon, lista_tipos)
        
        poder_de_ataque = get_int("ingrese el poder de ataque: (desde 0 hasta 150): ", "error", 0, 150, 3)
        
        poder_de_defensa = get_int("ingrese el poder de defensa: (desde 0 hasta 150): ", "error", 0, 150, 3)
        
        habilidades = []
        while len(habilidades) < 3:
            habilidad = get_string("Ingrese las habilidades: ", "error", 20, 3)
            habilidades.append(habilidad)
            continuar = get_int("Desea ingresar otra habilidad? ingrese 1 para confirmar - 2 para cancelar: ", "error", 1, 2, 3)
            if continuar == 2:
                break

        medida_pokemon = get_string("Ingrese el tamaño de su pokemon: (XS, S, M, L, XL)","error", 2, 3)
        
        diccionario_pokemones = crear_pokemon(id_pokemon, nombre, tipo, poder_de_ataque, poder_de_defensa, habilidades, medida_pokemon)
        lista_pokemones.append(diccionario_pokemones)
        id_pokemon += 1
        break

def editar_pokemon(lista_pokemones: list, id_pokemon: int) -> list:
    for pokemon in lista_pokemones:
        if id_pokemon == pokemon["id_pokemon"]:
            print(f"el pokemon asociado a ese id es: {pokemon["nombre"]}")
            
            mensaje = get_int("Está por editar un pokemon, desea continuar? ingrese 1 para confirmar - 2 para cancelar: ", "error", 1, 2, 3)
            if mensaje == 2:
                break
            elif mensaje == 1:
                lista_menu ="1.Modificar nombre\n2.Modificar tipo\n3.Modificar poder de ataque\n4.Modificar poder de defensa\n5.Modificar habilidades\n6.Modificar tamaño del pokemon\n7.Salir\nIngrese un numero de la lista para continuar"
                lista_opciones = [1,2,3,4,5,6,7]
                menu_ediciones = get_menus(lista_menu, lista_opciones)
                
                match menu_ediciones:
                    case 1:
                        nombre_nuevo = get_string("Ingrese un nombre nuevo: ", "error", 20, 3)
                        pokemon["nombre"] = nombre_nuevo
                        print("Pokemon modificado! acá están los cambios:")
                        mostrar_pokemones(pokemon)
                    case 2:
                        tipo_nuevo = get_string("Ingrese un tipo nuevo: ", "error", 10, 3)
                        pokemon["tipo"] = tipo_nuevo
                        print("Pokemon modificado! acá están los cambios:")
                        
                        mostrar_pokemones(pokemon)
                        
                    case 3:
                        poder_nuevo = get_int("Ingrese un nuevo poder de ataque: ", "error",0, 150, 3)
                        pokemon["poder_de_ataque"] = poder_nuevo
                        print("Pokemon modificado! acá están los cambios:")
                        
                        mostrar_pokemones(pokemon)
                        
                    case 4:
                        defensa_nuevo =  get_int("Ingrese un nuevo poder de defensa: ", "error",0, 150, 3)
                        pokemon["poder_de_defensa"] = defensa_nuevo
                        print("Pokemon modificado! acá están los cambios:")
                        
                        mostrar_pokemones(pokemon)
                        
                    case 5:
                        habilidad_nueva = get_string("Ingrese una nueva habilidad: ", "error", 20, 3)
                        pokemon["habilidad"] = habilidad_nueva
                        print("Pokemon modificado! acá están los cambios:")
                        
                        mostrar_pokemones(pokemon)
                        
                    case 6:
                        medida_nueva = get_string("Ingrese un tamaño nuevo: ", "error", 2, 3)
                        pokemon["medida_pokemon"] = medida_nueva
                        print("Pokemon modificado! acá están los cambios:")
                        
                        mostrar_pokemones(pokemon)
                        
                    case 7:
                        break

#eliminar
def eliminar_pokemon(lista_pokemones: list, id_pokemon: int, lista_eliminados: list) -> list:
    pokemon_a_eliminar = None
    for pokemon in lista_pokemones:
        if id_pokemon == pokemon["id_pokemon"]:
            print(f"el pokemon asociado a ese id es: {pokemon["nombre"]}")
            mensaje = get_int("Está por eliminar un pokemon, desea continuar? ingrese 1 para confirmar - 2 para cancelar: ", "error", 1, 2, 3)
            if mensaje == 2:
                break
            elif mensaje == 1:
                pokemon_a_eliminar = pokemon
                print("pokemon eliminado!!")
                mensaje = get_int("Desea ver los datos del pokemon eliminado? ingrese 1 para confirmar - 2 para cancelar: ", "error", 1, 2, 3)
                if mensaje == 2:
                    break
                elif mensaje == 1:
                    mostrar_pokemones(pokemon)
                break
        
    if pokemon_a_eliminar != None:
        lista_pokemones.remove(pokemon_a_eliminar)
        # lista_eliminados.append(pokemon_a_eliminar)
    # return pokemon_a_eliminar 
        
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
    # mensaje_usuario = int(input("1. por Nombre \n 2. por Tipo \n 3. por Ataque \n 4. por Defensa\n Seleccione una opcion para ordenar los pokemones: "))
    lista_menu1 = "1.por Nombre\n2.por Tipo\n3.por Ataque\n4.por Defensa\nSeleccione un numero de la lista para ordenar los pokemones: "
    lista_opciones1 = [1,2,3,4]
    mensaje_usuario = get_menus(lista_menu1, lista_opciones1)
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
            print("pokemon encontrado!")
            mostrar_pokemones(pokemon)

def calcular_promedios(lista_pokemones: list):
    total_electricos = 0
    total_psiquicos = 0
    total_tierra = 0
    
    suma_electricos = 0
    suma_psiquicos = 0
    suma_tierra = 0
    
    for pokemon in lista_pokemones:
        tipo = pokemon["tipo"]
        if tipo == "electrico":
            total_electricos += 1
            suma_electricos += pokemon["poder_de_ataque"]
        elif tipo == "psiquico":
            total_psiquicos += 1
            suma_psiquicos += pokemon["poder_de_ataque"]
        elif tipo == "tierra":
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
            print("error, no seleccionaste correctamente una de las opciones disponibles")
        
    