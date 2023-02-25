#Juan Carlos Gallardo Brambila
#Lista de compras
lista = []
titutlo = "\n     Programa Lista de la Compra     \n"
print("-"*len(titutlo),titutlo,"-"*len(titutlo))
print("\n\n")
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

print("La lista de compra es:\n",lista)