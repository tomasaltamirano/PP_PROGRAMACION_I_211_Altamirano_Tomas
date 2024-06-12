from validate import validate_number, validate_lenght

def get_int(mostar_mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) ->int|None:
    numero = int(input(mensaje_error))
    resultado = validate_number(numero, mensaje_error, minimo, maximo, reintentos)
    
    return resultado

# print(get_int("Por favor, ingrese un número entre 0 y 150: ", "El número ingresado excede el limite, probá de nuevo: ", 1, 10, 3))

def mostrar_mensaje(mensaje):
    print(mensaje)
    
    
    
# def get_string(mensaje_entrada:str, 
#                mensaje_error:str, 
#                longitud:int, 
#                reintentos:int)->str|None: 
#     mensaje_entrada = input(mensaje)
    
#     caracteres_ingresados = validate_lenght(mensaje_entrada,mensaje_error,longitud,reintentos)

#     return caracteres_ingresados

# mensaje = "Por favor ingrese un mensaje que no supere los 10 caracteres: "
# mensaje_error = "El mensaje supera los caracteres maximos"
# longitud = 10
# reintentos = 2

# print(get_string(mensaje, mensaje_error, longitud, reintentos))
    
