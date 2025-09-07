# Ejercicio 7

dolares = float(input("Ingrese la cantidad de dolares que desea convertir: "))

# TASAS
tasa_col= 4002.50 # 1 dólar = 4.002,50 pesos colombianos
tasa_arg = 1361.00 # 1 dólar = 1.361,00 pesos argentinos
tasa_euro = 0.86  # 1 dólar = 0,86 euros


peso_colombiano = dolares*tasa_col
peso_argentino = dolares*tasa_arg
euros = dolares*tasa_euro

print(f"La conversion de {dolares} dolares a peso colombiano es: ", peso_colombiano)
print(f"La conversion de {dolares} dolares a peso argentino es: ", peso_argentino)
print(f"La conversion de {dolares} dolares a euro es: ", euros)

