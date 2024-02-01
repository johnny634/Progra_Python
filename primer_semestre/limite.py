#definiendo la funcion UTILIZAMOS LISTAS
def fibonacci(n):
    serie_fibonacci = [0, 1]
    for _ in range(2, n):
        serie_fibonacci.append(serie_fibonacci[-1] + serie_fibonacci[-2])
    return serie_fibonacci
#genram,os la serie de los primeros 10 numeros FIBONACCI
n = 10
# LLAMADA A LA FUNCION
result = fibonacci(n)
# SALIDA EN PANTALLA
print(f"Primeros 10nuemros de la serie Fibonacci: {result}")