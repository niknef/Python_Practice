from random import randint

vida_inicial_pikachu = 80
vida_inicial_squirtle = 90
vida_actual_pikachu = 80
vida_actual_squirtle = 90

while vida_actual_pikachu > 0 or vida_actual_squirtle > 0:
    #COMBATE

    #Turno de Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)

    if ataque_pikachu == 1:
        #Bola Voltio
        print("Pikachu ataca con Bola Voltio\n")
        vida_actual_squirtle -= 10
    else:
        print("Pikachu ataca con Cola Ferrea\n")
        vida_actual_squirtle -= 11

    porcentaje_vida_pikachu = int((vida_actual_pikachu * 10) / vida_inicial_pikachu)
    barra_vida_pikachu = print("VIDA DE PIKACHU: " "[" + "#" * porcentaje_vida_pikachu + "]" + "{}%".format(porcentaje_vida_pikachu * 10))

    porcentaje_vida_squirtle = int((vida_actual_squirtle * 10) / vida_inicial_squirtle)
    barra_vida_squirtle = print("VIDA DE SQUIRTLE: " "[" + "#" * porcentaje_vida_squirtle + "]" + "{}%".format(porcentaje_vida_squirtle*10))

    input("Presiona ENTER para continuar..."
          "\n\n")

    #Turno Squirtle
    print("Turno de Squirtle")
    ataque_squirtle = None

    while ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "C":
        ataque_squirtle = input("¿Qué ataque eliges? [[A] Placaje  |  [B] Pistola Agua  |  [C] Burbuja]")

    if ataque_squirtle == "A":
        #Placaje
        print("Squirtle ataca con Placaje\n")
        vida_actual_pikachu -= 10
    elif ataque_squirtle == "B":
        #Pistola Agua
        print("Squirtle ataca con Pistola Agua\n")
        vida_actual_pikachu -= 12
    elif ataque_squirtle == "C":
        #Burbuja
        print("Squirtle ataca con Burbuja\n")
        vida_actual_pikachu -= 9

    porcentaje_vida_pikachu = int((vida_actual_pikachu * 10) / vida_inicial_pikachu)
    barra_vida_pikachu = print("VIDA DE PIKACHU: " "[" + "#" * porcentaje_vida_pikachu + "]" + "{}%".format(porcentaje_vida_pikachu * 10))

    porcentaje_vida_squirtle = int((vida_actual_squirtle * 10) / vida_inicial_squirtle)
    barra_vida_squirtle = print("VIDA DE SQUIRTLE: " "[" + "#" * porcentaje_vida_squirtle + "]" + "{}%".format(porcentaje_vida_squirtle * 10))

    input("Presiona ENTER para continuar..."
          "\n\n")

if vida_actual_pikachu > vida_actual_squirtle:
    print("PIKACHU GANA!")
else:
    print("SQUIRTLE GANA!")