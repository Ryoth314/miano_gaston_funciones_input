from Validate import *

def get_int(mensaje: str, mensaje_error: str, minimo: int, 
            maximo: int, reintentos: int) -> int|None:
    """
    Recibe dos strings, uno para mensaje y otro para mensaje de error,
    3 enteros que representan un minimo, un maximo y cantidad de intentos.
    Retorna el numero si es válido, None si se usaron la cantidad de 
    reintentos.
    """

    contador = 0

    print(f"Cantidad de intentos: {reintentos + 1}")

    numero = int(input(mensaje))
    valido = validate_number(numero, minimo, maximo)

    while valido != True:
        
        contador += 1
        
        if contador > reintentos:
            numero = None
            break

        else:
            print(mensaje_error)
            print(f"Reintento N°: {contador}")
            numero = int(input(mensaje))
            valido = validate_number(numero, minimo, maximo)

    return numero

def get_float(mensaje: str, mensaje_error: str, minimo: float, 
            maximo: float, reintentos: int) -> float|None:
    """
    Recibe dos strings, uno para mensaje y otro para mensaje de error,
    3 flotantes que representan un minimo, un maximo y cantidad de intentos.
    Retorna el numero si es válido, None si se usaron la cantidad de 
    reintentos.
    """

    contador = 0
    print(f"Cantidad de intentos: {reintentos + 1}")
    numero = float(input(mensaje))
    valido = validate_number(numero, minimo, maximo)

    while valido != True:
        
        contador += 1
        
        if contador > reintentos:
            numero = None
            break

        else:
            print(mensaje_error)
            print(f"Reintento N°: {contador}")
            numero = float(input(mensaje))
            valido = validate_number(numero, minimo, maximo)

    return numero

def get_string(mensaje: str,mensaje_error: str, 
                longitud: int, reintentos: int) -> str|None:

    """
    Recibe 2 strings, uno para mensaje y otro para mensaje de error,
    y 2 enteros que representan la longitud maxima de la cadena y
    la cantidad de reintentos que tiene.
    Retorna la cadena si es menor a la longitud maxima, caso contrario
    None si se acabaron los reintentos.
    """

    contador = 0

    cadena = input(mensaje)
    valido = validate_length(cadena, longitud)

    while valido != True:

        contador += 1

        if contador == reintentos:
            cadena = None
            break
        
        else:    
            print(mensaje_error)
            cadena = input(mensaje)
            valido = validate_length(cadena, longitud)
    
    return cadena