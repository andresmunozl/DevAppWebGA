dia = input("¿Qué día es hoy? ")

match dia:
    case "lunes":
        print("Inicio de la semana a trabajar")
    case "viernes":
        print("Por fin es viernes, casi fin de semana")
    case "sabado" | "domingo":
        print("Es fin de semana, a descansar")
    case _:
        print("Día no válido")
