def entero_a_binario(num):
    if num <= 0:
        return "0"
    else:
        bina = ""
        while num > 0:
            resto = num % 2
            bina = str(resto)+bina
            num //= 2
        return bina
while True:
    num = int(input("Digite un numero entero menor a 257: "))
    if num >= 257:
        print("El numero digitado es mayor o igual a 257, por favor ingrese un numero menor a 257")
    else:
        bina = entero_a_binario(num)
        print(f"El numero {num} en binario es: {bina}")
        break