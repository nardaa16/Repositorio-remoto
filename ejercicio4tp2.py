nombre_comprador = input("Ingrese su nombre: ")
nombre_empresa = "Zapallos S.A."
tipo_moneda = input("Ingrese el tipo de moneda (dolares, yenes, guaranies, pesos): ").lower()
cantidad = int(input("Ingrese la cantidad de zapallos: "))

COSTO_ZAPALLO = 1000
DESCUENTOS = {
    'dolares': 0.05,
    'yenes': 0.15,
    'guaranies': 0.20,
    'pesos': 0.10
}
AUMENTO = 0.10


costo_total = cantidad * COSTO_ZAPALLO
if tipo_moneda in DESCUENTOS:
    descuento = DESCUENTOS[tipo_moneda]
    precio_final = costo_total * (1 - descuento)
    tipo_desc = "Descuento"
    monto_desc = costo_total * descuento
else:
    incremento = AUMENTO
    precio_final = costo_total * (1 + incremento)
    tipo_desc = "Incremento"
    monto_desc = costo_total * incremento


print("\n----- RECIBO -----")
print(f"Nombre del Comprador: {nombre_comprador}")
print(f"Nombre de la Empresa: {nombre_empresa}")
print(f"Tipo de Moneda: {tipo_moneda.capitalize()}")
print(f"{tipo_desc}: ${monto_desc:.2f}")
print(f"Cantidad: {cantidad} zapallo(s)")
print(f"Precio Total en Pesos: ${precio_final:.2f}")
