lista_numeros = []

numero_user = int(input("Introduzca un numeros: "))
lista_numeros.append(numero_user)

while input("Desea introducir más numero (S/N): ") == "S":
    numero_user = int(input("Introduzca los numeros: "))
    lista_numeros.append(numero_user)

num_max = print("El número más grande es {}".format(max(lista_numeros)))
num_min = print("El numero más pequeño es {}".format(min(lista_numeros)))
