dia= int(input('Ingrese el dia: '))
mes= int(input('Ingrese el mes: '))
año= int(input('Ingrese el año: '))

es_valida= True

if año <= 0 or mes <= 0 or dia <= 0:
    es_valida = False
elif mes > 12:
    es_valida = False
else:
    
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
        dias_por_mes[2] = 29

   
    if dia > dias_por_mes[mes]:
        es_valida = False

print(f"Fecha: {dia}/{mes}/{año} - Válida: {es_valida}")
