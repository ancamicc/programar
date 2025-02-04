#Programa que determina si en una lista no existen elementos repetidos:
def elementos_unicos(lista):
    return len(lista) == len(set(lista))

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5, 2]
print("No existen elementos repetidos." if elementos_unicos(mi_lista) else "Existen elementos repetidos.")