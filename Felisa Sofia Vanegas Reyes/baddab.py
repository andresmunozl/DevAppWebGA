def decimal_a_binario(numero_decimal):
    # bin() devuelve una cadena que empieza con '0b', usando [2:] lo eliminamos
    return bin(numero_decimal)[2:]

def binario_a_decimal(numero_binario):
    # int() con el segundo argumento '2' convierte la cadena binaria a entero
    return int(str(numero_binario), 2)

# --- Ejemplo de uso e interfaz en consola ---
def menu():
    print("--- CONVERTIDOR BINARIO / DECIMAL ---")
    print("1. Convertir Decimal a Binario")
    print("2. Convertir Binario a Decimal")
    
    opcion = input("Elige una opción (1 o 2): ")
    
    if opcion == "1":
        num = int(input("Ingresa un número decimal: "))
        resultado = decimal_a_binario(num)
        print(f"El número {num} en binario es: {resultado}")
        
    elif opcion == "2":
        num_bin = input("Ingresa un número binario (solo 0s y 1s): ")
        try:
            resultado = binario_a_decimal(num_bin)
            print(f"El binario {num_bin} en decimal es: {resultado}")
        except ValueError:
            print("Error: Ingresaste un número binario no válido.")
            
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    menu()