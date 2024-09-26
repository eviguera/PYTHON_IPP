""""
API 1 
PROGRAMACION BASICA
EDUARDO VIGUERA

ITEM 3
Elabora un programa que, ingresando todas las notas, entregue la nota de presentación.
"""

Lab1 = float(input("Ingrese la primera nota de laboratorios: "))
Lab2 = float(input("Ingrese la segunda nota de laboratorios: "))
Lab3 = float(input("Ingrese la tercera nota de laboratorios: "))

clase1 = float(input("Ingrese la primera nota de clase: "))
clase2 = float(input("Ingrese la segunda nota de clase: "))
clase3 = float(input("Ingrese la tercera nota de clase: "))

solemne1 = float(input("Ingrese la primera solemne clase: "))
solemne2 = float(input("Ingrese la segunda solemne clase: "))

promedio_lab = (Lab1 + Lab2 + Lab3)/3
Porcetanje_final_laboratorios = promedio_lab * 0.15

promedio_clases = (clase1 + clase2 + clase3)/3
Porcetanje_final_clases = promedio_clases * 0.15

Porcetanje_final_solemne1 = solemne1 * 0.35
Porcetanje_final_solemne2 = solemne2 * 0.35

nota_final = Porcetanje_final_laboratorios + Porcetanje_final_clases + Porcetanje_final_solemne1 + Porcetanje_final_solemne2

print("La nota Final de Presentacion es: ",nota_final)


