def validar_Cadena_Numeros(numero:str):
    """
    Valida que una cadena de caracteres sea un número.
    Devuelve True en caso de serlo, False si no lo es.
    """
    valido = True

    for caracter in numero:
        #Validación para casos de solamente "-"
        if i == 0 and caracter == "-":
            if len(numero) > 1:
                i = 1
                continue
            else:
                valido = False
                break

        if caracter >= "0" and caracter <="9":
            valido = True
        else:
            valido = False
            break

    return valido

def validar_Cadena_Numeros_Flotante(numero:str):
    """
    Valida que una cadena de caracteres sea un número flotante.
    Devuelve True en caso de serlo, False si no lo es.
    """
    i = 0

    punto = False
    negativo = False
    valido = True

    for caracter in numero:
        #Validación para casos de solamente "-" o "." y "-."
        if len(numero) > 1 and (i <= 1):
            if i == 0 and caracter == "-":
                negativo = True
                i += 1
                continue

            if caracter == ".":
                if (i == 0 or (i == 1 and negativo == True)) or punto == True:
                    valido = False
                    break
                else:
                    punto = True
                    continue

        if caracter >= "0" and caracter <="9":
            valido = True
            i += 1
        else:
            valido = False
            break

    return valido

# 1-Crear una función que le solicite al usuario el ingreso de un 
# número entero y lo retorne.
def solicitar_Numero(mensaje:str)->int:
    """
    Recibe una cadena de caracteres por parámetro.
    Pide un número y lo retorna.
    """

    numero = input(mensaje)

    while len(numero) < 1 or validar_Cadena_Numeros(numero) != True:
        print("No ingresaste un número válido.")
        numero = input(mensaje)

    numero = int(numero)

    return numero

# 2-Crear una función que le solicite al usuario el ingreso de un número 
# flotante y lo retorne.
def solicitar_Numero_Flotante(mensaje:str, mensaje_error:str)->float:
    """
    Recibe una cadena de caracteres por parámetro.
    Pide un número flotante y lo retorna.
    """
    numero = input(mensaje)
    
    while len(numero) < 1 or validar_Cadena_Numeros_Flotante(numero) != True:
        print(mensaje_error)
        numero = input(mensaje)

    numero = float(numero)

    return numero

# 3-Crear una función que le solicite al usuario el ingreso de una cadena y la
# retorne. 
def solicitar_Cadena(mensaje:str, mensaje_error:str)->str:
    """
    Pide una cadena de caracteres y la retorna.
    """
    cadena = input(mensaje)
    while len(cadena) <= 0:
        print(mensaje_error)
        cadena = input(mensaje)
    
    return cadena

# 4-Escribir una función que calcule el área de un rectángulo. La función 
# recibe la base y la altura y retorna el área. 
def calcular_Area_Rectangulo(base:float, altura:float)->float:
    """
    Recibe una base y una altura de un rectangulo,
    calcula el area y la retorna.
    """
    area = base * altura
    
    return area

# 5-Escribe una función que calcule el área de un círculo. La función debe 
# recibir el radio como parámetro y devolver el área.

def calcular_Area_Circulo(radio:float)->float:
    """
    Recibe el radio de un circulo. Calcula el area y la retorna.
    """
    area = 3.14 * (radio**2)
    
    return area

# 6-Crea una función que verifique si un número dado es par o impar. 
# La función debe imprimir un mensaje indicando si el número es par o impar.

def verificar_Par_Impar(numero:int)->None:
    """
    Recibe un número. Calcula y devuelve si el número es par o impar.
    """
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")
    

# 7-Crea una función que verifique si un número dado es par o impar. 
# La función retorna True si el número es par, False en caso contrario.

def verificar_Par_Impar_Booleano(numero:int)->bool:
    """
    Recibe un número. Calcula y retorna True si es par, caso contrario
    retorna False.
    """
    if numero % 2 == 0:
        retorno = True
    else:
        retorno = False
    
    return retorno

# 8-Define una función que encuentre el máximo de tres números. 
# La función debe aceptar tres argumentos y devolver el número más grande.

def encontrar_Maximo(numero_uno:int, numero_dos:int, numero_tres:int)->int:
    
    """
    Recibe 3 números. Compara cual es el mayor y lo retorna como entero.
    """
    
    if numero_uno > numero_dos and numero_uno > numero_tres:
        numero_maximo = numero_uno
    elif numero_dos > numero_tres:
        numero_maximo = numero_dos
    else:
        numero_maximo = numero_tres
    
    return numero_maximo
    

# 9-Diseña una función que calcule la potencia de un número. La función debe 
# recibir la base y el exponente como argumentos y devolver el resultado.

def calcular_Potencia(base:int, exponente:int)->int:
    """
    Recibe un número como base y otro como exponente. 
    Calcula y retorna la potencia de dichos valores.
    """
    resultado = base ** exponente
    
    return resultado

# 10-Crear una función que reciba un número y retorne True si el número 
# es primo, False en caso contrario.

def calcular_Primo(numero:int)->bool:
    """
    Recibe un número entero por parametro, calcula si es o no un número primo.
    Retorna True en caso de serlo, sino False.
    """
    retorno = True

    if numero <= 1:
        retorno = False
        
    else:
        for n in range(2, numero):
            if numero % n == 0:
                retorno = False
                break
        
    return retorno

# 11-Crear una función que (utilizando el algoritmo del ejercicio 
# de la guia de for), muestre todos los números primos comprendidos 
# entre la unidad y un número ingresado como parámetro. 
# La función retorna la cantidad de números primos encontrados. 
# Modularizar todo lo posible.

def mostrar_Primos(numero:int)->int:
    """
    Recibe un número entero por parámetro. Muestra por pantalla cada número
    primo comprendido entre 1 y dicho número, y a su vez retorna la cantidad
    de números primos que encuentre. 
    """
    
    cantidad = 0
    
    for numero in range(2, numero+1):
        if calcular_Primo(numero) == True:
            print(numero)
            cantidad += 1
    
    return cantidad

# 12-Crear una función que imprima la tabla de multiplicar 
# de un número recibido como parámetro. La función debe aceptar
# parámetros opcionales (inicio y fin) para definir el rango 
# de multiplicación. Por defecto es del 1 al 10.

def imprimir_Tabla_Multiplicar(numero:int, inicio:int=1, fin:int=10)->None:
    """
    Recibe  por parametro 3 enteros,un número a multiplicar, 
    un inicio(opc) y fin(opc) como rango de multiplicación.
    Calcula y muestra en pantalla la tabla de multiplicar de dicho número.
    """
    for n in range(inicio, fin + 1):
        resultado = numero * n
        print(f"{numero}*{n} = {resultado}")

# 13-Especializar las funciones del punto 1, 2 y 3 para 
# hacerlas reutilizables.Agregar validaciones.
