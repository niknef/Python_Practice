import os
from random import randint

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

TAMAÑO_BARRA_VIDA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE


while vida_pikachu > 0 and vida_squirtle > 0:
    # Los turnos de combate se desarrollan aquí

    # Turno de Pikachu
    print("Turno de Pikachu")
    print("-" * 98)
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con Bola Voltio")
        print("-" * 98)
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        print("-" * 98)
        vida_squirtle -= 11

    vida_squirtle = max(0, vida_squirtle)  # Asegurarse de que la vida no sea negativa

    barras_de_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] ({}/{})".format("#" * barras_de_vida_pikachu, " " *
                                              (TAMAÑO_BARRA_VIDA - barras_de_vida_pikachu), vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:    [{}{}] ({}/{})".format("#" * barras_de_vida_squirtle, " " * (TAMAÑO_BARRA_VIDA - barras_de_vida_squirtle),
                                              vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...")
    os.system("cls")

    # Turno de Squirtle
    print("-" * 98)
    print("Turno de Squirtle")
    print("-" * 98)

    ataque_squirtle = None

    while ataque_squirtle not in ["P", "A", "B", "N"]:
        ataque_squirtle = input("¿Qué ataque deseas realizar? [P - Placaje | A - Agua | B - Burbuja | N - No atacar]: ")

        if ataque_squirtle == "P":
            vida_pikachu -= 10
            print("-" * 98)
            print("Squirtle ataca con Placaje")
        elif ataque_squirtle == "A":
            print("-" * 98)
            print("Squirtle ataca con Pistola de agua")
            vida_pikachu -= 12
        elif ataque_squirtle == "B":
            print("-" * 98)
            print("Squirtle ataca con Burbuja")
            vida_pikachu -= 9
            print("-" * 98)
        elif ataque_squirtle == "N":
            print("-" * 98)
            print("Squirtle decide no atacar este turno.")
            print("-" * 98)

    vida_pikachu = max(0, vida_pikachu)  # Asegurarse de que la vida no sea negativa

    barras_de_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] ({}/{})".format("#" * barras_de_vida_pikachu, " " *
                                              (TAMAÑO_BARRA_VIDA - barras_de_vida_pikachu), vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:    [{}{}] ({}/{})".format("#" * barras_de_vida_squirtle, " " * (TAMAÑO_BARRA_VIDA - barras_de_vida_squirtle),
                                              vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    print("Enter continuar....")
    os.system("cls")

if vida_pikachu > vida_squirtle:
    print("-" * 98)
    print("Pikachu gana")
    print("-" * 98)
else:
    print("-" * 98)
    print("Squirtle gana")
    print("-" * 98)