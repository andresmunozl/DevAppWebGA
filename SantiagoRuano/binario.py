def decimal_a_binario(numero):
	"""Convierte un número decimal entero a una cadena binaria."""
	if not isinstance(numero, int):
		raise TypeError("El número debe ser un entero")
	return bin(numero)[2:] if numero >= 0 else "-" + bin(-numero)[2:]


def binario_a_decimal(numero):
	"""Convierte una cadena binaria a un número decimal entero."""
	numero = str(numero).strip()
	if not numero or any(digito not in "01" for digito in numero.lstrip("-")):
		raise ValueError("El número binario solo puede contener 0 y 1")
	return int(numero, 2)


if __name__ == "__main__":
	print("Conversor decimal/binario")
	opcion = input("1. Decimal a binario\n2. Binario a decimal\nElige una opción: ").strip()

	try:
		if opcion == "1":
			decimal = int(input("Introduce un número decimal entero: "))
			print(f"Resultado: {decimal_a_binario(decimal)}")
		elif opcion == "2":
			binario = input("Introduce un número binario: ")
			print(f"Resultado: {binario_a_decimal(binario)}")
		else:
			print("Opción no válida")
	except (TypeError, ValueError) as error:
		print(f"Error: {error}")
