PRECIOS = [3, 5, 1, 6, 0.5]

def mostrar_menu():
    print("Bienvenido a la despensa de abarrotes")
    print("Seleccione el artículo que desea comprar:")
    for i in range(len(PRECIOS)):
        print(f"{i + 1}. Artículo {i + 1}: ${PRECIOS[i]}")
    print(f"{len(PRECIOS) + 1}. Terminar")

def seleccionar_articulo():
    while True:
        try:
            opcion = int(input("Ingrese el número del artículo: "))
            if 1 <= opcion <= len(PRECIOS) + 1:
                return opcion
            else:
                print("Opción inválida, intente de nuevo")
        except ValueError:
            print("Por favor, ingrese un número válido")

def ingresar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad a comprar: "))
            if cantidad >= 1:
                return cantidad
            else:
                print("Cantidad inválida, intente de nuevo")
        except ValueError:
            print("Por favor, ingrese un número válido")

def calcular_subtotal(opcion, cantidad):
    return PRECIOS[opcion - 1] * cantidad

def main():
    total = 0
    while True:
        mostrar_menu()
        opcion = seleccionar_articulo()
        if opcion == len(PRECIOS) + 1:
            break
        cantidad = ingresar_cantidad()
        subtotal = calcular_subtotal(opcion, cantidad)
        print(f"Subtotal: ${subtotal}")
        total += subtotal
    print(f"Total de la compra: ${total}")
    print("Gracias por su compra. ¡Hasta luego!")

if __name__ == "__main__":
    main()
