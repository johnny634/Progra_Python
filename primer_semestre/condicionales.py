# Condicionales
# Solicitar datos al usuario
edad = int(input("\n Ingrese su edad:   ")) 
# Se solicita la edad del usuario
nivel_educativo = input(" \n Ingrese su nivel educativo: ") 
# Se solicita el nivel educativo del usuario

# Evaluar la situación
# Si el usuario tiene 18 años o más y es bachiller
if edad >= 18 and nivel_educativo == "Bachiller": 
    print(" \n Puede inscribirse en la universidad.")
    # Se le permite inscribirse en la universidad
elif edad >= 18 and nivel_educativo != "Bachiller": 
    # Si el usuario tiene 18 años o más pero no es bachiller
    print(" \n Puede inscribirse en la universidad, pero no cuenta con el nivel educativo adecuado.")
    # Se le permite inscribirse pero se le informa que no tiene el nivel educativo adecuado
else: # Si el usuario no cumple con los requisitos
    print("\n No cumple con los requisitos para inscribirse en la universidad.") 
    # Se le informa que no cumple con los requisitos
