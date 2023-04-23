#Juan Carlos Gallardo Brambila
import readchar
import os
import random

#Constants
POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 3
VIDA_PIKACHU = 90
VIDA_SQUIRTLE = 80

#Variables in game
vida_pikachu = VIDA_PIKACHU
vida_squirtle = VIDA_SQUIRTLE
my_position = [14,9]
tail_length = 0
map_objects = []
end_game = False
#Map Design
obstacle_definition = """\
########   ########     #####
#                           #
#       ##          ##      #
        ##          ##       
        ##          ##       
        ##          ##       
        ##          ##       
#                           #
#                           #
#                           #
#                           #
#                           #
         ##          ##      
         ##          ##      
         ##          ##      
         ##          ##      
#                           #
#                           #
########   ########     #####\ """                                      

#Generate obstacles on the map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = 29
MAP_HEIGHT = 19

while True:
    #Generate random objects on the map
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0,(MAP_WIDTH-1)), random.randint(0,(MAP_HEIGHT-1))]

        if new_position not in map_objects and new_position != my_position: 
            if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
                map_objects.append(new_position)

    print("Score: {}".format(tail_length))
    #Draw Map
    print("-"+"--" * MAP_WIDTH+"-")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            object_in_cell = None
            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " +"
                if object_in_cell:
                    os.system("cls")
                    vida_pikachu = VIDA_PIKACHU
                    vida_squirtle = VIDA_SQUIRTLE
                    titulo = "\n   Batalla Pokemon   \n"
                    print("-"*len(titulo)+titulo+"-"*len(titulo))
                    print("\nPikachu vs Squirtle\n")

                    while vida_pikachu and vida_squirtle > 0:

                        print("\nTurno de Squirtle:\n"
                                    "A. Placaje\n"
                                    "B. Pistola de agua\n"
                                    "C. Burbuja\n")
                        ataque = random.randint(1,3)
                        if ataque == 1:
                            print("\nSquirtle ataca con Placaje\n"
                                "Vida de Pikachu {} - 10 puntos\n".format(vida_pikachu))
                            vida_pikachu -= 5
                        elif ataque == 2:
                            print("\nSquirtle ataca con Pistola de Agua\n"
                                "Vida de Pikachu {} - 12 puntos\n".format(vida_pikachu))
                            vida_pikachu -= 15
                        elif ataque == 3:
                            print("\nSquirtle ataca con Burbuja\n"
                                "Vida de Pikachu {} - 9 puntos\n".format(vida_pikachu))
                            vida_pikachu -= 10

                        if vida_pikachu < 0:
                            vida_pikachu = 0
                        if vida_squirtle < 0:
                            vida_squirtle = 0
                        print("Vida Pikachu:")
                        print("[" + "#" * (int(vida_pikachu / 10)), " " * (10 - int(vida_pikachu / 10)),
                            "] ({}/{})".format(vida_pikachu,VIDA_PIKACHU))
                        print("Vida Squirtle:")
                        print("[" + "#" * (int(vida_squirtle / 10)), " " * (10 - int(vida_squirtle / 10)),
                            "] ({}/{})".format(vida_squirtle,VIDA_SQUIRTLE))


                        input("\n\nPresiona Enter para continuar...")
                        os.system("cls")

                        if vida_pikachu >0:
                            ataque = input("\nTurno de Pikachu:\n"
                                        "A. Bola voltio\n"
                                        "B. Onda trueno\n")
                            if ataque == "A" or ataque == "a":
                                print("\nPikachu ataca con Bola voltio\n"
                                    "Vida de Squirtle {} - 10 puntos\n".format(vida_squirtle))
                                vida_squirtle -= 10
                            elif ataque == "B" or ataque == "b":
                                print("\nPikachu ataca con Onda trueno\n"
                                    "Vida de Squirtle {} - 10 puntos\n".format(vida_squirtle))
                                vida_squirtle -= 11
                            else:
                                print("\nAtaque incorrecto, pierdes turno...\n")

                            if vida_pikachu < 0:
                                vida_pikachu = 0
                            if vida_squirtle < 0:
                                vida_squirtle = 0

                            print("Vida Pikachu:")
                            print("[" + "#" * (int(vida_pikachu / 10)), " " * (10 - int(vida_pikachu / 10)),
                                "] ({}/{})".format(vida_pikachu, VIDA_PIKACHU))
                            print("Vida Squirtle:")
                            print("[" + "#" * (int(vida_squirtle / 10)), " " * (10 - int(vida_squirtle / 10)),
                                "] ({}/{})".format(vida_squirtle, VIDA_SQUIRTLE))

                            input("\n\nPresiona Enter para continuar...")
                            os.system("cls")
                    if vida_pikachu > 0:
                        map_objects.remove(object_in_cell)
                        tail_length +=1
                    else:
                        end_game = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")
        
    if end_game:
        break

    print("-"+"--" * MAP_WIDTH+"-")
    
    #Input of where to move, readchar == input()
    direction = readchar.readchar()

    new_position = None
    #Movement conditions
    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y]-1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[POS_X]-1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y]+1) % MAP_HEIGHT]

    elif direction == "d":
        new_position = [(my_position[POS_X]+1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        break

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    os.system("cls")
os.system("cls")
print("\n\n       YOU LOOSE    ")
print("\n\n=========================")
print("     Final Score: {}     ".format(tail_length))
print("=========================\n\n")
