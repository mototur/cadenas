#Escribir un programa que pida al usuario que introduzca una frase en la consola
#y una vocal 

frase = input ("Ingrese una frase: \n")
vocal = input ("Ingrese una vocal en minuscula: \n")
print (frase.replace(vocal, vocal.upper()))
