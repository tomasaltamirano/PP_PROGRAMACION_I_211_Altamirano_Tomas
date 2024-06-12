def validate_number(numero:int|str, 
                    mensaje_error:str, 
                    minimo:int, 
                    maximo:str, 
                    reintentos:str)->int|float|None:
    match numero:
        case int():
            for _ in range(reintentos):
                if numero <= minimo or numero >= maximo:
                    numero = int(input(mensaje_error))
                    resultado = None
                else:
                    resultado = numero
                    break
        case float():
            for _ in range(reintentos):
                if numero <= minimo or numero >= maximo:
                    numero = float(input(mensaje_error))
                    resultado = None
                else:
                    resultado = numero
                    break
    
    return resultado 

def validate_lenght(mensaje_entrada:str, mensaje_error:str, longitud:str, reintentos:int) -> str|None:
    for _ in range(reintentos):
        if len(mensaje_entrada) >= longitud:
            caracteres_ingresados = None
            mensaje_entrada = input(mensaje_error)
            
        else:
            caracteres_ingresados = mensaje_entrada
            break
    
    return caracteres_ingresados
            

