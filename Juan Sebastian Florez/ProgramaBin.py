print("1. Decimal a Binario")
print("2 Binario a Decimal")


opcion = int(input("Seleccione una opcion: "))

if opcion == 1:
    decimal = int(input("Ingrese un numero decimal: "))

    bin(decimal)[2:]

    binario = bin(decimal)[2:]

    print("Binario: ", binario)


elif opcion ==2:
    binario = input("Ingrese un numero binario: ")
    decimal =int(binario, 2)
    print("Decimal:", decimal)