import random

# Este codigo es un juego para adivinar un numero

numero_aleatorio = random.randint(1, 100)
print("Este es un juego en el que tienes que adivinar un numero aleatorio entre el 1 y el 100, "
      "trata de adivinar con la menor cantidad de intentos")
bandera = False
num_intentos = 1
while not bandera:
    numero = int(input("{}. Intento, digite un numero --> ".format(num_intentos)))
    num_intentos += 1
    if numero > numero_aleatorio:
        print("menor\n".title())
    elif numero < numero_aleatorio:
        print("Mayor\n")
    else:
        bandera = True
print("Felicidades, haz adinivando el numero {}".format(numero_aleatorio))
print("Numero de intentos: {}".format(num_intentos))

