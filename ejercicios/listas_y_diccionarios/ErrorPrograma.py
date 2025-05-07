"""Enunciado:
El siguiente código debería contar cuántas veces aparece cada palabra en una lista, pero no funciona correctamente. 
¿Puedes encontrar el error y arreglarlo? python"""

palabras = ["manzana", "banana", "manzana", "pera", "banana", "manzana"]
contador = {}

for palabra in palabras:
    if palabra not in contador:
        contador[palabra] = 1
    else:
        contador[palabra] += 1

print(contador)