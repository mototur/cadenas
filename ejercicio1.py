#Escribir un programa que prefunte el nombre del usuario en la consola y un numero entero e imprima por pantalla
#en lineas distintas el nombre del usuario tantas veces como el numero introducido

nombre_usuario = input ("Cual es su nombre \n")
n = input("Introduce un numero entero: ")
print ((nombre_usuario + "\n") * int (n))