#Escribir un programa que pregunte al correo electronico del usuario en la consola
#y muestre por pantalla otro correo electronico con el mismo nombre.

correo_electronico = input ("Ingrese un correo electronico: \n")
print (correo_electronico[:correo_electronico.find( '@' )] + '@ceu.es')