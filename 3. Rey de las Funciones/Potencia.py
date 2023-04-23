# Juan Carlos Gallardo Brambila

def potencia(num, *args):
    total = num * num
    p = args[0]
    if args:
        total = num ** p
    return total


def main():
    print("==============================================")
    print("Este programa calcula la potencia de un numero")
    print("==============================================\n\n")
    number = int(input("Digite un numero: \n"))
    try:
        power = int(input("Digite la potencia : \n"))
    except ValueError:
        power = 2
    print("El resultado es: {}".format(potencia(number, power)))


if __name__ == "__main__":
    main()
