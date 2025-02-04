#Programa que determina si un elemento de una lista es una cadena palíndromo
def palindromo(cad):
    return cad == cad [::-1]
def buscar_palindromo(lista):
    for elemento in lista:
        if isinstance(elemento, str) and palindromo(elemento):
            print(f"Palíndromo: {elemento}")
            return
    print("No existe")
entrada = input("Ingrese las palabras separadas por espacios: ")
la_lista = entrada.split()
buscar_palindromo(la_lista)