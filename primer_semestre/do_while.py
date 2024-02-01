#Bucle do-while: Crea un programa en Python que simule un juego de adivinanza. 
# En este juego, el usuario debe adivinar un número secreto (por ejemplo, 7) 
# y el programa le dará pistas si su adivinanza es demasiado alta o demasiado baja.
#  Utiliza un bucle do-while para asegurarte de que el usuario juegue 
# al menos una vez y pueda seguir jugando si lo desea.
import random

# Genera un número secreto aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

while True:
    # Pide al usuario que adivine el número
    intento = int(input("Adivina el número secreto (entre 1 y 10): "))

    # Comprueba si el intento es correcto
    if intento == numero_secreto:
        print("¡Felicidades! ¡Has adivinado el número secreto!")
        break
    elif intento < numero_secreto:
        print("El número es demasiado bajo. Intenta nuevamente.")
    else:
        print("El número es demasiado alto. Intenta nuevamente.")

    # Pregunta al usuario si quiere jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()

    # Si la respuesta no es 's', termina el bucle
    if jugar_de_nuevo != 's':
        break

# Fin del programa
print("Gracias por jugar.")
