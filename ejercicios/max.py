

numeros_introducidos = input("introduzca los numeros separados por coma: ")
numeros_procesados = [int(numero) for numero in numeros_introducidos.split(",")]

print("El numero mas grande es: ")
print(max(numeros_procesados))
print("Y el numero mas pequeño es: ")
print(min(numeros_procesados))

