lista = [30, 1, 10, 20]

def prueba_index(lista, indice):
    for rango in range(len(lista)):
        if indice == rango:
            print(lista[indice])

def prueba_count(lista):
    pass

def prueba_sort(lista, reverse=False):
    for i in range(len(lista)):
        for j in range(i, -1):
            if lista[i] > lista[j+1]:
                lista[i], lista[j+1] = lista[j+1], lista[i]
    print(lista)

def prueba_max(lista):
    maximo = 0
    try:
        for i in lista:
            if i > maximo:
                maximo = i
        print(maximo)
    except TypeError:
        print("Uno o varios elementos de la lista no son numeros")

def prueba_prom(lista):
    promedio = 0
    try:
        for i in lista:
            promedio += i
        print(promedio/len(lista))
    except TypeError:
        print("Uno o varios elementos de la lista no son numeros")


def prueba_min(lista):
    minimo = 0
    try:
        for i in lista:
            if minimo == 0:
                minimo = i
            elif i < minimo:
                minimo = i
        print(minimo)
    except TypeError:
        print("Uno o varios elementos de la lista no son numeros")


prueba_sort(lista)