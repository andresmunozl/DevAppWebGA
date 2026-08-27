# 1. Pedir al usuario que ingrese un número entero
numero = int(input("Ingresa un número: "))

# 2. Verificar si es múltiplo de 5 Y de 9
if numero % 5 == 0 and numero % 9 == 0:
    print(f"El número {numero} ES múltiplo de 5 y de 9.")
else:
    print(f"El número {numero} NO es múltiplo de ambos números.")