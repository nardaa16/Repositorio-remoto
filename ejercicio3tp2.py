total_compra = int(input('Ingrese el total de la compra: '))
dinero_recibido = int(input('Ingrese el total de dinero recibido: '))

denominaciones = [500, 100, 50, 20, 10, 5, 1]

if dinero_recibido < total_compra:
    print("ERROR: Dinero recibido insuficiente.")
else:
    vuelto = dinero_recibido - total_compra
    print(f"El vuelto es: ${vuelto}") 

    cambio = {}

    for billete in denominaciones:
        if vuelto >= billete:
            cantidad_billetes = vuelto // billete
            vuelto -= cantidad_billetes * billete
            cambio[billete] = cantidad_billetes

    print("Billetes a entregar:")

    for billete, cantidad in cambio.items():
        if cantidad > 0:
            print(f"${billete}: {cantidad} billete(s)")
