# Definir funciones para cada operación
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

# Función por defecto en caso de operación no válida
def default():
    return "Opción no válida"

# Función que simula la estructura switch-case
def switch_case(operacion, num1, num2):
    # Diccionario que asocia operaciones con funciones
    operaciones = {
        'sumar': sumar,
        'restar': restar,
        'multiplicar': multiplicar,
        'dividir': dividir
    }
    
    # Obtener la función asociada con la operación, o la función por defecto si no existe
    # Luego, llamar a esa función con los números proporcionados
    return operaciones.get(operacion, default)(num1, num2)

# Solicitar entrada al usuario
operacion = input("\n Ingrese la operación (sumar, restar, multiplicar, dividir): ")
numero1 = float(input("\n Ingrese el primer número: "))
numero2 = float(input("\n Ingrese el segundo número: "))

# Realizar la operación seleccionada
resultado = switch_case(operacion, numero1, numero2)

# Mostrar el resultado
print(f" \n El resultado de {operacion} {numero1} y {numero2} es: {resultado}")

