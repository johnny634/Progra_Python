# Definir los artículos y sus precios
articulos = {
    1: {"nombre": "Jamón", "precio": 3},
    2: {"nombre": "Arroz", "precio": 5},
    3: {"nombre": "Aceite", "precio": 1},
    4: {"nombre": "Queso", "precio": 6},
    5: {"nombre": "Achote", "precio": 0.5}
}

# Inicializar variables
subtotal = 0

# Mostrar el menú de opciones
print("Artículos:")
for codigo, articulo in articulos.items():
    print(f"{codigo}. {articulo['nombre']} ${articulo['precio']}")

# Procesar la selección del cliente
while True:
    opcion = int(input("Seleccione el artículo (1-6) o 6 para terminar: "))
    
    if opcion == 6:
        break
    
    if opcion in articulos:
        cantidad = int(input("Ingrese la cantidad a comprar: "))
        articulo = articulos[opcion]
        subtotal += articulo["precio"] * cantidad
        print(f"{articulo['nombre']} {cantidad} ${articulo['precio']} ${articulo['precio'] * cantidad}")
    else:
        print("Opción inválida. Por favor, seleccione nuevamente.")