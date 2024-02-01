titulo = "Bienvenido a nuestro test para saber que tipo de moto comprar: "
print(f"\n<{titulo}\n{'-' * len(titulo)}>\n")

tierra = 0
pista = 0
touring = 0

opcion = input("Pregunta 1: ¿Que hago si veo un camino de tierra? \n "
               "A - Me meto sin dudarlo \n "
               "B - Me lo planteo \n "
               "C - No entro por nada en el mundo \n")

if opcion == "A":
    tierra += 1
elif opcion == "B":
    touring += 1
elif opcion == "C":
    pista += 1
else:
    print("Las opciones son A B y C")
    exit()

opcion = input("Pregunta 2: ¿Que tipo de ruta elegirias? \n "
               "A - Todo Campo y barro \n "
               "B - Una que mezcle un poco de campo con un poco de carretera \n "
               "C - Todo carretera \n")

if opcion == "A":
    tierra += 1
elif opcion == "B":
    touring += 1
elif opcion == "C":
    pista += 1
else:
    print("Las opciones son A B y C")
    exit()

opcion = input("Pregunta 3: ¿Que preferis en una moto? \n "
               "A - Agilidad \n "
               "B - Comodidad \n "
               "C - Velocidad \n")

if opcion == "A":
    tierra += 1
elif opcion == "B":
    touring += 1
elif opcion == "C":
    pista += 1
else:
    print("Las opciones son A B y C")
    exit()

if tierra > touring and tierra > pista:
    print("Felicidades tu moto ideal seria una moto trial")
elif touring > tierra and touring > pista:
    print("Felicidades tu moto ideal seria una touring")
elif pista == tierra:
    print("Felicidades tu moto ideal seria una touring")
else:
    print("Felicidades tu moto ideal seria una de pista")