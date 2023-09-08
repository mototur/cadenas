#Escribir un programa que pregunte el nombre del usuario en la consola y muestre en 
#pantalla <NOMBRE> tiene <n> letras.

nombre_usuario = input ("Ingresa tu nombre \n")
print(nombre_usuario.upper() + " tiene " + str (len (nombre_usuario )) + " letras ")