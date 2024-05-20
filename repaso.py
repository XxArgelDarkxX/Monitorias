# horas = int(input("Ingrese la cantidad de horas: "))
# minutos = int(input("Ingrese la cantida de minutos: "))
# segundos = int(input("Ingrese la cantida de segundos: "))
# dias = 0

# minutos = minutos + segundos // 60
# segundos = segundos % 60
# horas = horas + minutos // 60
# minutos = minutos % 60
# dias = dias + horas // 24
# horas = horas % 24



# print(f"{dias:02d}:{horas:02d}:{minutos:02d}:{segundos:02d}")

# import math 

# tamaño_disco = float(input("Cuantas GB se procesaran: "))
# tamaño_disco2 = tamaño_disco * 1024
# valor_cd = 5000
# tamaño_cd = 700 / 1024

# cantidad_cds = math.ceil(tamaño_disco / tamaño_cd)
# precio_base_cds = cantidad_cds * valor_cd
# precio_iva = precio_base_cds * 0.19
# precio_total = precio_base_cds + precio_iva

# print(f"Para almacenar {tamaño_disco} GB o {tamaño_disco2} MB en discos de 700 MB se requieren {cantidad_cds} CD's que en total cuestan {precio_total}")

def es_par(n):
    return (n % 2 == 0)

def collatz(n):
    print(n)
    if n == 1:
        return 1
    if es_par(n):
        return collatz(n/2)
    else:
        return collatz(3*n+1)
    
def funcion(numero, contador):
    while contador < 4:
        if(collatz(numero) == 1):
            contador += 1
funcion(13, 0)


