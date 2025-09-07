#Ejercicio 3-Simulador de cajero automatico

nombre = input("Ingrese su nombre y apellido: ")
intentos = 0
PIN_correcto = 1234
while intentos < 3:
    PIN = int(input("Ingrese su PIN (máximo 3 intentos): "))
    if PIN != PIN_correcto:
        print("PIN incorrecto, por favor digite su PIN.")
        intentos += 1
    else:
        print("PIN correcto, Bienvenido.")
        break
if intentos == 3:
    print("Maximo numero de intentos permitidos.")
    exit()

# Proceso de retiro
saldo_inicial = 50000

while True:
    entrada = input("Ingrese el monto a retirar (o escriba 'cancelar' para salir): ")
    if entrada.lower() == "cancelar":
        print("Operacion cancelada por el usuario.")
        break
    if not entrada.isdigit():
        print("Entrada inválida. Debe ingresar un número.")
        continue
    retiro = int(entrada)
    if retiro % 1000 != 0:
        print("Solo se puede retirar un monto multiplo de 1000")
        continue
    elif retiro > saldo_inicial:
        print("El retiro no puede superar el saldo inicial.")
        continue
    if retiro > 20000:
        comision = retiro * 0.02
        total = retiro + comision
        if total > saldo_inicial:
            print("El retiro más la comisión supera el saldo disponible.")
            continue
        saldo_inicial -= total
        print(f"Retiro exitoso. Comisión aplicada: ${comision:.2f}")
    else:
        saldo_inicial -= retiro
        print("Retiro exitoso sin comisión.")

    print(f"Saldo actualizado: ${round(saldo_inicial, 2)}")
    break



