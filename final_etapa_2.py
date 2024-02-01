import os
import readchar
import random

TITLE = "Pokemon Challenge"
POS_X = 0
POS_Y = 1
LIFE_BAR_SIZE = 20
NUM_OF_COACHS = 5
POKEMON_MAP = """\
         #################
###           ############
#########        #########
##############     #######
#############   #   ######
#############      #######
###            ###########
#######  ###         #####
###########    ####    ###
########     ######     ##
#####    ##########   ####
######     ########      #
#########    #######    ##
############           ###
###             ##########
###           ############
#     ####################
###       ################
#####         ############
##########        ########
################          \
"""

POKEMON_MAP = [list(row) for row in POKEMON_MAP.split("\n")]

MAP_WIDTH = len(POKEMON_MAP[0])
MAP_HEIGHT = len(POKEMON_MAP)

my_position = [0, 0]
map_coachs = []
coach_defeat = 0
title_space = int((MAP_WIDTH - len(TITLE)) / 2)
end_game = False

# Pikachu life
INITIAL_LIFE_PIKACHU = 80
pikachu_life = INITIAL_LIFE_PIKACHU

# Enemies

trainers_and_pokemons = [
    ["Mysty", "Squirtle", [["Water Gun", 8], ["Bubble Beam", 6]], 90, 90],
    ["Brock", "Charizard", [["Flamethrower", 7], ["Dragon Claw", 9]], 100, 100],
    ["Lt. Surge", "Jolteon", [["Thunder Shock", 4], ["Double Kick", 10]], 50, 50],
    ["Blaine", "Blastoise", [["Hydro Pump", 5], ["Surf", 8]], 65, 65],
    ["Snorlax Trainer", "Snorlax", [["Body Slam", 12], ["Rest", 3]], 70, 70]
]

# My Atacks
pikachu_attacks = ["T", "Q", "I"]


# Clear console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Coach positions create
while len(map_coachs) < NUM_OF_COACHS:
    new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

    if new_position not in map_coachs and new_position != my_position and \
            POKEMON_MAP[new_position[POS_Y]][new_position[POS_X]] != "#":
        map_coachs.append(new_position)

