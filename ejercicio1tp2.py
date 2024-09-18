def mayor_estricto(a, b, c):
   
    es_mayor_a = (a > b) * (a > c)
   
    es_mayor_b = (b > a) * (b > c)
 
    es_mayor_c = (c > a) * (c > b)

    return (es_mayor_a * a) + (es_mayor_b * b) + (es_mayor_c * c)


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))


son_positivos = (a > 0) * (b > 0) * (c > 0)

if son_positivos:
    resultado = mayor_estricto(a, b, c)
    
    if resultado == 0:
        print("No existe el mayor estricto.")
    else:
        print("El mayor estricto es:", resultado)
else:
    print("Los números deben ser positivos.")
