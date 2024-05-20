import math  
import time

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    return x / y
    
def potenciacion(x, y):
    return x ** y

def raiz(x):
    return math.sqrt(x)

def sen(x):
    return math.sin(x)  

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def loga(x, y):
    return math.log(x, y)

def loga10(x):
    return math.log10(x)

def factorial(x):
    return math.factorial(x)

def euler_exponente_x(x):
    return math.exp(x)

#Menu de opciones

while True:
    print("""Menu de opciones
          1. Suma                       8. Coseno
          2. Resta                      9. Tangente
          3. Multiplicacion             10. Logaritmo
          4. Division                   11. Logaritmo en base 10
          5. Potencia                   12. Factorial
          6. Raiz                       13. e^x
          7. Seno                       14. Salir""")
              
    opcion = int(input("Seleccione la operacion a hacer: "))

    if opcion == 1:
        num1 = float(input("Ingrese el primer numero real: "))
        num2 = float(input("Ingrese el segundo numero real: "))        
        print(suma(num1, num2))
        time.sleep(3)

    if opcion == 2:
        num1 = float(input("Ingrese el primer numero real: "))
        num2 = float(input("Ingrese el segundo numero real: "))        
        print(resta(num1, num2))
        time.sleep(3)

    if opcion == 3:
        num1 = float(input("Ingrese el primer numero real: "))
        num2 = float(input("Ingrese el segundo numero real: "))        
        print(multiplicacion(num1, num2))
        time.sleep(3)

    if opcion == 4:
        num1 = float(input("Ingrese el primer numero real: "))
        num2 = float(input("Ingrese el segundo numero real: "))        
        print(division(num1, num2))
        time.sleep(3)

    if opcion == 5:
        num1 = float(input("Ingrese el primer numero real: "))
        num2 = float(input("Ingrese el segundo numero real: "))        
        print(potenciacion(num1, num2))
        time.sleep(3)

    if opcion == 6:
        num1 = float(input("Ingrese un numero real: "))       
        print(raiz(num1))
        time.sleep(3)

    if opcion == 7:
        num1 = float(input("Ingrese un numero real: "))       
        print(sen(num1))
        time.sleep(3)

    if opcion == 8:
        num1 = float(input("Ingrese un numero real: "))       
        print(cos(num1))
        time.sleep(3)

    if opcion == 9:
        num1 = float(input("Ingrese un numero real: "))       
        print(tan(num1))      
        time.sleep(3)

    if opcion == 10:
        num1 = float(input("Ingrese el primer numero real: "))
        num2 = float(input("Ingrese el segundo numero real: "))
        print(loga(num1, num2))
        time.sleep(3)

    if opcion == 11:
        num1 = float(input("Ingrese un numero real: "))
        print(loga10(num1))
        time.sleep(3)

    if opcion == 12:
        num1 = int(input("Ingrese un numero entero: "))
        print(factorial(num1))
        time.sleep(3)

    if opcion == 13:
        num1 = float(input("Ingrese un numero real: "))
        print(euler_exponente_x(num1))
        time.sleep(3)

    if opcion == 14:
        print("Gracias por usar, Adios")
        break