# main loop
while not end_game:

    print("\n{} {} {}".format("-------" * title_space, TITLE, "-------" * title_space))
    print("\n{}  Coach Defeats: {}/5\n".format("       " * title_space, coach_defeat))
    print("Use W,A,S,D to move")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_Draw = " "
            object_in_cell = None

            for map_coach in map_coachs:
                if map_coach[POS_X] == coordinate_x and map_coach[POS_Y] == coordinate_y:
                    char_to_Draw = "*"
                    object_in_cell = map_coach

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_Draw = "@"

                if object_in_cell:
                    clear_console()

                    random_trainer = random.randint(0, 4)
                    while trainers_and_pokemons[random_trainer][3] == 0:
                        random_trainer = random.randint(0, 4)

                    print("\n Comienza una pelea contra {} junto a {}!\n".format
                          (trainers_and_pokemons[random_trainer][0], trainers_and_pokemons[random_trainer][1]))
                    # Combat
                    while pikachu_life > 0 and trainers_and_pokemons[random_trainer][3] > 0:
                        enemy_attack = int(random.randint(0, 1))
                        # Enemy turn
                        if enemy_attack == 0:
                            print("\n{} ataca con {}".format(trainers_and_pokemons[random_trainer][1],
                                                             trainers_and_pokemons[random_trainer][2][enemy_attack][0]))
                            pikachu_life -= trainers_and_pokemons[random_trainer][2][enemy_attack][1]
                        else:
                            print("\n{} ataca con {}".format(trainers_and_pokemons[random_trainer][1],
                                                             trainers_and_pokemons[random_trainer][2][enemy_attack][0]))
                            pikachu_life -= trainers_and_pokemons[random_trainer][2][enemy_attack][1]


                        pikachu_life_bars = int(pikachu_life * LIFE_BAR_SIZE / INITIAL_LIFE_PIKACHU)
                        print("\nPikachu:     [{}{}] ({}/{})".format("*" * pikachu_life_bars,
                                                                     " " * (LIFE_BAR_SIZE - pikachu_life_bars),
                                                                     pikachu_life, INITIAL_LIFE_PIKACHU))

                        enemy_life_bars = int(trainers_and_pokemons[random_trainer][3] * LIFE_BAR_SIZE /
                                              trainers_and_pokemons[random_trainer][4])
                        print("\n{}:    [{}{}] ({}/{})".format(trainers_and_pokemons[random_trainer][1],
                                                               "*" * enemy_life_bars, " " *
                                                               (LIFE_BAR_SIZE - enemy_life_bars),
                                                               trainers_and_pokemons[random_trainer][3],
                                                               trainers_and_pokemons[random_trainer][4]))

                        if pikachu_life <= 0:
                            pikachu_life = 0
                            print("\n ---- {} ganó ---- \n".format(trainers_and_pokemons[random_trainer][1]))
                            print("Lo lamento, mejor suerte la proxima!")
                            end_game = True

                        input("\n\nEnter para continuar....\n\n")
                        clear_console()

                        # Pikachu Turn
                        clear_console()
                        print("\n---- Turno Pikachu ----\n")

                        pikachu_attack = None
                        while pikachu_attack not in pikachu_attacks:
                            pikachu_attack = input("\n¿Qué ataque realizó? [T]hunder Shock, "
                                                   "[Q]uick Attack, [I]ron Tail, [N]ada ")

                        if pikachu_attack == "T":
                            print("\nPicachu ataca con Thunder Shock")
                            trainers_and_pokemons[random_trainer][3] -= 15
                        elif pikachu_attack == "Q":
                            print("\nPicachu ataca con Quick Attack")
                            trainers_and_pokemons[random_trainer][3] -= 12
                        elif pikachu_attack == "I":
                            print("\nPicachu ataca con Iron Tail")
                            trainers_and_pokemons[random_trainer][3] -= 9
                        elif pikachu_attack == "N":
                            print("\nPicachu se queda paralizado y no ataca")

                        pikachu_life_bars = int(pikachu_life * LIFE_BAR_SIZE / INITIAL_LIFE_PIKACHU)
                        print("\nPikachu:     [{}{}] ({}/{})".format("*" * pikachu_life_bars,
                                                                     " " * (LIFE_BAR_SIZE - pikachu_life_bars),
                                                                     pikachu_life, INITIAL_LIFE_PIKACHU))

                        enemy_life_bars = int(trainers_and_pokemons[random_trainer][3] * LIFE_BAR_SIZE /
                                              trainers_and_pokemons[random_trainer][4])
                        print("\n{}:    [{}{}] ({}/{})".format(trainers_and_pokemons[random_trainer][1],
                                                               "*" * enemy_life_bars, " " *
                                                               (LIFE_BAR_SIZE - enemy_life_bars),
                                                               trainers_and_pokemons[random_trainer][3],
                                                               trainers_and_pokemons[random_trainer][4]))

                        input("\n\nEnter para continuar...\n\n")
                        clear_console()

                    if trainers_and_pokemons[random_trainer][3] <= 0:
                        trainers_and_pokemons[random_trainer][3] = 0
                        print("\n ----Pikachu ganó la batalla---- \n")
                        map_coachs.remove(object_in_cell)
                        pikachu_life = INITIAL_LIFE_PIKACHU
                        coach_defeat += 1

                if coach_defeat == 5:
                    clear_console()
                    print("\nFelicitaciones, venciste a todos los entrenadores pokemon! GANASTE!")
                    end_game = True

            if POKEMON_MAP[coordinate_y][coordinate_x] == "#":
                char_to_Draw = "#"
            print(" {} ".format(char_to_Draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("\nPress 'Q' to Exit")

    # Ask user where he wants to move
    direction = readchar.readchar()
    new_position = None

    if direction == "W":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == "S":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "A":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "D":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "Q":
        leaving_message = input("Desea finalizar el juego? [S]")
        if leaving_message == "S":
            end_game = True

    if new_position:
        if POKEMON_MAP[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position
    clear_console()
