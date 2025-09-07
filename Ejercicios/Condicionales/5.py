#Ejercicio 5 - Simulador de carrito de compras

nombre = input("Ingrese su nombre: ")
cant_prod = int(input("Ingrese la cantidad de productos: "))
while cant_prod <= 0:
    print("Cantidad de productos incorecta.")
    cant_prod = int(input("Por favor digite una cantidad de productos correcta: "))

monto_compra = float(input("Ingrese el valor de su compra: "))
while monto_compra <= 0:
    print("Monto incorrecto.")
    monto_compra = float(input("Por favor digite un monto correcto: "))

medio_pago = input("Escriba su medio de pago (efectivo, debito, credito, mercado_pago): ")

#Reglas 
descuento = 0
recargo = 0
if medio_pago == "efectivo":
    descuento = monto_compra * 0.15
    monto_total = monto_compra - descuento
elif medio_pago == "debito":
    descuento = monto_compra * 0.10
    monto_total = monto_compra - descuento
elif medio_pago == "credito":
    recargo = monto_compra * 0.05
    monto_total = monto_compra + recargo
elif medio_pago == "mercado_pago":
    if monto_compra > 10000:
     descuento = monto_compra * 0.20
     monto_total = monto_compra - descuento
    else:
        monto_total = monto_compra

#Mas de 10 productos
descuento_extra = 0
if cant_prod > 10:
    descuento_extra = monto_total * 0.05
    monto_total = monto_total - descuento_extra
    
#Mostrar detalle final
print("-------------------------------------------")
print("RESUMEN DE COMPRA")
print("Cliente:", nombre)
print("Cantidad de productos:", cant_prod)
print("Monto original: $", round(monto_compra, 2))
print("Descuento aplicado: $", round(descuento, 2))
print("Recargo aplicado: $", round(recargo, 2))
print("Descuento extra por cantidad:", round(descuento_extra, 2))
print("Importe final a pagar: $", round(monto_total, 2))