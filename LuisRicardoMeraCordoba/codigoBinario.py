# Conversor de Binario <-> Decimal

print("=== CONVERSOR DE NUMEROS ===")
print("1. Binario a Decimal")
print("2. Decimal a Binario")

opcion = input("Elige una opcion (1 o 2): ")

if opcion == "1":
    binario = input("Escribe un numero binario: ")

    # Comprobar que solo tenga 0 y 1
    if all(digito in "01" for digito in binario):
        decimal = int(binario, 2)
        print(f"Binario: {binario}")
        print(f"Decimal: {decimal}")
    else:
        print("Error: debes escribir solamente 0 y 1.")

elif opcion == "2":
    decimal = input("Escribe un numero decimal: ")

    if decimal.isdigit():
        decimal = int(decimal)
        binario = bin(decimal)[2:]

        print(f"Decimal: {decimal}")
        print(f"Binario: {binario}")
    else:
        print("Error: debes escribir un numero decimal valido.")

else:
    print("Opcion no valida.")