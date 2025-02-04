def tiene_dos_vocales(cadena):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in cadena if letra in vocales) >= 2

def buscar_cadena_con_vocales(lista):
    for elemento in lista:
        if isinstance(elemento, str) and tiene_dos_vocales(elemento):
            print(f"Cadena encontrada con dos o más vocales: {elemento}")
            return
    print("No existe")

# Ejemplo de uso
mi_lista = ["sol", "programación", "cielo"]
buscar_cadena_con_vocales(mi_lista)