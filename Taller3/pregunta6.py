def promedio(n):
    promedio = sum(n)/len(n)
    return promedio

lista_numeros = []

while len(lista_numeros) < 10:
    n = int(input("Introduzca un numero entero: "))
    lista_numeros.append(n)
    print(f"Numeros registrados: {len(lista_numeros)}/10")

print(f"El promedio de los numeros {lista_numeros} es: {promedio(lista_numeros)}")
