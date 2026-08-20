nombre = input("Ingrese su nombre: ")
precio = float(input("Ingrese el precio del producto: "))
producto = int(input("Ingrese la cantidad de productos: "))
vip = int(input("Ingrese si es cliente VIP (1 para sí, 0 para no): "))

total = precio * producto

if producto >= 5 and vip == 1:
    descuento = 25

elif producto >= 5 or vip == 1:
    descuento = 15

else:
    descuento = 0

dinero_descuento = total * (descuento / 100)
total_pagar = total - dinero_descuento

print("----- RECIVO DE COMPRA -----")
print("Cliente:", nombre)
print("Total sin descuento:", total)
print("Descuento:", descuento, "%")
print("Dinero descontado:", dinero_descuento)
print("Total a pagar:", total_pagar)
