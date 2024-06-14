
def get_string(mensaje: str, mensaje_error: str, longitud_maxima: int, reintentos: int) -> str | None:
    for _ in range(reintentos):
        entrada_usuario = input(mensaje)
        if len(entrada_usuario) > longitud_maxima:
            print(mensaje_error + f" (máximo {longitud_maxima} caracteres)")
        elif not entrada_usuario[0].isupper():
            print(mensaje_error + " (el primer caracter debe ser mayuscula y no debe ser un numero)")
        else:
            return entrada_usuario
    # print(mensaje_error + " (excedió el número de reintentos)")
    # return None

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    for _ in range(reintentos):
        numero_str = input(mensaje)
        if "." in numero_str:
            print("no se permiten numeros flotantes")
            continue
        numero = int(numero_str)
        if minimo <= numero <= maximo:
            return numero
    print(mensaje_error)
    # return None
    

lista_tipos = ["Agua", "Bicho", "Dragon", "Electrico", "Fantasma", "Fuego",
        "Hielo", "Lucha", "Normal", "Planta", "Psiquico", "Roca",
        "Tierra", "Veneno", "Volador"]

def get_tipo(tipos_pokemon: str,lista_tipos: list):
    while True:
        for tipo in lista_tipos:
            ingresar_tipo = input("Ingresa un tipo para tu pokemon: ")
            if ingresar_tipo in lista_tipos:
                return ingresar_tipo
            else:
                print("el tipo que ingresaste no es valido")
    

def get_menus(opciones: str, lista_opciones: list):
    for _ in range(len(lista_opciones)):
        opcion_str = input(opciones)
        if "." in opcion_str:
            print("no se permiten numeros flotantes")
            continue
        opcion = int(opcion_str)
        if opcion in lista_opciones:
            return opcion
        




