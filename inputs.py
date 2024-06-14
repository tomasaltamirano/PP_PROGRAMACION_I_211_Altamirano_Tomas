from mensajes import mensajes_genericos

def get_string(mensaje: str, mensaje_error: str, longitud_maxima: int, reintentos: int) -> str | None:
    for _ in range(reintentos):
        entrada_usuario = input(mensaje)
        if len(entrada_usuario) > longitud_maxima:
            print(mensaje_error + f" (máximo {longitud_maxima} caracteres)")
        elif not entrada_usuario[0].isupper():
            print(mensaje_error + " (primer caracter debe ser mayuscula)")
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




