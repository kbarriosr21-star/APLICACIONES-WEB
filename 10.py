compra = int(input("Ingrese el valor de la compra: "))

if compra > 300000:
    compra = compra - (compra * 20 / 100)

print("Debe pagar:", compra)
