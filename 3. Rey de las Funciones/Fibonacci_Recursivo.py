# Juan Carlos Gallardo Brambila
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    num = int(input("Digite el numero de la secuencia de Fibonacci:\n"))
    for f in range(num):
        print(fibonacci(f), end=", ")
