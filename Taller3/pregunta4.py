def multiplos_4():
    n = 1
    contador = 1
    lista_multiplos_4 = [1]
    while contador < 12:
        valor = 4*n
        n += 1
        contador += 1
        lista_multiplos_4.append(valor)
        multiplos_de_4 = ", ".join(map(str, lista_multiplos_4))
    return multiplos_de_4
        
def cuadrados():
    n = 1
    lista_potencias = []
    while n < 10:
        valor = n**2
        n += 1
        lista_potencias.append(valor)
        potencias = ", ".join(map(str, lista_potencias))
    return potencias 
    
def multiplos_2():
    n = 1
    lista_multiplos_2 = []
    contador = 1
    while contador < 7:
        valor = 2*n
        n += 1
        contador += 1
        lista_multiplos_2.append(valor)
        multiplos_de_2 = ", ".join(map(str, lista_multiplos_2))
    return multiplos_de_2
#No los imprimo todos al tiempo para que no sea confuso, al rebisar debe cambiar el nombre de la funcion
#Aunque seria bueno hacer un menu que te deje mostrar lo que quieras pero no pidio eso y me da guea XD

print(cuadrados())