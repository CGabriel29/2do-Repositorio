# Ejercicio 2 - Gestion de turnos hospitalarios

nombre = input("Ingrese su nombre completo: ")
DNI = int(input("Ingrese su DNI: "))
while DNI < 0:
    print("Por favor ingrese un numero de DNI correcto.")
    DNI = int(input("Ingrese nuevamente su DNI: "))
edad = int(input("Ingrese su edad: "))
obra_social = input("Posee obra social? (si/no): ")
prioridad = int(input("Prioridad? (1 = emergencia, 2 = urgente, 3 = control): "))

#Evaluar Condicion
if prioridad == 1:
    turno_asignado = "Guardia"
elif prioridad == 2:
    if obra_social == "si":
        turno_asignado = "turno en menos de 24hs."
    else:
        turno_asignado = "turno en 48hs."
elif prioridad == 3:
    if edad > 65:
        turno_asignado = "turno preferencial en 72hs."
    else:
        turno_asignado = "turno normal en 7 dias."

# Presentar datos
print("--------------------------------------------")
print("Paciente: ", nombre)
print("DNI: ", DNI)
print("Edad: ", edad)
print("Prioriodad: ", prioridad)
print("Turno asignado: ", turno_asignado)  
print("--------------------------------------------")  