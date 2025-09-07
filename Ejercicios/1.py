# Ejercicio 1: Sistema de becas estudiantiles

nombre_apellido = input("Ingrese su nombre y apellido: ")
edad = int(input("Ingrese su edad: "))
while edad <= 18 or edad > 120:
    print("Edad invalida, ingrese una edad entre 18 y 120.")
    edad = int(input("Ingrese su edad nuevamente: "))
promedio = float(input("Ingrese su promedio: "))
while promedio < 0 and promedio >= 10:
    print("Promedio invalido, ingrese un promedio entre 0 y 10.")
    promedio = float(input("Ingrese su promedio nuevamente: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))
while ingresos < 0:
    print("Ingreso invalido, ingrese un dato mayor a 0.")
    ingresos = float(input("Ingrese sus ingresos nuevamente: "))

# Casos

if promedio < 6:
    Resultado = "Rechazado"
else:
   if ingresos < 300000:
       Resultado = "Beca Completa"
   elif ingresos <= 600000:
       Resultado = "Media Beca"
   else:
       Resultado = "Rechazado"    

# Resultado

print("Nombre: ", nombre_apellido, ",", edad, " años")
print("Promedio: ", promedio)
print("Ingresos: $", ingresos)
print("Resultado: ", Resultado)
