titulo = "Este programa te ayuda a escoger tu celular, por favor responda las preguntas"
print("\n" + titulo + "\n" + "-"*len(titulo) + "\n")
mensaje_error = "Ups, esa opcion no se encuentra en el menu"
opc = input("Que SO prefieres?\n"
            "A. Android\n"
            "B. IOS\n")
if opc == "A":
    opc = input("Tienes dinero? S/N")
    if opc == "S":
        opc = input("Te importa la camara del movil? S/N")
        if opc == "S":
            print("Tu mejor opcion es comprar el Google pixar superCam")
        elif opc == "N":
            print("Tu mejor opcion es comprar un Android calidad-precio")
        else:
            print("\n" + mensaje_error + "\n" + "-"*len(mensaje_error) + "\n")
    elif opc == "N":
        print("Tu mejor opcion es comprar un android chino de $100")
    else:
        print("\n" + mensaje_error + "\n" + "-"*len(mensaje_error) + "\n")
elif opc == "B":
    opc = input("Tienes dinero? S/N")
    if opc == "S":
        print("Tu mejor opcion es comprar un Iphone Ultra pro max")
    elif opc == "N":
        print("Tu mejor opcion es comprar un Iphone de segunda mano")
    else:
        print("\n" + mensaje_error + "\n" + "-"*len(mensaje_error) + "\n")
else:
    print("\n" + mensaje_error + "\n" + "-"*len(mensaje_error) + "\n")