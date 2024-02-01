import math  # Agrega esta línea para incluir el módulo math necesario para las operaciones matemáticas

figura = input(" \n Seleccione una figura geométrica: (1) Pentágono, (2) Hexágono, (3) Trapecio, (4) Paralelogramo: ")

# Calcular el área y perímetro del Pentágono
if figura == "1":
    apotema = float(input("\n Ingrese el apotema del Pentágono en centímetros: "))
    lado = float(input(" \n Ingrese el lado del Pentágono en centímetros: "))
     # Aplicamos la formula para obtener apotema, perimetro y area
    perimetro = 5 * lado
    area = (5/4) * apotema * lado  
   #Imprimimos los resultados 
    print(f" \n El Pentágono de apotema {apotema}cm  ")
    print(f"\n Tiene un perímetro de {perimetro} cm ")
    print(f"\n Un área de {area} cm2")

# Calcular el área y perímetro del Hexágono
elif figura == "2":
    apotema = float(input("Ingrese el apotema del Hexágono en centímetros: "))
    lado = float(input("Ingrese el lado del Hexágono en centímetros: "))
    # Aplicamos la formula para obtener apotema, perimetro y área
    # Calculamos su perimetro
    perimetro = 6 * lado
    # Calculamos su su area
    area = (3/2) * apotema * lado  
    print(f"\n El Hexágono de apotema {apotema}cm ")
    print(f"\n Tiene un perímetro de {perimetro} cm")
    print(f"\n Un área de {area} cm2")


# Calcular el área y perímetro del Trapecio
elif figura == "3":
    base_mayor = float(input("Ingrese la base mayor del Trapecio en centímetros: "))
    base_menor = float(input("Ingrese la base menor del Trapecio en centímetros: "))
    altura = float(input("Ingrese la altura del Trapecio en centímetros: "))
    # Aplicamos la formula para obtener apotema, perimetro y área
    # Calculamos su perimetro
    perimetro = base_mayor + base_menor + 2 * math.sqrt(altura**2 + ((base_mayor - base_menor)/2)**2)
    area = (base_mayor + base_menor) * altura / 2
    print(f"\n El Trapecio de base mayor {base_mayor}cm")
    print(f"\n Base menor{base_menor} cm")
    print(f"\n Altura {altura} cm")
    print(f"\n Tiene un perímetro de {perimetro} cm")
    print(f"\n Un área de {area} cm2")

# Calcular el área y perímetro del Paralelogramo
elif figura == "4":
    base = float(input("Ingrese la base del Paralelogramo en centímetros: "))
    altura = float(input("Ingrese la altura del Paralelogramo en centímetros: "))
    # Aplicamos la formula para obtener apotema, perimetro y área
    # Calculamos su perimetro
    perimetro = 2 * (base + altura)
    area = base * altura
    print(f"\n El Paralelogramo de base {base}cm ")
    print(f"\n Altura {altura} cm ")
    print(f"\n Tiene un perímetro de {perimetro} cm ")
    print(f"\n Un área de {area} cm2")

# Si la figura seleccionada no es válida, mostrar un mensaje de error
else:
    print("Figura geométrica no válida")
