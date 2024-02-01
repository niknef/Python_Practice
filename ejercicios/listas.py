lista_de_compras = []

print("\nPrograma lista de la compra\n")

while True:
    pregunta = input("¿Qué desea comprar? ([Q] para salir) => ")
    if pregunta not in "Q":
        if pregunta in lista_de_compras:
            print(f"El elemento {pregunta} ya se encuentra en la lista de compras.")
        elif pregunta not in lista_de_compras:
            confirmacion = input(f"Seguro que quieres añadir el elemento {pregunta} a tu lista? [S/N] => ")
            if confirmacion == "S":
                lista_de_compras.append(pregunta)
                print(f"Haz añadido el elemento '{pregunta}' a tu lista de compras!")
            elif confirmacion == "N":
                print(f"No haz añadido el elemento '{pregunta}' a tu lista de compras.")
            else:
                print("No haz seleccionado una de las opciones correspondientes.")
    elif pregunta == "":
        print("No haz escrito un elemento.")
    elif pregunta == "Q" and len(lista_de_compras) == 0:
        print("Tu lista de compras está vacia.")
    elif pregunta == "Q":
        print(f"Los elementos de la lista de compras son {lista_de_compras}")
        print("Gracias por usar nuestro programa!")
        break