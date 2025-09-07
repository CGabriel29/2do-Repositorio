# Ejercicio 8: Viaje en auto

distancia = float(input("Ingrese la distancia en KM que recorrio: "))
precio_gasolina = float(input("Ingrese precio de gasolina X litro: "))

litros_usados = (distancia/100) * 8
costo_viaje = litros_usados * precio_gasolina
tiempo_viaje = distancia / 90

print("Los litros usados son: ", litros_usados)
print("El costo de viaje es: ", costo_viaje)
print(f"El tiempo de viaje es: " , round (tiempo_viaje,2), "horas")