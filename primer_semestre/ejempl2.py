#INICIALIZACION DE VARIABLES
Nombre_Empleado = str()
Tipo_Empleado = int()
Telefono = int()
Cedula = int()
Sueldo_Base = float()
Iess = float()
Bonificacion = float()
Sueldo_Neto = float()
Liquido_Recibir = float()
#==============================================
#INGRESOS DE DATOS POR EL USUARIO Y VALIDACION
Nombre_Empledado = str(input("Escriba nombre del empleado ==========> "))
Telefono = int(input("Escriba Numero de Telefono del Empleado ======> "))
Cedula = int(input("Escriba Numero de Cedula del Empledado =========> "))
Sueldo_Base = float(input("Escriba el sueldo Base del Empleado =====> "))
print("TIPO DE EMPLEADO ")
print("< 1 > OFICINA ")
print("< 2 > PRODUCCION ")
Tipo_Empleado = int(input("SELECCIONE TIPO DE EMPLEADO ======> "))
# ==============================================
#CALCULOS
if Tipo_Empleado == 1:
    print("EMPLEADO SIN BONIFICACION")
else:   
    Bonificacion = (Sueldo_Base * 0.05)

# FIN DE IF
Sueldo_Neto = Sueldo_Base + Bonificacion
Iess = (Sueldo_Neto * 0.0945)
Liquido_Recibir = Sueldo_Neto - Iess
# ==============================================
#IMPRESIONES POR PANTALLA
print("<==================================================")
print("============== GUTIERREZ RIVERA SAS ================")
print("=================== ROL DE PAGO ====================")
print("NOMBRE DEL EMPLEADO ======>", Nombre_Empledado)
print("TELEFONO DEL EMPLEADO =====>", Telefono)
print("CEDULA DEL EMPLEADO =====>", Cedula)
print("<======== INGRESOS =====>")
print("SUELDO DEL EMPLEADO =====>", Sueldo_Base)
print("BONIFICACION DEL EMPLEADO =====>", Bonificacion)
print("<======== EGRESOS =====>")
print("APORTE AL IESS =====>", Iess)
print("<==================================================")
print("LIQUIDO A RECIBIR =====>", Liquido_Recibir)
print("<==================================================")