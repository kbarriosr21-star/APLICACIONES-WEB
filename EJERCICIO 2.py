ventas_dia = ["Electrónica", "Ropa", "Electrónica", "Hogar", "Ropa", "Electrónica", "Juguetes", "Hogar"]

categoria_unica = set(ventas_dia)
print("Categorías únicas vendidas:", categoria_unica)

conteo = {}

for categoria in ventas_dia:
    if categoria in conteo:
        conteo[categoria] = conteo[categoria] + 1
    else:
        conteo[categoria] = 1

print("Conteo de ventas por categoría:", conteo)

mas_vendida = max(conteo, key=conteo.get)
print("Categoría más vendida:", mas_vendida)
