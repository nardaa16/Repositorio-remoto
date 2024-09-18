nota1= float(input('Ingrese la nota del primer parcial: '))
nota2= float(input('Ingresela nota del segundo parcial: '))

promedio= (nota1 + nota2 )/ 2
print("El promedio de las notas es:", promedio)

if nota2 >= 7 :
    print("Aprobo el ultimo parcial")
else:
    print("Desaprobo el ultimo parcial")

if nota2 == nota1:
    print("Progreso del 1er al 2do parcial: Mantuvo la nota")
elif nota2 > nota1:
    print("Progreso del 1er al 2do parcial: Mejoro su desempeño")
else:
    print("Progreso del 1er al 2do parcial: Empeoro su desempeño")

if promedio >= 7:
    print("Promociono la materia")
elif promedio >= 4:
    print("Debe rendir final")
else:
    print("Debe recursar")



