# Juan Carlos Gallardo Brambila
# BataLLa Pokemon
import os
VIDA_PIKACHU = 90
VIDA_SQUIRTLE = 80
vida_pikachu = VIDA_PIKACHU
vida_squirtle = VIDA_SQUIRTLE

titulo = "\n   Batalla Pokemon   \n"
print("-"*len(titulo)+titulo+"-"*len(titulo))
print("\nPikachu vs Squirtle\n")

while vida_pikachu and vida_squirtle >=0:

    ataque = input("\nTurno de Squirtle:\n"
                   "A. Placaje\n"
                   "B. Pistola de agua\n"
                   "C. Burbuja\n")
    if ataque == "A" or ataque == "a":
        print("\nSquirtle ataca con Placaje\n"
              "Vida de Pikachu {} - 10 puntos\n".format(vida_pikachu))
        vida_pikachu -= 10
    elif ataque == "B":
        print("\nSquirtle ataca con Pistola de Agua\n"
              "Vida de Pikachu {} - 12 puntos\n".format(vida_pikachu))
        vida_pikachu -= 12
    elif ataque == "C":
        print("\nSquirtle ataca con Burbuja\n"
              "Vida de Pikachu {} - 9 puntos\n".format(vida_pikachu))
        vida_pikachu -= 9
    else:
        print("\nAtaque incorrecto, pierdes turno...\n")

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
        if ataque == "A":
            print("\nPikachu ataca con Bola voltio\n"
                  "Vida de Squirtle {} - 10 puntos\n".format(vida_squirtle))
            vida_squirtle -= 10
        elif ataque == "B":
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
    print("!\nPikachu Gana!!!\n")
else:
    print("\nSquirtle Gana!!\n")
input("")