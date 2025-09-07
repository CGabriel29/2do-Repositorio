# Ejercicio 9

monto_solicitado = float(input("Ingrese el monto solicitado: "))

i = 0.02
n = 12

cuota = monto_solicitado * (i * (1 + i)**n) / ((1 + i)**n - 1)

monto_total = cuota * 12

print("El monto TOTAL a devolver es: ", round (monto_total,2))
print("El valor de cada couta mensual es: ", round(cuota,2))
