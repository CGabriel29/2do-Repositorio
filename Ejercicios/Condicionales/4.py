# Ejercicio 4-Categoria de conductores

nombre = input("Ingrese su nombre y apellido: ")
edad = int (input("Ingrese su edad: "))
años_exp = int(input("Ingrese años de experiencia conduciendo: "))

#Evaluar Condiciones

if edad < 18:
    resultado = "Menor de edad, no puede conducir."
elif edad >= 18 and años_exp < 1:
    resultado = "Principiante"
elif edad >= 21 and 1 <= años_exp <= 5:
    resultado = "Conductor Intermedio."
elif edad >= 39 and años_exp > 10:
    resultado = "Conductor Profesional."
else:
    resultado = "Conductor Estándar."

#Mensaje Resultado
print("----------------------------")
print("Conductor: ",nombre)
print("Edad: ",edad)
print("Años de experiencia: ",años_exp)
print("RESULTADO: ",resultado)