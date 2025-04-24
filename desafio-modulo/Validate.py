
def validate_number(numero:float, minimo:float, maximo:float) -> bool:
    
    if numero > maximo or numero < minimo:
        valido = False
    else:
        valido = True
    
    return valido

def validate_length(cadena:str, longitud: int) -> bool:

    if len(cadena) > longitud or len(cadena) < 1:

        valido = False
    else:
        valido = True

    return valido