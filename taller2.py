# #1
# def promedio(nota1, nota2, nota3, nota4):
#     global promedios
#     for i in range(estudiantes):
#         promedios = []
#         notadefinitiva = (nota1 + nota2 + nota3 + nota4)/4
#         promedios.append(notadefinitiva)
#     return promedios
    
# def main():
#     for i in range(len(promedios)):
#         if promedios[i] >= 4.5:
#             print(f"La nota definitiva del estudiante {i+1} califica para la beca")
#         else:
#             print(f"La nota definitiva del estudiante {i+1} no califica para la beca")


# if __name__ == '__main__':
#     estudiantes = 4
#     while estudiantes > 0:
#         nota1 = float(input("Ingrese su nota 1: "))
#         nota2 = float(input("Ingrese su nota 2: "))
#         nota3 = float(input("Ingrese su nota 3: "))
#         nota4 = float(input("Ingrese su nota 4: "))
#         print("\n")
#         promedio(nota1, nota2, nota3, nota4)
#         main()
#         estudiantes -= 1

#2

# def año_bisiesto(año):


#serie fibonacci

# indice = 12
# fibonacci = [0, 1]

# while len(fibonacci) < indice:
#     fibonacci.append(fibonacci[-1] + fibonacci[-2])
#     print(fibonacci)

#Definir si un numero es par o impar
#Preguntarle al usuario si quiere hacer una operacion con los numeros
#Preguntarle si quiere introducir otro numero

def suma(numeros):
    resultado = sum(numeros)

def resta(numeros):
    pass

def multiplicar(numeros):
    pass

def dividir(numeros):
    pass

def potenciar(numeros):
    pass

def raiz(numeros):
    pass

def menu():
    print("Quieres hacer alguna operacion? y/n")
    option1 = input("")

    if option1.lower() == "y":
        while True:
            print("""Menu de Opciones
                1. Suma
                2. Resta
                3. Multiplicacion
                4. Division
                5. Potenciacion
                6. Radicacion
                7. Dejar de usar la calculadora
              
                """)
            
            option2 = int(input("Introduzca una accion del menu"))
            if option2 == 1:
                print(suma())
            elif option2 == 2:
                print(resta())
            elif option2 == 3:
                print(multiplicar())
            elif option2 == 4:
                print(dividir())
            elif option2 == 5:
                print(potenciar())
            elif option2 == 6:
                print(raiz())
            elif option2 == 7:
                break
    else:
        pass
               

count = 0
lista_numeros = []
while True:
    numero = int(input("Introduzca un numero entero: "))

    if numero % 2 == 0:
        print("El numero introducido es par")
        lista_numeros.append(numero)
        count += 1
    else:
        print("El numero introducido es impar")
        lista_numeros.append(numero)
        count += 1
    
    if count >= 2 and count <= 5:
        menu()
    else:
        print("Rango maximo de numeros ingresados.")
        menu()
        break