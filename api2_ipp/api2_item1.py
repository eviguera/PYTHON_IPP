# Api n°2 item 1
# Programacion basica
# Eduardo Viguera
# Debes crear un programa que dibuje una matriz, según las siguientes consideraciones:
#1. Solicitar la cantidad de filas.
#2. Solicitar la cantidad de columnas.
#3. Dibujar las filas y columnas solicitadas.

def dibujar_matriz():
    # Solicitar la cantidad de filas y columnas al usuario
    filas = int(input("Ingresa la cantidad de filas: "))
    columnas = int(input("Ingresa la cantidad de columnas: "))

    # Para Dibujar la matriz usaremos  el blucle for, X es la variable de control que repetiremos n veces en las filas y usaremos Y para las columnas 
    for X in range(filas):
        for Y in range(columnas):
            print("+---", end="")
        print("+")  # Finaliza la línea de la fila
        for Y in range(columnas):    
            print("|   ", end="")
        print("|")  # Finaliza la línea de la fila con las celdas
    # Dibujar la última línea horizontal de la matriz
    for Y in range(columnas):
        print("+---", end="")
    print("+") # Finaliza la línea de la columnas

# Llamar a la función para dibujar la matriz

dibujar_matriz()
