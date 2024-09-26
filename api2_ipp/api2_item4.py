#Api2 item 4
#Programacion basica
#eduardo viguera
#Crea un programa que:
#1. Permita al usuario elegir dos palabras que cumplan con las condiciones mencionadas anteriormente.
#2. Solicite al usuario que ingrese una frase.
#3. Reemplace las letras según la regla establecida a partir de las palabras elegidas.
#4. Imprima la nueva frase con las letras reemplazadas

def validar_palabras(palabra1, palabra2):
    # Verifica que las palabras tengan el mismo largo y que las letras iguales no coincidan en la misma posición
    if len(palabra1) != len(palabra2):
        return False
    
    for i in range(len(palabra1)):
        if palabra1[i] == palabra2[i]:
            return False
    
    return True

def crear_diccionario_reemplazo(palabra1, palabra2):
    # Crea un diccionario para mapear letras de palabra1 a palabra2 y viceversa
    diccionario = {}
    for i in range(len(palabra1)):
        diccionario[palabra1[i]] = palabra2[i]
        diccionario[palabra2[i]] = palabra1[i]  # También mapea en sentido contrario
    return diccionario

def reemplazar_frase(frase, diccionario):
    # Reemplaza las letras de la frase según el diccionario de reemplazo
    frase_reemplazada = ''
    for letra in frase:
        if letra in diccionario:
            frase_reemplazada += diccionario[letra]
        else:
            frase_reemplazada += letra
    return frase_reemplazada

def main():
    while True:
        palabra1 = input("Ingrese la primera palabra: ").strip()
        palabra2 = input("Ingrese la segunda palabra: ").strip()
        
        if validar_palabras(palabra1, palabra2):
            break
        else:
            print("Las palabras no son válidas. Deben tener el mismo largo y las letras iguales no deben coincidir en la misma posición.")
    
    diccionario = crear_diccionario_reemplazo(palabra1, palabra2)
    
    frase = input("Ingrese una frase: ")
    frase_reemplazada = reemplazar_frase(frase, diccionario)
    
    print("Frase con las letras reemplazadas:")
    print(frase_reemplazada)

if __name__ == "__main__":
    main()
