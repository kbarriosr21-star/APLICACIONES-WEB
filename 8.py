dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

dia = dia + 1

if dia > 30:
    dia = 1
    mes = mes + 1

    if mes > 12:
        mes = 1
        anio = anio + 1

print("La fecha del día siguiente es:", dia, "/", mes, "/", anio)
