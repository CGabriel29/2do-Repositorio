# Ejercicio 3 - Evaluacion de Credito Bancario

#Entrada de datos
nombre_apellido = input("Ingrese su nombre u apellido: ")
CUIT = input("Ingrese su CUIT (formato XX-XXXXXXXX-X): ")
while len(CUIT) != 13 or not CUIT.replace("-", "").isdigit():
    print("CUIT invalido, Ingrese un CUIT nuevamente: ")
    CUIT = input("Ingrese su CUIT (formato XX-XXXXXXXX-X): ")
ingresos = float(input("Ingrese sus ingresos mensuales: "))
antiguedad = int(input("Ingrese su antiguedad: "))
while antiguedad < 0:
    print("Antiguedad incorrecta.")
    antiguedad = int(input("Ingrese su antiguedad nuevamente: "))
historial = input("Ingrese su historial crediticio (bueno / regular / malo): ")

# Evaluar condicion
if historial == "malo":
    condicion = "Rechazado de Credito"
elif ingresos < 200000:
    condicion = "Rechazado por ingresos bajos"
elif ingresos >= 200000:
    if antiguedad < 2:
        condicion = "Puede pedir un credito de $500.000"
    else:
        if historial == "regular":
            condicion = "Puede pedir hasta $1.000.000" 
        elif historial == "bueno":
            condicion = "Puede pedir hasta $3.000.000"
#Salida de datos

print("--------------------------------------------")
print("Cliente: ",nombre_apellido)
print("CUIT: ",CUIT)
print("Ingresos: ",ingresos)
print("Antiguedad: ",antiguedad)
print("Historial: ",historial)
print("Resultado: ", condicion)