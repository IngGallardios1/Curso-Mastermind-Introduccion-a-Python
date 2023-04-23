# Juan Carlos Gallardo Brambila
import random


def string_mas_larga(string, *args):
    cadenas = [string]
    if args:
        for a in args:
            cadenas.append(a)
    return max(cadenas, key=len)


def suma(lista_sumas):
    resultado = 0
    for a in lista_sumas:
        resultado += a
    return resultado


def es_impar(n):
    return not n % 2 == 0


def estas_seguro(s):
    return s == "S"


def mayusculas(s):
    respuesta = ""
    for a in s:
        if a.islower():
            respuesta += chr(ord(a) - 32)
        else:
            respuesta += a
    return respuesta


def juego_adivina_un_numero(n):
    respuesta = random.randint(1, 100)
    while n != respuesta:
        if n > respuesta:
            print("El numero es menor que {}".format(n))
            n = int(input("Adivina el numero: \n"))
        else:
            print("El numero es mayor que {}".format(n))
            n = int(input("Adivina el numero: \n"))
    return "Haz adivinado, respuesta: {}".format(respuesta)


def lista_de_la_compra(lista):
    lista = [lista]
    opc = None
    while opc != "Q":
        opc = input("\nQue desea Comprar? ([Q] para salir)\n")
        if opc != "Q":
            confirmacion = input("Seguro que desea añadir {} a la lista? S/N\n".format(opc))
            if confirmacion == "S":
                if opc in lista:
                    print("{} ya esta en la lista".format(opc))
                else:
                    print("{} se ha añadido a la lista!".format(opc))
                    lista.append(opc)
            elif confirmacion == "N":
                print()
            else:
                print("Opcion Incorrecta, favor de poner [S/N] para confirmar su compra")
    return lista


def main():
    # print(string_mas_larga("hola", "Como", "Estas"))
    # print(suma([1, 2, 3, 4, 5]))
    # print(es_impar(21))
    # s = input("Estas seguro???? -> S/N")
    # print(estas_seguro(s))
    # print(mayusculas("Hola"))
    # n = int(input("Adivina el numero: \n"))
    # print(juego_adivina_un_numero(n))
    print(lista_de_la_compra("Lista de compra:"))


if __name__ == "__main__":
    main()
