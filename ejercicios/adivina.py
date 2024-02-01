import random

numero_secreto = random.randint(1, 10)

numero_usuario = int(input("Por favor, adivina un número del 1 al 10: "))

if numero_usuario == numero_secreto:
    print("¡Enhorabuena! Has adivinado el número.")
else:
    print("Lo siento, no has adivinado el número. El juego ha terminado.")