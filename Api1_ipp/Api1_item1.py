""""
API 1 
PROGRAMACION BASICA
EDUARDO VIGUERA

ITEM 1
Confecciona un programa que solicite al usuario ingresar la temperatura en grados Celsius y la convierta 
a grados Fahrenheit. Luego, se debe imprimir el resultado en pantalla.

"""
# °F = (9/5) °C + 32

C = int(input("Ingrese la Cantidad de Grads Celsius a Convertir: "))
F = 9/5 * C + 32

print(C, "Grados Celsius equivalen a ", F, "Grados Fahrenheit. ")
