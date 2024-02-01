import random

numero_random = random.randint(0, 100)

print("---------------------------------------------------------\n"
      "Bienvenido a la Mazmorra de las Decisiones.\n"
      "Te encuentras en una oscura y misteriosa cueva, y el eco de tus pasos resuena en las paredes húmedas. \n"
      "A medida que avanzas, te das cuenta de que el camino se divide en dos direcciones. \n"
      "Dos puertas macizas se alzan frente a ti. \n")

print("Puerta de la Sombra: \n"
      "Emana un brillo tenue y unas débiles sombras danzan a su alrededor.\n"
      "Parece invitar a los valientes a descubrir los secretos que se esconden en su interior.\n")

print("Puerta de la Oscuridad: \n"
      "Cubierta por una neblina oscura que parece absorber la luz. Un aura de misterio y desafío rodea esta entrada. \n"
      "Indicando peligros y desafíos inminentes.")

opcion = input("¿Qué camino deseas recorrer?\n"
               "A - Puerta de la Sombra.. \n"
               "B - Puerta de la Oscuridad.. \n")

if opcion == "A":
      print("Haz elegido la puerta de la SOMBRA. \n"
            "Al abrir la Puerta de la Sombra, te sumerges en una sala iluminada por tenues antorchas. \n"
            "De repente, un misterioso personaje, el Guardián de las Sombras, aparece y Ofrece un trato:\n"
            "Responder correctamente a sus acertijos o enfrentar las consecuencias.\n"
            "Tienes que elegir entre confiar en tu astucia o huir.\n")

      opcion = input("A - Resuelvo el acertijo \n"
                     "B - Huir \n")
      if opcion == "A":
            print(" -Guardian de las sombras:\n"
                  "Felicitaciones eres un valiente pero igual deberas resolver mi acertijo para continuar: \n"
                  "Para avanzar deber decirme el codigo secreto, realiza la siguiente cuenta para conocerlo.. \n"
                  "10*{}".format(numero_random))
            resultado = float(input("Ingrese el codigo: "))

            if (10 * numero_random) == resultado:
                  print("Felicitaciones haz tu codigo es el correcto. \n"
                        "Continuas el camino de las sombras..")
                  maso_combate = False
                  opcion = input("Mientras avanzas por el camino te encuentras un maso de combate.. \n"
                                 "Lo agarras? [S/N]")
                  if opcion == "S":
                        maso_combate = True
                  elif opcion == "N":
                        maso_combate = False

                  if maso_combate == True:
                        print("Te topaste con el jefe final y pudiste vencerlo gracias a tu maso. \n"
                              "Enorabuena Superaste la mazmorra con exito!")
                        exit()
                  elif maso_combate == False:
                        print("Te topaste con el jefe final y te destrozo ¨Haz Muerto¨")
                        exit()

            else:
                  print("El guardian de las sombras te mata por no ser digno. ¨Haz Muerto¨")
                  exit()

      elif opcion == "B":
            barreta = False
            opcion = input("huyes y te tropiesas con una barreta \n"
                           "La agarras? [S/N]")

            if opcion == "S":
                  barreta = True

            elif opcion == "N":
                  barreta = False

            if barreta == True:
                  print("Encontraste una puerta en el camino y usaste la barreta para abrirla. \n"
                        "Enorabuena Superaste la mazmorra con exito!")
                  exit()
            elif barreta == False:
                  print("Llegas al final del camino y el guardian te persiguio y te mato. ¨Haz Muerto¨")
                  exit()


elif opcion == "B":
      print("Haz elegido la puerta de la OSCURIDAD, la cual tiene un pase a la victoria, GANASTE")
      exit()


else:
      print("Al no seleccionar una puerta a tiempo, tu luz fue consumida ¨Haz Muerto¨")
      exit()