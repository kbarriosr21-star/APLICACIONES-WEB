dia = int(input("ingrese el dia:"))
mes = int(input("ingrese el mes:"))
año = int(input("ingrese el año:"))

if mes == 2:
    if dia >= 1 and dia <= 28:
        print("la fecha es correcta")
    else:
        print("la fecha es incorrecta")
        
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia >= 1 and dia <= 30:
        print("la fecha es correcta")
    else:
        print("la fecha es incorrecta")
        
elif mes == 1 or mes == 3 or mes == 6 or mes == 9 or mes == 11:
    if dia >= 1 and dia <= 31:
        print("la fecha es correcta")
    else:
        print("la fecha es incorrecta")
        
else:
    print("la fecha es incorrecta")
