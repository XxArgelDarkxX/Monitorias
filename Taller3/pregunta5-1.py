def es_par_impar(x):
    lista_pares = []
    lista_impares = []
    contador_pares = 1
    contador_impares = 1
    while contador_pares < 7 and contador_impares < 7:
        if x % 2 == 0:
            lista_pares.append(x)
            x += 1
            contador_pares += 1
        else:
            lista_impares.append(x)
            x +=1
            contador_impares += 1
    return lista_pares, lista_impares

def fracciones():
    numeros_pares, numeros_impares = es_par_impar(1)
    for i in range(min(len(numeros_pares), len(numeros_impares))):
        fraccion = numeros_impares[i] / numeros_pares[i]
        print(fraccion)

#la siguiente pregunta que era la c la tenia incompleta como dije en el grupo pero esta la tengo completa


