#Programa que determina si una lista es palíndromo:
def es_palindromo_lista(lista):
    return lista == lista[::-1]
# Ejemplo de uso
mi_lista = [1, 2, 3, 2, 1]
print("La lista es palíndromo." if es_palindromo_lista(mi_lista) else "La lista no es palíndromo.")
