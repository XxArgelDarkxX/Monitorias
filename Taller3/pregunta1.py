def multiplo(x):
    contador = 1
    #Se pone asi porque un numero puede tener multiplos infinitos
    while len(lista_multiplos) < 10:
        multiplicar = x * contador
        lista_multiplos.append(multiplicar)
        contador += 1

lista_multiplos = []
numero = int(input("Introduzca un numero entero cualquiera: "))
multiplo(numero)
#Lo que hace aqui es tan solo decorativo, use lo mismo en varios archivos para poder imprimirlos como str y separarlos por comas 
#Ya que las listas al imprimirse aparecen con corchetes a mi no me parece estetico
multiplos = ", ".join(map(str, lista_multiplos))
print(f"Los multiplos de {numero} son: {multiplos}")        


