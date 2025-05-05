"""
Puntos en el plano cartesiano
    Escribir un programa que pida ingresar coordenadas (x, y) y determine cuántos puntos se encuentran en cada cuadrante (I, II, III, IV).
    Nota: Al inicio, el programa debe solicitar la cantidad de puntos a procesar.
"""
#Se inicializan los contadores en 0
cuadranteI, cuadranteII, cuadranteIII, cuadranteIV = 0, 0, 0, 0

cantidadPuntos = int(input("\n¿Cuántas COORDENADAS quieres que CALCULE el programa?\n"))

for i in range(cantidadPuntos):
    
    print(f"\nCOORDENADA {i+1}")
    puntoX = float(input(f"Ingresa el PUNTO X de la COORDENADA {i+1}: "))
    puntoY = float(input(f"Ingresa el PUNTO Y de la COORDENADA {i+1}: "))

    print(f"Ingresó la COORDENADA ({puntoX},{puntoY})\n")

    if puntoX!=0 and puntoY!=0:

        if puntoX>0 and puntoY>0:
            cuadranteI+=1
            print("La COORDENADA esta en CUADRANTE I")

        elif puntoX>0 and puntoY<0:
            cuadranteIV+=1
            print("La COORDENADA esta en CUADRANTE IV")

        elif puntoX<0 and puntoY>0:
            cuadranteII+=1
            print("La COORDENADA esta en CUADRANTE II")
        
        elif puntoX<0 and puntoY<0:
            cuadranteIII+=1
            print("La COORDENADA esta en CUADRANTE III")
        
    else:
        print("LA COORDENADA esta en el CENTRO del PLANO CARTESIANO")

print(f"\nLa CANTIDAD de COORDENADAS en el CUADRANTE I es: {cuadranteI}")
print(f"\nLa CANTIDAD de COORDENADAS en el CUADRANTE II es: {cuadranteII}")
print(f"\nLa CANTIDAD de COORDENADAS en el CUADRANTE III es: {cuadranteIII}")
print(f"\nLa CANTIDAD de COORDENADAS en el CUADRANTE IV es: {cuadranteIV}")