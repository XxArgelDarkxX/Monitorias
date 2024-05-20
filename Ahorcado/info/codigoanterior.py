import random
import os
import time

lista_palabras = []
with open('palabras.txt', 'r') as palabras:
    for i in palabras:
        j = i.strip()
        lista_palabras.append(j)


IMAGENES_AHORCADO = ['''
+---+
|   |
    |
    |
    |
    |

=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

+---+
|   |
O   |
/|   |
    |
    |
=========''', '''

+---+
|   |
O   |
/|\  |
    |
    |
=========''', '''

+---+
|   |
O   |
/|\  |
/    |
    |
=========''', '''

+---+
|   |
O   |
/|\  |
/ \  |
    |
=========''']

palabra_aleatoria = random.choice(lista_palabras)
palabra_oculta = '_' * len(palabra_aleatoria)
letras_adivinadas = []
letras_incorrectas = []


while '_' in palabra_oculta and len(letras_incorrectas) < len(IMAGENES_AHORCADO):
    os.system('cls')
    print(IMAGENES_AHORCADO[len(letras_incorrectas)])
    print(palabra_oculta)
    letra = input("Introduzca una letra: ").lower()  
    if letra in letras_adivinadas or letra in letras_incorrectas:
        print("La letra que introduciste ya la pusiste. Intenta con otra.")
        time.sleep(2)
        continue
    elif letra in palabra_aleatoria.lower():  
        for i in range(len(palabra_aleatoria)):
            if letra == palabra_aleatoria[i].lower():
                palabra_oculta[i] = palabra_aleatoria[i]
        letras_adivinadas.append(letra)
    else:
        letras_incorrectas.append(letra)


os.system('cls')
if '_' not in palabra_oculta:
    print(IMAGENES_AHORCADO[len(letras_incorrectas)])
    print(palabra_oculta)
    print(f"Felicidades, adivinaste la palabra con {len(letras_incorrectas)} fallos, la palabra correcta era: {palabra_aleatoria}")
else:
    print(IMAGENES_AHORCADO[-1])
    print(palabra_oculta)
    print(f"Oh, haz perdido, la palabra a adivinar era: {palabra_aleatoria}")
