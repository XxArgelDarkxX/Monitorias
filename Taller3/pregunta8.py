#Gracias por el chancuco mi querido monitor XD

def fibonacci(n):
    lista_numeros = []
    num1 = 0
    num2 = 1
    for i in range(n):
        lista_numeros.append(num1)
        num1, num2 = num2, num2 + num1
    return lista_numeros

n = int(input("Ingrese la cantidad de veces que se repite la serie: "))
while True:
    if n < 0:
        n *= -1
    else:
        print(f"Los primeros {n} terminos de la serie son: {fibonacci(n)}")
        break

