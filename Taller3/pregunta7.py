#He reutilizado el codigo de la pregunta 2 proque los numeros primos tienen dos divisores, ellos mismos y 1
#Asi que al tener que buscar divisores ps simplemente reutilize y modifique el codigo
def primos(x):
    contador = 1
    while contador <= x:
        if x % contador == 0:
            lista_primos.append(contador)
        contador += 1
    if len(lista_primos) == 2:
        print("El numero es primo")
    else:
        print("El numero no es primo")

lista_primos = []
num = int(input("Ingrese un número entero: "))
primos(num)
