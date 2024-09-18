print('Universidad de Python - Inscripciones')

nombre= input('Ingrese su nombre: ')
edad= int(input('Ingrese su edad: '))
fecha_nac= input('Ingrese fecha de nacimiento (dd/mm/aaaa): ')

posee_titulo_secundario = True
monto_matricula= float(input('Ingrese el monto de la matricula: '))

cuota= monto_matricula + 1000
arancel_pythonI = 12000
cuota_mensual = cuota + arancel_pythonI / 4

pago_efectivo = input('¿El pago se realizara en efectivo? (si/no): ')
if pago_efectivo == 'si':
   descuento= 0.15
   cuota_descuento= cuota * (1- descuento)
else:
   cuota_descuento= cuota

print("Nombre Completo: ", nombre)
print("Fecha de nacimiento y edad:", fecha_nac)
print("Edad", edad)
print("Posee tirulo?: ", posee_titulo_secundario)
print("Matricula: ", monto_matricula)
print("Cuota mensual: ", cuota_mensual)
print("Arancel mensual materia 'Python I': ", cuota_mensual )
print("Arancel mensual materia 'Python I' con descuento: ", cuota_descuento )

   




