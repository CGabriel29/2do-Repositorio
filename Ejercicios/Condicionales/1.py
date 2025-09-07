# Ejercicio 1-Clasificacion de impuestos

nombre = input("Ingrese su nombre y apellido: ")
edad = int(input("Ingrese su edad: "))
ingresos = float(input("Digite sus ingresos anuales: "))

#Reglas

if edad > 65:
    impuesto = "Impuesto reducido al 50%"
elif ingresos < 500000:
    impuesto = "No paga impuesto"
elif ingresos >= 500000 and ingresos < 2000000:
    impuesto = "Paga 10% de impuesto"
elif ingresos >= 2000000 and ingresos < 5000000:
    impuesto = "Paga 20% de impuesto"
else:
    impuesto = "Paga 35% de impuestos"
    
# Salida

print("______________________________")
print("Nombre y apellido: ", nombre)
print("Edad: ",edad)
print("Ingresos anuales: ",ingresos)
print("Impuesto final: ", impuesto)