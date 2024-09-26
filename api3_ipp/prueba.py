def sumar_numeros():
    suma_total = 0
    while True:
        entrada = input("Ingresa un número (o presiona Enter para terminar): ")

        if entrada == "":  # Verifica si el usuario presionó enter sin ingresar nada
            break

        try:
            numero = float(entrada)  # Intenta convertir la entrada a número
            suma_total += numero
        except ValueError:  # Captura el error si el usuario ingresa un carácter no numérico
            print("Error: Ingresa solo números.")

    print(f"La suma total de los números ingresados es: {suma_total}")

# Llamada a la función
sumar_numeros()
