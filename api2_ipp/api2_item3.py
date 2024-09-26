#Api2 item 3
#Programacion basica
#eduardo viguera
# Cree un programa en Python que permita:
#1. Pedir al usuario el año de nacimiento de una persona.
#2. Pedir al usuario el año de muerte de la persona.
#3. Si la persona sigue viva, el año de muerte será 0. En este caso, el programa debe reemplazar el 0 por el año actual.
#4. Calcular la cantidad de años bisiestos que la persona ha vivido.
#5. Mostrar la cantidad de años bisiestos calculados en el paso anterior.


from datetime import datetime #crear libreria sobre dias, meses y años pra poder usar calendarios

def es_bisiesto(año):
    #Determina si un año es bisiesto.
    if (año % 4 == 0): #Un año bisiesto es un año que es divisible por 4  pero no por 400.
        if (año % 100 == 0): #excepto los años que son divisibles por 100
            if (año % 400 == 0): #pero no por 400.
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def contar_bisiestos(inicio, fin):
    #Cuenta los años bisiestos entre dos años .
    bisiestos = 0
    for año in range(inicio, fin + 1):
        if es_bisiesto(año):
            bisiestos += 1
    return bisiestos

def main():
    # Pedir al usuario el año de nacimiento y de muerte
    año_nacimiento = int(input("Introduce el año de nacimiento: "))
    año_muerte = int(input("Introduce el año de muerte (0 si la persona sigue viva): "))
    
    # Si la persona está viva, usar el año actual
    if año_muerte == 0:
        año_muerte = datetime.now().year
    
    # Asegurarse de que el año de muerte sea posterior al año de nacimiento
    if año_muerte < año_nacimiento:
        print("El año de muerte debe ser mayor o igual al año de nacimiento.")
        return
    
    # Contar y mostrar los años bisiestos
    bisiestos = contar_bisiestos(año_nacimiento, año_muerte)
    print(f"La persona ha vivido {bisiestos} años bisiestos.")

if __name__ == "__main__":
    main()
