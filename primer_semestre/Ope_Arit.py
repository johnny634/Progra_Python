# Entrada de datos
# Uso de al menos dos operadores aritméticos para realizar cálculos matemáticos.

# a. Uso de al menos dos operadores aritméticos
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("\na. Operadores Aritméticos:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}\n")


# Implementación de al menos dos operadores lógicos para evaluar condiciones y tomar decisiones.

# b. Implementación de al menos dos operadores lógicos
condicion1 = bool(input("Ingresa una condición (V / F ): ").capitalize())
condicion2 = bool(input("Ingresa otra condición (V / F): ").capitalize())

and_resultado = condicion1 and condicion2
or_resultado = condicion1 or condicion2
not_resultado = not condicion1

print("\n b. Operadores Lógicos:")
print(f"AND: {and_resultado}")
print(f"OR: {or_resultado}")
print(f"NOT: {not_resultado}\n")

# Utilización de al menos dos operadores relacionales para comparar valores y obtener resultados basados en esas comparaciones.


# c. Utilización de al menos dos operadores relacionales
valor1 = float(input("Ingresa un valor: "))
valor2 = float(input("Ingresa otro valor: "))

igual = valor1 == valor2
diferente = valor1 != valor2
mayor_que = valor1 > valor2
menor_que = valor1 < valor2

print("\n c. Operadores Relacionales:")
print(f"Igual a: {igual}")
print(f"Diferente de: {diferente}")
print(f"Mayor que: {mayor_que}")
print(f"Menor que: {menor_que}")
