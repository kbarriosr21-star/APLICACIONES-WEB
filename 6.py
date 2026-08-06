dia = int(input("ingrese el dia:"))
mes = int(input("ingrese el mes:"))
año = int(input("ingrese el año:"))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia >= 1 and dia <= 30:
        print("la fecha es correcta")
        
else: 
    print("la fecha es incorrecta")
