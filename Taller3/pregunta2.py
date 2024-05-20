def divisores(x):
    contador = 1
    while contador <= x:
        if x % contador == 0:
            lista_divisores.append(contador)
        contador += 1
    return lista_divisores

lista_divisores = []
num = int(input("Ingrese un número entero: "))
divisores(num)
divisores_encontrados = ", ".join(map(str, lista_divisores))
print(f"Los divisores de {num} son: {divisores_encontrados}")

