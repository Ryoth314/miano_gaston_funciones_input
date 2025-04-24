#MIANO GASTON
#DIV 117 TM
#FUNCIONES EJERCICIO MEDICINA

# def cargar_consulta(nombre_paciente: str, peso: float, 
# altura: float, temperatura: float,
# presion_sistolica: float, 
# presion_diastolica: float) -> None:

#     imc = peso / (altura ** 2)

#     if temperatura > 41:
#         fiebre = "Muy alta."
#     elif temperatura > 39:
#         fiebre = "Alta."
#     elif temperatura >= 38:
#         fiebre = "Fiebre moderada."
#     elif temperatura > 37.3:
#         fiebre = "Febrícula."
#     else:
#         fiebre = "Temperatura normal."

#     if imc < 18.5:
#         analisis_imc = "Es necesario aumentar ingesta calórica."
#     elif imc < 25:
#         analisis_imc = "Peso equilibrado."
#     else:
#         analisis_imc = "Es necesario disminuir ingesta calórica."

#     if presion_sistolica < 90 or presion_diastolica < 60:
#         analisis_presion = "Baja"
#     elif presion_sistolica > 140 or presion_diastolica > 90:
#         analisis_presion = "Alta"
#     else:
#         analisis_presion = "Normal"

#     diagnostico = f"""
# Diagnóstico del paciente {nombre_paciente}:
# Peso: {analisis_imc}
# Temperatura: {fiebre}
# Presión: {analisis_presion}
# """

#     print(diagnostico)

def analizar_temperatura(temperatura: float) -> str:
    analisis = ""
    if temperatura > 41:
        analisis = "Muy alta."
    elif temperatura > 39:
        analisis = "Alta."
    elif temperatura >= 38:
        analisis = "Fiebre moderada."
    elif temperatura > 37.3:
        analisis = "Febrícula."
    else:
        analisis = "Temperatura normal."
    return analisis

def analizar_imc(peso: float, altura: float) -> str:
    imc = peso / (altura ** 2)
    analisis = ""
    if imc < 18.5:
        analisis = "Es necesario aumentar ingesta calórica."
    elif imc < 25:
        analisis = "Peso equilibrado."
    else:
        analisis = "Es necesario disminuir ingesta calórica."
    return analisis

def analizar_presion(sistolica: float, diastolica: float) -> str:
    analisis = ""
    if sistolica < 90 or diastolica < 60:
        analisis = "Baja"
    elif sistolica > 140 or diastolica > 90:
        analisis = "Alta"
    else:
        analisis = "Normal"
    return analisis

def generar_mensaje_diagnostico(nombre: str, imc: str, 
                        fiebre: str, presion: str) -> str:
    diagnostico = ""
    diagnostico += f"\nDiagnóstico del paciente: {nombre}\n"
    diagnostico += f"Peso: {imc}\n"
    diagnostico += f"Temperatura: {fiebre}\n"
    diagnostico += f"Presión: {presion}\n"

    return diagnostico

def mostrar_dianostico(nombre_paciente: str, peso: float, altura: float, 
                    temperatura: float, presion_sistolica: float, 
                    presion_diastolica: float) -> None:
    
    resultado_imc = analizar_imc(peso, altura)
    resultado_temperatura = analizar_temperatura(temperatura)
    result_presion = analizar_presion(presion_sistolica, presion_diastolica)

    diagnostico = generar_mensaje_diagnostico(nombre_paciente, resultado_imc,
                                        resultado_temperatura, result_presion)
    print(diagnostico)

def generar_diagnostico_paciente()-> None:

    nombre = input("Ingrese su nombre: ")

    peso = float(input("Ingrese su peso: "))

    altura = float(input("Ingrese su altura: "))

    temperatura = float(input("Ingrese su temperatura: "))

    presion_sistolica = float(input("Ingrese su presión sistólica: "))

    presion_diastolica = float(input("Ingrese su presión diastólica: "))

    mostrar_dianostico(nombre, peso, altura, temperatura, presion_sistolica,
                        presion_diastolica)

generar_diagnostico_paciente()

