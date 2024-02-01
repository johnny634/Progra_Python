#El dueño de una despensa de abarrotes requiere que se diseñe un

# Definir precios de los artículos
precios = {'Jamón': 3, 'Arroz': 5, 'Aceite': 1, 'Queso': 6, 'Achote': 0.5}

# Inicializar variables
total_compra = 0
carrito = {}

# Mostrar menú
print("Artículos disponibles: \n ")
for articulo, precio in precios.items():
    print(f"{articulo}: ${precio}")

# Iniciar bucle
while True:
    # Pedir al usuario que seleccione un artículo
    seleccion = input("Seleccione un artículo o escriba 'Terminar' para finalizar: ")

    # Salir del bucle si el usuario elige 'Terminar'
    if seleccion.lower() == 'terminar':
        break

    # Verificar si el artículo seleccionado existe
    if seleccion in precios:
        # Pedir al usuario que ingrese la cantidad
        cantidad = int(input(f"\n Ingrese la cantidad de {seleccion} a comprar:  "))

        # Calcular subtotal por artículo y actualizar total
        subtotal = precios[seleccion] * cantidad
        total_compra += subtotal

        # Agregar al carrito

        carrito[seleccion] = {'Precio unitario': precios[seleccion], 'Cantidad': cantidad, 'Subtotal': subtotal}

        print(f" \n Se ha añadido al carrito: {seleccion} x {cantidad}")
    else:
        print(" \n Artículo no válido. Por favor, seleccione un artículo de la lista.")

# Mostrar detalles de la compra
print("\n Detalles de la compra:")
for articulo, detalles in carrito.items():
    print(f"{articulo}: Precio unitario ${detalles['Precio unitario']} - Cantidad: {detalles['Cantidad']} - Subtotal: ${detalles['Subtotal']}")

# Mostrar el total de la compra
print(f"\nTotal de la compra: ${total_compra}")
