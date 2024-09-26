#Api3 Programacion basica
# Eduardo Viguera

#item 1 
#Escribir un programa que lea entre 10 y 20 números ingresados por el usuario, los almacene en una lista y los muestre ordenados de mayor a menor. El programa debe seguir recibiendo ingreso de números hasta que el usuario ingrese 0. Sin embargo, el número 0 no debe ser mostrado en pantalla.

def main():
    numeros = []
    
    print("Ingresa entre 10 y 20 números. Para detener el ingreso, ingresa 0.")
    
    while len(numeros) < 20:  # Mientras no se haya alcanzado el máximo de 20 números
        try:
            numero = int(input("Ingresa un número (0 para terminar): "))
            
            if numero == 0:
                if len(numeros) >= 10:  # Verifica si ya se ingresaron al menos 10 números
                    break
                else:
                    print("Debes ingresar al menos 10 números antes de detenerte.")
                    continue
            
            numeros.append(numero)
        
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    # Ordenar la lista de mayor a menor
    numeros.sort(reverse=True)
    
    # Mostrar los números ingresados, excluyendo el 0
    print("Números ordenados de mayor a menor:")
    print(numeros)

# Llamar a la función principal
if __name__ == "__main__":
    main()



# item 2
#Escribir un programa que almacene palabras ingresadas por el usuario. El programa debe seguir recibiendo ingreso de palabras hasta que el usuario ingrese tres asteriscos "***". Luego de esto, las palabras deben ser mostradas por pantalla una única vez. Es decir, si el usuario ingresó palabras repetidas, solo se deben mostrar una vez

def main():
    palabras = set()  # Usamos un conjunto (set) para evitar duplicados

    print('Ingresa palabras. Para finalizar, escribe "***".')

    while True:
        palabra = input("Ingresa una palabra: ")
        
        if palabra == "***":
            break
        
        palabras.add(palabra)  # Añade la palabra al conjunto (solo se guardan valores únicos)
    
    # Mostrar las palabras únicas
    print("\nPalabras únicas ingresadas:")
    for palabra in palabras:
        print(palabra)

# Llamar a la función principal
if __name__ == "__main__":
    main()



#item 3
# ¡Juguemos Scrabble! Construye un diccionario con los siguientes valores. Luego, el usuario ingresa una palabra por pantalla y el programa devuelve el puntaje correspondiente.

valores_juego_scrabble = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"    
}

# FUNCION PARA OBTENER PUNTA DE CADA LETRA

def obtener_puntaje(letra):
    for valor, letras in valores_juego_scrabble.items():
        if letra.upper() in letras:
            return valor
    return 0

#pedir al usuario que ingrese la palabra

palabra = input("ingresa una palabra para calcular su puntaje: ")

#sumar el puntaje  correspondiente al total

puntaje_total = 0
for letra in palabra:
    puntaje_total += obtener_puntaje(letra)

#mostrar puntaje  total
print(f"el puntaje total de la palabra {palabra} es: {puntaje_total}") 

#item4
#Construir un programa que determine si dos palabras ingresadas por el usuario son anagramas.

#pedir al usuario que ingrese la palabra

palabra1 = input("ingresa la primera palabra: ")
palabra2 = input("ingresa la segunda palabra: ")

#convertir ambas palabras en lista de caracteres

lista1 = sorted(list(palabra1))
lista2 = sorted(list(palabra2))

#comparar lista ; si son iguales, las palabras son anagramas.

if lista1 == lista2: 
    print("las palabras son anagramas")
else:
    print("las palabras no son anagramas")    


#item5
#Construir un programa en donde el usuario ingrese números por pantalla y el programa devuelva la suma de todos los números ingresados por el usuario. Si el usuario ingresa un carácter no numérico, el programa debe mostrar un mensaje de error y continuar solicitando números y sumando. El programa finaliza cuando el usuario presione enter.

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
