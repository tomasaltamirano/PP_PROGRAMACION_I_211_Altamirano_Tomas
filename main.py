from os import system
from modules.pokemones import *
from modules.batalla_pokemon import *
from modules.utilidades import *
# import csv

def menu_de_usuario() -> str:
    """
    Muestra un menú interactivo para el usuario y captura la opción seleccionada.
    Returns:
        str: La opción seleccionada por el usuario.
    """
    opcion = input("MENU\n1. Ingresar pokemon \n2. Modificar pokemon\n3. Elminar pokemon \n4. Mostrar todos los pokemones\n5. Ordenar pokemones\n6. Buscar pokemones por ID \n7. Calcular promedio y mostrarlo\n8. Batalla pokemon \n9. Guardar json \n10. Salir \n. Elija una opcion: ")
    return opcion  

lista_pokemones = [{
        "id_pokemon": 1,
        "nombre": "Bulbasaur",
        "tipo": "Planta",
        "poder_de_ataque": 60,
        "poder_de_defensa": 62,
        "habilidades": ["Clorofila", "Espesura"],
        "medida_pokemon": "S"
    },
    {
        "id_pokemon": 2,
        "nombre": "Charmander",
        "tipo": "Fuego",
        "poder_de_ataque": 80,
        "poder_de_defensa": 43,
        "habilidades": ["Lanzallamas", "Poder Solar"],
        "medida_pokemon": "XL"
    },
    {
        "id_pokemon": 3,
        "nombre": "Squirtle",
        "tipo": "Agua",
        "poder_de_ataque": 80,
        "poder_de_defensa": 65,
        "habilidades": ["Hidrobomba", "Cura Lluvia"],
        "medida_pokemon": "L"
    },
    {
        "id_pokemon": 4,
        "nombre": "Pidgey",
        "tipo": "Volador",
        "poder_de_ataque": 45,
        "poder_de_defensa": 40,
        "habilidades": ["Vista Lince", "Tumbos"],
        "medida_pokemon": "M"
    },
    {
        "id_pokemon": 5,
        "nombre": "Rattata",
        "tipo": "Normal",
        "poder_de_ataque": 56,
        "poder_de_defensa": 35,
        "habilidades": ["Fuga", "Agallas"],
        "medida_pokemon": "XS"
    },
    {
        "id_pokemon": 6,
        "nombre": "Ekans",
        "tipo": "Veneno",
        "poder_de_ataque": 60,
        "poder_de_defensa": 44,
        "habilidades": ["Intimidación", "Mudar"],
        "medida_pokemon": "M"
    },
    {
        "id_pokemon": 7,
        "nombre": "Pikachu",
        "tipo": "Electrico",
        "poder_de_ataque": 55,
        "poder_de_defensa": 40,
        "habilidades": ["Electricidad Estática", "Pararrayos"],
        "medida_pokemon": "L"
    },
    {
        "id_pokemon": 8,
        "nombre": "Sandshrew",
        "tipo": "Tierra",
        "poder_de_ataque": 75,
        "poder_de_defensa": 85,
        "habilidades": ["Velo Arena", "Flexibilidad"],
        "medida_pokemon": "XS"
    },
    {
        "id_pokemon": 9,
        "nombre": "Abra",
        "tipo": "Psiquico",
        "poder_de_ataque": 20,
        "poder_de_defensa": 15,
        "habilidades": ["Sincronía", "Foco Interno"],
        "medida_pokemon": "XL"
    },
    {
        "id_pokemon": 10,
        "nombre": "Geodude",
        "tipo": "Roca",
        "poder_de_ataque": 80,
        "poder_de_defensa": 100,
        "habilidades": ["Cabeza Roca", "Robustez"],
        "medida_pokemon": "XS"
    },
    {
        "id_pokemon": 11,
        "nombre": "Magnemite",
        "tipo": "Electrico",
        "poder_de_ataque": 55,
        "poder_de_defensa": 95,
        "habilidades": ["Imán", "Robustez"],
        "medida_pokemon": "S"
    },
    {
        "id_pokemon": 12,
        "nombre": "Voltorb",
        "tipo": "Electrico",
        "poder_de_ataque": 30,
        "poder_de_defensa": 50,
        "habilidades": ["Levitación", "Ráfaga"],
        "medida_pokemon": "S"
    },
    {
        "id_pokemon": 13,
        "nombre": "Electabuzz",
        "tipo": "Electrico",
        "poder_de_ataque": 83,
        "poder_de_defensa": 57,
        "habilidades": ["Electricidad Estática", "Espíritu Vital"],
        "medida_pokemon": "S"
    },
    {
        "id_pokemon": 14,
        "nombre": "Jolteon",
        "tipo": "Electrico",
        "poder_de_ataque": 65,
        "poder_de_defensa": 60,
        "habilidades": ["Absorber Electricidad", "Electricidad Estática"],
        "medida_pokemon": "XS"
    },
    {
        "id_pokemon": 15,
        "nombre": "Alakazam",
        "tipo": "Psiquico",
        "poder_de_ataque": 50,
        "poder_de_defensa": 45,
        "habilidades": ["Sincronía", "Cálculo"],
        "medida_pokemon": "XL"
    },
    {
        "id_pokemon": 16,
        "nombre": "Drowzee",
        "tipo": "Psiquico",
        "poder_de_ataque": 48,
        "poder_de_defensa": 45,
        "habilidades": ["Insomnio", "Imperturbable"],
        "medida_pokemon": "L"
    },
    {
        "id_pokemon": 17,
        "nombre": "Hypno",
        "tipo": "Psiquico",
        "poder_de_ataque": 73,
        "poder_de_defensa": 70,
        "habilidades": ["Insomnio", "Precognición"],
        "medida_pokemon": "M"
    },
    {
        "id_pokemon": 18,
        "nombre": "Cubone",
        "tipo": "Tierra",
        "poder_de_ataque": 50,
        "poder_de_defensa": 95,
        "habilidades": ["Cabeza Roca", "Pararrayos"],
        "medida_pokemon": "XL"
    },
    {
        "id_pokemon": 19,
        "nombre": "Diglett",
        "tipo": "Tierra",
        "poder_de_ataque": 55,
        "poder_de_defensa": 25,
        "habilidades": ["Velo Arena", "Trampa Arena"],
        "medida_pokemon": "M"
    },
    {
        "id_pokemon": 20,
        "nombre": "Golem",
        "tipo": "Tierra",
        "poder_de_ataque": 120,
        "poder_de_defensa": 130,
        "habilidades": ["Cabeza Roca", "Robustez"],
        "medida_pokemon": "XL"
    }
]


