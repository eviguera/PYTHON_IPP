""""
API 1 
PROGRAMACION BASICA
EDUARDO VIGUERA

ITEM 4
Con lo aprendido hasta el momento, realiza un programa que de manera totalmente matemática (ocupando solo lo visto hasta el momento), muestre el digito verificador de un programa. El Rut ingresado debe ser un input que sea de largo 8 (sobre 10 millones) y una vez ingresado este número el programa deberá retornar un número del 1 al 11 (siendo simbólicamente el 10 la letra K y el 11 el número 0, pero esto no es importante que se muestren así).
"""

Rut = input("Ingresa el RUT sin dígito verificador (sin punto ni guion): ")
rut_invertido = Rut[::-1]
suma = 0
multiplicador = 2

for digito in rut_invertido:
    suma += int(digito) * multiplicador  
    multiplicador  += 1  
    if multiplicador > 7:
        multiplicador = 2

modulo = 11 - (suma % 11) 
if modulo == 11:
    digito_verificador = "0"   
elif modulo == 10:
    digito_verificador = "k"
else:
    digito_verificador = str(modulo)

print("El dígito verificador es:", digito_verificador)

