#Escribir un programa que pregunte por un numero de telefono con este formato y 
#muestre en pantalla el numero de telefono sin el prefijo y la extension
#prefijo es el codigo del Pais +34 y la extension tiene dos digitos.

numero_de_telefono = input ("Ingrese un numero de telefono \n ")
eliminar_prefijo_extension = numero_de_telefono
print (eliminar_prefijo_extension [4:-3])