nombre_archivo = "pokemones.csv"
crear_csv(nombre_archivo)


while True:
    opcion = menu_de_usuario()
    match opcion:
        case "0":
            victoria = verificar_victoria(lista_pokemones)
            if victoria:
                print("¡Ganamos la batalla!")
            else:
                print("No tenemos suficientes pokemones para ganar.")
        case "1":
            #ingresar pokemones en la lista
            ingresar_pokemon(lista_pokemones) 
        case "2":
            #modificar pokemones
            id_pokemon = int(input("ingrese el id del pokemon: "))
            editar_pokemon(lista_pokemones, id_pokemon)
        case "3":
            # #eliminar pokemon 
            id_pokemon = int(input("ingrese el id del pokemon a eliminar: "))
            eliminar_pokemon(lista_pokemones, id_pokemon, lista_eliminados)
        case "4":
            #mostrar todos los pokemons
            mostrar_lista_pokemones(lista_pokemones)
        case "5":
            #ordenar los pokemons
            ordenar_pokemones(lista_pokemones)
            mostrar_lista_pokemones(lista_pokemones)
        case "6":
            #buscar pokemon por id y mostrar la informacion especifica
            id_pokemon = int(input("por favor ingrese el id del pokemon que desea buscar:"))
            buscar_pokemon_id(lista_pokemones, id_pokemon)
        case "7":
            #calcular promedios
            # calcular_promedios(lista_pokemones)
            mostrar_promedios(lista_pokemones)
        case "8":
            batalla_pokemon(lista_pokemones)

        case "9":
            guardar_json(lista_pokemones)
        case "10":
            
            guardar_pokemones(nombre_archivo, lista_pokemones)
            break
        
    system("pause")
    system("cls")