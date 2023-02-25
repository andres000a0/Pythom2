# pedir datos del dia y el mes
dia = int(input("Ingrese el día (1-31): "))
mes = int(input("Ingrese el mes (1-12): "))

#funcion 
def obtener_estacion(mes, dia):
    if (mes == 0 or dia == 0 ):
        return print(f'El mes {mes} o el dia {dia} no pueden ser 0')
#inicio Invierno    
    elif (mes == 12 and dia > 21 and dia == 31) or (mes == 1 and dia >= 1 and dia <= 31) or (mes == 2 and dia <= 1 and dia <= 28) or (mes == 3 and dia >=1 and dia <= 20):
        estacion = "Invierno"
#inico del primavera
    elif (mes == 3 and dia >= 21 and dia <= 31) or (mes == 4 and dia >= 1 and dia <= 30) or (mes == 5 and dia >= 1 and dia <= 31) or (mes == 6 and dia >=1 and dia <= 21):
        estacion = "Primavera"
#inicio Verano
    elif (mes == 6 and dia >= 1 and dia <= 30) or (mes == 7 and dia >= 1 and dia <= 31) or (mes == 8 and dia >= 1 and dia <= 31) or (mes == 9 and dia >= 1 and dia <= 23):
        estacion = "Verano"
#inicio Otoño       
    elif (mes == 9 and dia >= 24 and dia <= 30) or (mes == 10 and dia >= 1 and dia <= 31) or (mes == 11 and dia >= 1 and dia <= 30) or (mes == 12 and dia >= 1 and dia <= 21):
        estacion = "Otoño"
    else:    
        estacion = "fecha inválida"
    return estacion
estacion = obtener_estacion(mes, dia)
print(f"La fecha {dia}/{mes} corresponde a la estación {estacion}")
