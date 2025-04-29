"""
Cálculo de áreas de triángulos
    Confeccionar un programa que lea n pares de datos (base y altura) correspondientes a triángulos. Debe mostrar:
    Base, altura y superficie de cada triángulo.
    Cantidad de triángulos con superficie mayor a 12.
"""

contador = 0

cantidadAreasT = int(input("\n¿Cuántas ÁREAS de TRIANGULOS quieres que CALCULE el programa?\n"))

for i in range(0, cantidadAreasT, 1):
    
    print(f"\nTRIÁNGULO {i+1}")
    base = float(input(f"Ingresa la BASE del TRIÁNGULO {i+1}: "))
    altura = float(input(f"Ingresa la ALTURA del TRIÁNGULO {i+1}: "))

    superficie = ((base * altura)/2)
    print(f"\nLa SUPERFICIE (ÁREA) del TRIÁNGULO {i+1} es: {superficie}\n")
    if superficie>12:
        contador+=1


print(f"\nLa CANTIDAD de ÁREAS de TRIÁNGULOS mayores a 12 es: {contador}")