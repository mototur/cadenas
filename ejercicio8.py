#Escribir un programa que pregunte en la consola el precio de un producto en euros
#con dos decimales y muestre por pantalla el numero de centimos del precio.

precio_producto = input ("Ingrese el precio del producto con dos decimales: \n ")
print (precio_producto[:precio_producto.find('.')], 'euros y', precio_producto[precio_producto.find('.')+1:], 'centimos.' )
