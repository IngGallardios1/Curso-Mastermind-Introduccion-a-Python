titulo = "Este programa calcula el maximo entre dos numeros"
print("\n" + titulo + "\n" + "-"*len(titulo) + "\n")
num1 = int(input("Digite el primer numero:\n"))
num2 = int(input("Digite el segundo numero:\n"))
num3 = int(input("Digite el tercer numero:\n"))
print("Los numeros son {}, {}, {}".format(num1,num2,num3))
print("El numero mayor es: {}".format(max(num1,num2,num3)))
print("El numero menor es: {}".format(min(num1,num2,num3)))


