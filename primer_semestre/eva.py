#Ejercicio 1
#Declamos las varialbes

# Solicitar al usuario que ingrese el primer número
val1 = int(input("Ingrese el primer numero entero: "))
# Solicitar al usuario que ingrese el segundo número
val2 = int(input("Ingrese el segundo numero entero: "))

# Calcular la suma de los dos números ingresados
resultado = val1 + val2

# Mostrar el resultado
print(" \n La suma de", val1, "y", val2, " es = ",  resultado, "\n")

#Ejercico 2
#Declara variables de tipo decimal.

float1= float(input("Ingrese el primer numero decimal :  "))
# Solicitar al usuario que ingrese el segundo número
float2= float(input("Ingrese el segundo numero decimal: "))

# Calcular la suma de los dos números ingresados
resul = float1 + float2

# Mostrar el resultado
print ("\n La suma de", float1, "y", float2,  "es =", resul, "\n")

#Ejercico 3
#Declaramos las varibles de tipo caractares.

# Solicitar al usuario que ingrese su nombre
x = str(input("Ingresa tu nombre: "))
# Solicitar al usuario que ingrese su apellido
y = str (input("Ingresa tu apellido: "))

# Mostrar el resultado
print("\n Mi nombre y apellidos es: " , x  , " ", y, "\n")  


#Ejercico 4
# Pregunta Ejercicio Booleano
pregunta =" Sabes sumar (v / f ):  \n"

# Respuesta correcta
respuesta_correcta = True

# Muestra la pregunta y recibe la respuesta del usuario
respuesta_usuario = input(pregunta ).lower()

# Imprime el resultado directamente sin utilizar if
print("Felicitaciones!🎉 \n" if respuesta_usuario == "v" or respuesta_usuario == " f" else "Tu puedes. 🤦‍♂️")









