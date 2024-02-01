opcion = input("¿Qué sistema operativo prefieres? \n"
               "A - IOs \n"
               "B - Android \n")

if opcion == "A":
    opcion = input("¿Tienes dinero? \n"
                   "A - No tengo \n"
                   "B - Si tengo \n")
    if opcion == "A":
        print("Usted deberia comprar un iphone de segunda mano")
    elif opcion == "B":
        print("Usted deberia comprar un Iphone Ultra Pro Max")
    else:
        print("No selecciono ninguna opcion valida")

if opcion == "B":
    opcion = input("¿Tienes dinero? \n"
                   "A - No tengo \n"
                   "B - Si tengo \n")
    if opcion == "A":
        print("Usted deberia comprar un Android chino de $100")
    elif opcion == "B":
        opcion = input("¿Le importa la camar? \n"
                       "A - No me interesa \n"
                       "B - Si me interesa \n")
        if opcion == "A":
            print("Usted deberia comprar un android calidad-precio")
        elif opcion == "B":
            print("Usted deberia comprar el Google pixel Supercamera")
        else:
            print("No selecciono ninguna opcion valida")

    else:
        print("No selecciono ninguna opcion valida")