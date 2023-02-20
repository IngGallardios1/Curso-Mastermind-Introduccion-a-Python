print("Este programa convierte grados Farenheit y Celcius")
opc = int(input("1.C - F\n"
                "2.F - C\n"))
if opc == 1:
    c = float(input("Digite los grados Celcius: "))
    grados = (c*(5/9))+32
    print("{} F".format(grados))
elif opc == 2:
    f = float(input("Digite los grados Farenheit: "))
    grados = (f-32)*(5/9)
    print("{} C".format(grados))
else:
    print("Opcion invalida")
