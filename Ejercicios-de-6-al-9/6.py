# Ejercicio 6

parcial1 = float(input("Ingrese la primera nota parcial: "))
parcial2 = float(input("Ingrese la segunda nota parcial: "))
parcial3 = float(input("Ingrese la tercera nota parcial: "))

promedio_parciales = (parcial1+parcial2+parcial3) / 3


examen_final = float(input("Ingrese nota de examen final: "))
trabajo_final = float(input("Ingrese nota de trabajo final: "))

nota_parciales = promedio_parciales * 0.55
nota_examen = examen_final * 0.33
nota_trabajo = trabajo_final * 0.15

# NOTA FINAL

nota_final = nota_parciales + nota_examen + nota_trabajo

print("La calificacion FINAL en Algoritmos es: ", nota_final)
