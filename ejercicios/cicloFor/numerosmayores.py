"""
Números mayores o iguales a 1000
Escribir un programa que lea n números enteros y determine cuántos de ellos son mayores o iguales a 1000.
"""

contador = 0

cantidadNumeros = int(input("¿Cuántos números quieres que LEA el programa?\n"))

for i in range(0, cantidadNumeros, 1):

    numeroIngresado = int(input(f"Ingresa el número {i+1}: "))

    if numeroIngresado>=1000:
        contador+=1


print(f"La CANTIDAD de NÚMEROS mayores o iguales a 1000 es: {contador}")