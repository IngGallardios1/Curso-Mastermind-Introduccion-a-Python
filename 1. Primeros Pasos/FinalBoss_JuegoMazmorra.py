import random

# Final Boss - Juego de mazmorra
# Juan Carlos Gallardo Brambila

titulo = "\n    Juego de Mazmorra   \n"
muerte_sin_sentido = "\n    Has conseguido una muerte dolorosa y sin sentido    \n"
numero_aleatorio = random.randint(1, 10)
resultado = 13*numero_aleatorio

print("-"*len(titulo)+titulo+"-"*len(titulo)+"\n")
print("Te has adentrado en un calabozo del cual nadie sobrevive, intenta obtener la muerte mas"
      " gloriosa que puedas para poder entrar al Valhala\n"
      "Escoge tu propio camino de decisiones que te llevaran a tu destino. Suerte!!!")
opc = input("\nTu camino dentro del calabozo empieza, desdeas continuar???\nS/N\n")
if opc == "S" or opc =="s":
    opc = input("\nAvanzando....\n"
          "\nTe has encontrado con un orco al que le falta un brazo!!!\nPeleas fuertemente con el "
          "y lo logras vencer, felicidades.\n"
          "Detras de el hay una bifurcacion de dos caminos, por cual deseas irte???\n"
          "A. Un tunel por el que se escucha un arroyo\n"
          "B. Un camino mas amplio que se ve iluminado por piedras preciosas\n")
    if opc == "A" or opc =="a":
        opc = int(input("\nAvanzando....\n"
                        "\nMientras avanzas te encuentras con un genio, el cual te da la opcion de irte por "
                        "tres puertas si logras contestar una pregunta de matematicas\n"
                        "Cuanto es 13 x {} ???".format(numero_aleatorio)))
        if opc == 13:
            print("\nMientras mas la agarras mas me crece jajajajajjajaja perdiste\n"+
                  "-"*len(muerte_sin_sentido)+muerte_sin_sentido+"-"*len(muerte_sin_sentido)+"\n")
        elif opc == resultado:
            opc = int(input("\nFelicidades, es correcto\n"
                            "El genio te da la opcion de entrar a una de tres puertas identicas,"
                            "cual escoges? 1, 2 o 3"))
            if opc == 1:
                print("\nLamentablemente esta puerta llevaba al exterior, por lo que has sobrevivido..."
                      "\nFelicidades has perdido\n")
            elif opc == 2:
                opc = input("\nEsta puerta te lleva con una version tuya de cuando eras pequeño, tienes dos opciones,"
                      "lo matas para sobrevivir tu o lo dejas vivir y el que muere eres tu\n"
                      "Que decides, lo matas o lo dejas vivir? S/N\n")
                if opc == "S" or opc =="s":
                    print("\nFelicidades, al matar a la version mas joven que tu, igualmente has muerto\n"+
                          "-" * len(muerte_sin_sentido) + muerte_sin_sentido + "-" * len(muerte_sin_sentido) + "\n")
                elif opc == "N" or opc =="n":
                    print("\nAl no matar a tu yo del pasado has muerto\n"+
                          "-" * len(muerte_sin_sentido) + muerte_sin_sentido + "-" * len(muerte_sin_sentido) + "\n")
                else:
                    print("\nEsa opcion no se encuentra en el menu, Felicidades!!!\n" +
                          "-" * len(muerte_sin_sentido) + muerte_sin_sentido + "-" * len(muerte_sin_sentido) + "\n")
            elif opc == 3:
                print("Esta puerta te lleva con una ciclope que esta mamadisimaaaaa")
                print("\n   Felicidades!!!\n"
                      "Has conseguido el santo grial\n\n" +
                      "-" * len("   MUERTE POR SNU SNU   ") +
                      "\n   MUERTE POR SNU SNU   \n" +
                      "-" * len("   MUERTE POR SNU SNU   "))
                print("\nBienvenido al Valhala\n")
            else:
                print("\nEsa opcion no se encuentra en el menu, Felicidades!!!\n" +
                      "-" * len(muerte_sin_sentido) + muerte_sin_sentido + "-" * len(muerte_sin_sentido) + "\n")
        else:
            print("\nIncorrectoooooo\n"
                  "El genio se enoja y peleas con el, pero obviamente pierdes\n"+
                  "-"*len(muerte_sin_sentido)+muerte_sin_sentido+"-"*len(muerte_sin_sentido)+"\n")
    elif opc == "B" or opc =="b":
        opc = input("\nAvanzando...\n"
                    "\nMientras vas caminando te encuentras con una ciclope que esta mamadisimaaaaa!!!\n"
                    "Por el momento se te ocurren dos opciones...\n"
                    "A. Fingir que estas muerto y esperar que te ignore\n"
                    "B. Intentar esquivarla y continuar con tu camino\n")
        if opc == "A" or opc =="a":
            print("\n\n   Felicidades!!!\n"
                  "Has conseguido el santo grial\n\n"+
                  "-"*len("   MUERTE POR SNU SNU   ")+
                  "\n   MUERTE POR SNU SNU   \n" +
                  "-"*len("   MUERTE POR SNU SNU   "))
            print("\nBienvenido al Valhala\n")
        elif opc == "B" or opc =="b":
            print("\nAl intentar esquivarla la ciclope te alcanza ya que esta mamadisimaaaa\n"
                  "Intentas pelear con ella pero no logras nada\n"+
                  "-"*len(muerte_sin_sentido)+muerte_sin_sentido+"-"*len(muerte_sin_sentido)+"\n")
        else:
            print("\nEsa opcion no se encuentra en el menu, Felicidades!!!\n" +
                  "-" * len(muerte_sin_sentido) + muerte_sin_sentido + "-" * len(muerte_sin_sentido) + "\n")
    else:
        print("\nEsa opcion no se encuentra en el menu, Felicidades!!!\n" +
              "-" * len(muerte_sin_sentido) + muerte_sin_sentido + "-" * len(muerte_sin_sentido) + "\n")
elif opc == "N" or opc =="n":
    print("\nFelicidades, No has conseguido nada. Vuelve pronto!!!\n")
else:
    print("\nEsa opcion no se encuentra en el menu, Felicidades!!!\n"+
          "-"*len(muerte_sin_sentido)+muerte_sin_sentido+"-"*len(muerte_sin_sentido)+"\n")