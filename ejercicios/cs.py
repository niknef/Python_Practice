titulo = "Bienvenido a nuestro test sobre Counter-Strike:Global Offensive"
print("\n" + titulo + "\n" + "•" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: ¿A que resolución juegas al CS:GO?\n"
               "A - 16:9\n"
               "B - 16:10\n"
               "C - 4:3\n")

if opcion == "A":
    puntuacion += 5
elif opcion == "B":
    puntuacion += 0
elif opcion == "C":
    puntuacion += 10
else:
    print("Las posibles opciones son A, B y C, elige una de ellas perro.")
    exit()

opcion = input("Pregunta 2: ¿En qué mapa del map pool competitivo se encuentran distribuidas gallinas?\n"
               "A - Inferno\n"
               "B - Overpass\n"
               "C - Mirage\n")
if opcion == "A":
    puntuacion += 10
elif opcion == "B":
    puntuacion += 0
elif opcion == "C":
    puntuacion += 0
else:
    print("Las posibles opciones son A, B y C, elige una de ellas perro.")
    exit()

opcion = input("Pregunta 3: ¿Qué pistola eligirias para disputar un 1vs1?\n"
               "A - Glock 18\n"
               "B - Desert Eagle\n"
               "C - P250\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 10
elif opcion == "C":
    puntuacion += 5
else:
    print("Las posibles opciones son A, B y C, elige una de ellas perro.")
    exit()

opcion = input("Pregunta 4: ¿Como se denomina popularmente al arma más odiada de todo CS:GO?\n"
               "A - The MachineGun\n"
               "B - AutoNoob\n"
               "C - Water Gun\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 10
elif opcion == "C":
    puntuacion += 0
else:
    print("Las posibles opciones son A, B y C, elige una de ellas perro.")
    exit()

opcion = input("Pregunta 5: ¿Qué jugador competitivo es considerado uno de los padres del AWP?\n"
               "A - Stewie2K\n"
               "B - Olofmeister\n"
               "C - KennyS\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 0
elif opcion == "C":
    puntuacion += 10
else:
    print("Las posibles opciones son A, B y C, elige una de ellas perro.")
    exit()

if puntuacion == 50:
    print("Resultado: Felicidades, eres un gran conocedor del mundo de Counter-Strike:Global Offensive, ahora haznos un favor a todos y sal a conocer el mundo real.")
elif puntuacion == 45:
    print("Resultado: Felicidades, conoces gran parte de este maravilloso juego.")
elif puntuacion == 40:
    print("Resultado: Felicidades, se nota que te gusta el Counter-Strike:Global Offensive.")
elif puntuacion >=30:
    print("Resultado: Felicidades, ya sabes más que la mayoría de juadores de Valorant.")
elif puntuacion >=15:
    print("Resultado: Parece que juegas de vez en cuando pero te faltan horas (y calle).")
elif puntuacion == 0:
    print("Resultado: Colega, no has acertado ni una, haznos un favor a todos y juegate un par de partidas, luego vuelve a intentarlo.")
