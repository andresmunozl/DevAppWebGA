print(" CONVERSOR DECIMAL - BINARIO ")
print("1. Convertir de Decimal a Binario")
print("2. Convertir de Binario a Decimal")

opcion = input("Elige una opción (1 o 2): ")

if opcion == "1":
    # Lógica de Decimal a Binario
    numero_decimal = int(input("Ingresa el número decimal: "))
    # La función bin() convierte a binario, [2:] quita el '0b' del principio
    numero_binario = bin(numero_decimal)[2:] 
    print(f"El resultado en binario es: {numero_binario}")

elif opcion == "2":
    # Lógica de Binario a Decimal
    numero_binario = input("Ingresa el número binario: ")
    # int(numero, 2) le dice a Python que convierta un texto base 2 (binario) a decimal
    numero_decimal = int(numero_binario, 2)
    print(f"El resultado en decimal es: {numero_decimal}")

else:
    print("Opción no válida. Por favor reinicia el programa.")