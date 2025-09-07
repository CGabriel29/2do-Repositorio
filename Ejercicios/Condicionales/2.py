# Ejercicio 2-Sistema de calificaciones con promocion

nombre = input("Ingrese nombre y apeliido: ")
legajo = int (input("Ingrese numero de legajo: "))
print("Ingrese 3 notas: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

promedio = (nota1+nota2+nota3)/3

# Condiciones

if nota1 < 4 or nota2 < 4 or nota3 < 4:
    estado = "Desaprobado directo"
elif promedio < 6:
    estado = "Desaprobado"
elif 6 <= promedio <= 7:
    estado = "Aprobado con final"
else:
    estado = "Promocionado"
    
#Resultados
print("-----------------------------")
print("\033[94mNombre y apellido del Alumno:\033[0m", nombre)
print("\033[96mLegajo:\033[0m", legajo)
print("\033[93mPromedio:\033[0m", round(promedio, 2))
print("\033[92mEstado académico final:\033[0m", estado)

