# Api n°2 item 2
# Programacion basica
# Eduardo Viguera
#crea un programa en Python que solicite al usuario:
#1. Ingresar un número entero del 1 al 9.
#2. Que ingrese números secuenciales partiendo por 1, pero saltándose aquellos que sean múltiplos del valor ingresado al comienzo.
#3. En caso de ingresar un valor erróneo, enviar un mensaje indicando el error y el número que correspondía ingresar


def es_multiplo(num, divisor):
    return num % divisor == 0

def juego_secuencial():
    # Solicitar al usuario que ingrese un número entero del 1 al 9
    while True:
        try:
            numero = int(input("Ingresa un número entero del 1 al 9: "))
            if 1 <= numero <= 9:
                break
            else:
                print("El número debe estar entre 1 y 9.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    # Inicializar el contador
    contador = 1

    # Iniciar el juego
    while True:
        # Calcular el valor correcto que debería ser ingresado
        if es_multiplo(contador, numero):
            contador += 1
            continue

        # Solicitar el siguiente número al usuario
        try:
            entrada = int(input(f"Ingrese el siguente  número : "))
            if entrada != contador:
                print(f"Error: El número que correspondía ingresar era {contador}. Juego terminado.")
                break
        except ValueError:
            print(f"Error: Debías ingresar el número {contador}. Juego terminado.")
            break

        # Incrementar el contador para la siguiente iteración
        contador += 1

# Llamar a la función para ejecutar el juego
juego_secuencial()
