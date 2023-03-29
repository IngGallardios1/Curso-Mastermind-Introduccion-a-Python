#Juan Carlos Gallardo Brambila

numeros_introducidos = input("Introuzca los numeros separados por una coma: [,]\n")
numeros_de_usuario = [int(numero) for numero in numeros_introducidos.split(",")]

print("\nEl numero menor es: {}\nEl nmero mayor es: {}".format(min(numeros_de_usuario),max(numeros_de_usuario)))