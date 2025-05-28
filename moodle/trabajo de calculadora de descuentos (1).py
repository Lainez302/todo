# Mensaje de bienvenida
print("Bienvenido a este sistema de compras online.\n")

# Pedimos el nombre del producto y nos aseguramos que no esté vacío
nombre_p = input("Ingrese el nombre del producto: ")
while nombre_p == "":
    print("Esta sección no puede estar vacía.")
    nombre_p = input("Por favor ingrese de nuevo el nombre del producto: ")

# Pedimos el precio del producto y validamos que sea un número positivo y no mayor a 999.999.999
precio_u_texto = input("Ingrese el precio unitario del producto (en pesos colombianos): ")
while not precio_u_texto.replace('.', '', 1).isdigit():
    print("Debe ingresar un número válido y positivo.")
    precio_u_texto = input("Ingrese el precio unitario del producto (en pesos colombianos): ")

precio_u = float(precio_u_texto)

# Confirmamos que el precio sea mayor que cero y no sobrepase 999.999.999
while precio_u <= 0 or precio_u > 999999999:
    if precio_u <= 0:
        print("El precio debe ser mayor que cero.")
    else:
        print("El precio no puede ser mayor a 999.999.999 pesos.")
    precio_u_texto = input("Ingrese el precio unitario del producto (en pesos colombianos): ")
    while not precio_u_texto.replace('.', '', 1).isdigit():
        print("Debe ingresar un número válido y positivo.")
        precio_u_texto = input("Ingrese el precio unitario del producto (en pesos colombianos): ")
    precio_u = float(precio_u_texto)

# Pedimos la cantidad de productos y verificamos que sea un número entero positivo
cantidad_texto = input("Ingrese la cantidad de productos: ")
while not cantidad_texto.isdigit():
    print("Debe ingresar un número entero positivo.")
    cantidad_texto = input("Ingrese la cantidad de productos: ")

cantidad = int(cantidad_texto)

# Confirmamos que la cantidad también sea mayor que cero
while cantidad <= 0:
    print("La cantidad debe ser mayor que cero.")
    cantidad_texto = input("Ingrese la cantidad de productos: ")
    while not cantidad_texto.isdigit():
        print("Debe ingresar un número entero positivo.")
        cantidad_texto = input("Ingrese la cantidad de productos: ")
    cantidad = int(cantidad_texto)

# Pedimos el porcentaje de descuento y nos aseguramos que esté entre 0 y 100
descuento_texto = input("Ingrese el porcentaje de descuento (0-100): ")
while not descuento_texto.replace('.', '', 1).isdigit():
    print("Debe ingresar un número entre 0 y 100.")
    descuento_texto = input("Ingrese el porcentaje de descuento (0-100): ")

porcentaje_descuento = float(descuento_texto)

# Verificamos que el descuento esté en el rango correcto
while porcentaje_descuento < 0 or porcentaje_descuento > 100:
    print("El descuento debe ser entre 0% y 100%.")
    descuento_texto = input("Ingrese el porcentaje de descuento (0-100): ")
    while not descuento_texto.replace('.', '', 1).isdigit():
        print("Debe ingresar un número entre 0 y 100.")
        descuento_texto = input("Ingrese el porcentaje de descuento (0-100): ")
    porcentaje_descuento = float(descuento_texto)

# Hacemos los cálculos de costos
costo_sin_descuento = precio_u * cantidad
monto_descuento = (porcentaje_descuento / 100) * costo_sin_descuento
costo_total = costo_sin_descuento - monto_descuento

# Mostramos el resumen de la compra con toda la información
print("\nHemos realizado el cálculo de su compra y esta es tu compra")
print("\nResumen de la compra:")
print("Producto:", nombre_p)
print("Precio unitario: $", "{:,.0f}".format(precio_u))
print("Cantidad:", cantidad)
print("Descuento aplicado:", porcentaje_descuento, "%")
print("Costo sin descuento: $", "{:,.0f}".format(costo_sin_descuento))
print("Monto de descuento: $", "{:,.0f}".format(monto_descuento))
print("Costo total a pagar: $", "{:,.0f}".format(costo_total))
