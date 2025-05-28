# MENSAJE DE BIENVENIDA
print("Bienvenido a nuestro sistema de compras online.\n")

# VAMOS A PEDIR EL NOMBRE DEL PRODUCTO
nombre_producto = input("Indícanos el nombre del producto: ")
while nombre_producto == "":
    print("Pon un nombre válido, no puede estar vacío.")
    nombre_producto = input("Indícanos el nombre del producto: ")

# PEDIMOS EL PRECIO DEL PRODUCTO
precio_u_t = input("Registra el precio del producto: ")
while not precio_u_t.replace('.', '', 1).isdigit():
    print("Escribe un precio válido, esta sección no puede estar vacía.")
    precio_u_t = input("Indícanos el precio del producto: ")

precio_u = float(precio_u_t)

# CONFIRMAMOS EL PRECIO DEL PRODUCTO
while precio_u <= 0 or precio_u > 100000000:
    if precio_u <= 0:
        print("Este precio debe ser mayor que 0.")
    else:
        print("El precio no debe ser mayor a 100000000.")
    precio_u_t = input("Indícanos de nuevo el precio del producto: ")
    while not precio_u_t.replace('.', '', 1).isdigit():
        print("Escribe un precio válido, esta sección no puede estar vacía.")
        precio_u_t = input("Indícanos el precio del producto: ")
    precio_u = float(precio_u_t)

# PEDIMOS LA CANTIDAD DE PRODUCTOS QUE DESEA COMPRAR
cantidad_t = input("Ingresa la cantidad de productos que deseas comprar: ")
while not cantidad_t.isdigit():
    print("La cantidad de productos no es válida, ingresa una cantidad válida.")
    cantidad_t = input("Ingresa la cantidad de productos que deseas comprar: ")

cantidad = int(cantidad_t)

# CONFIRMAMOS QUE LA CANTIDAD QUE DESEA COMPRAR SEA MAYOR QUE 0
while cantidad <= 0:
    print("La cantidad de productos no es válida, ingresa una cantidad válida.")
    cantidad_t = input("Ingresa la cantidad de productos que deseas comprar: ")
    while not cantidad_t.isdigit():
        print("La cantidad de productos no es válida, ingresa una cantidad válida.")
        cantidad_t = input("Ingresa la cantidad de productos que deseas comprar: ")
    cantidad = int(cantidad_t)

# PEDIMOS EL DESCUENTO QUE TIENE ESTE PRODUCTO
descuento_t = input("Ingresa el descuento que tiene este producto: ")
while not descuento_t.replace('.', '', 1).isdigit():
    print("El descuento no es válido, ingresa un descuento válido.")
    descuento_t = input("Ingresa el descuento que tiene este producto: ")

descuento = float(descuento_t)

# CONFIRMAMOS QUE ESTE DESCUENTO SEA CORRECTO
while descuento < 0 or descuento > 100:
    print("El descuento no es válido, ingresa un descuento entre 0% y 100%.")
    descuento_t = input("Ingresa el descuento que tiene este producto: ")
    while not descuento_t.replace('.', '', 1).isdigit():
        print("El descuento no es válido, ingresa un descuento válido.")
        descuento_t = input("Ingresa el descuento que tiene este producto: ")
    descuento = float(descuento_t)

# HACEMOS LOS CÁLCULOS DE LA COMPRA
costo_s_d = precio_u * cantidad 
monto_d = (descuento / 100) * costo_s_d
costo_d = costo_s_d - monto_d

# MOSTRAMOS EL RESULTADO DE ESTA COMPRA
print("\nEsta es tu compra:")
print("\nResumen de la compra:")
print("Producto:", nombre_producto)
print("Precio unitario: $", "{:,.0f}".format(precio_u))
print("Cantidad:", cantidad)
print("Descuento aplicado:", descuento, "%")
print("Costo sin descuento: $", "{:,.0f}".format(costo_s_d))
print("Monto de descuento: $", "{:,.0f}".format(monto_d))
print("Costo total a pagar: $", "{:,.0f}".format(costo_d))
print("\nGracias por tu compra.")
print("Esperamos verte pronto.")