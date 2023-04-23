# Juan Carlos Gallardo Brambila
SALIDA = "SALIR"
NOMBRE_DEL_ARCHIVO = "El_mas_Capito.txt"


def crear_archivo_texto(lista_de_compra):
    with open(NOMBRE_DEL_ARCHIVO, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_de_compra))


def pregunta_al_usuario():
    return input("Introduzca un producto: [{} para salir] \n".format(SALIDA))


def guardar_item(lista_de_compra, input_usuario):
    if input_usuario.lower() in [a.lower() for a in lista_de_compra]:
        print("El item ya existe!!!")
    else:
        lista_de_compra.append(input_usuario)


def cargar_archivo():
    lista_de_compra = []
    if input("Quieres cargar el archivo anterior? [S/N]\n") == "S":
        try:
            with open(NOMBRE_DEL_ARCHIVO, "r") as a:
                lista_de_compra = a.read().split("\n")
        except FileNotFoundError:
            print("El archivo no ha sido encontrado")
    return lista_de_compra


def mostrar_lista(lista_de_compra):
    print("\n".join(lista_de_compra))

def main():
    lista_de_compra = cargar_archivo()
    mostrar_lista(lista_de_compra)
    input_usuario = pregunta_al_usuario()

    while input_usuario != SALIDA:
        guardar_item(lista_de_compra, input_usuario)
        mostrar_lista(lista_de_compra)
        input_usuario = pregunta_al_usuario()

    crear_archivo_texto(lista_de_compra)


if __name__ == "__main__":
    main()
