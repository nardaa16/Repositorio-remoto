print("Aulas")

dia= int(input('Ingrese el numero del dia (1-Lunes a 6-Sabado): '))

if dia < 1 or dia > 6:
    print("Número de día inválido. Debe estar entre 1 y 6.")
    

if dia % 2 == 0:
     aula = "A-300"
else:
     aula = "A-315"

     print("Aula: ")


print("Descuentos y Estacionamiento")
turno = input("Ingrese el turno (Mañana, Tarde o Noche): ")
materias = int(input("Ingrese la cantidad de materias: "))
valor_cuota = float(input("El valor de la cuota es: "))


if turno == "tarde" and materias > 3:
        descuento = 0.25
else:
        descuento = 0.05

valor_descuento = valor_cuota * (1 - descuento)
print("El valor de la cuota con descuento es: ", valor_descuento)

medio_transporte = input("Ingrese el vehículo (Auto, Moto o Bicicleta): ")
    
if medio_transporte.lower() in ["auto", "moto"]:
        costo = 300
elif medio_transporte.lower() == "bicicleta":
        costo = 50
else:
    print("Vehículo no válido.")
    costo= None
    
if costo is not None:
    print(f"El costo de estacionamiento para {medio_transporte.capitalize()} es: {costo}")



    
    


