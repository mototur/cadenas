#Escribir un programa que pregunte al usuario la fecha de nacimiento en formato
#dd/mm/aaaa y lo muestre en pantalla 

dia_nacimiento = int (input ("Ingrese el dia de su nacimiento \n"))
mes_nacimiento = int (input ("Ingrese el mes de su nacimiento \n"))
anio_nacimiento = int (input ("Ingrese el anio de su nacimiento \n"))

if dia_nacimiento == 0 or dia_nacimiento > 31 or mes_nacimiento == 0 or mes_nacimiento > 12:
    print("Tu fecha no es valida")
else:
    print(f"Naciste el: {dia_nacimiento} / {mes_nacimiento}/ {anio_nacimiento}")
