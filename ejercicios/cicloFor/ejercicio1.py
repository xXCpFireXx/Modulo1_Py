lista_numeros: list[int] = [58, 46, 35, 64, 65, 65, 88, 66, 21, 14, 48, 32, 87, 98, 78, 96, 108, 205, 3684, 544, 512, 24, 365, 3365, 854514, 23,45,66,90,87,76,54,234,34,56,78,91,26]

valor = 0
cont = 0

print("Números Pares")
for i in range(0,len(lista_numeros)):

    valor = lista_numeros[i]

    if valor % 2 == 0:        
        cont += 1
        if cont <= 20:
            print(f"Contador: {cont}")
            print(lista_numeros[i])
        

""" Pide al usuario un número n y cálcula la suma de los primeros n
números naturales usando for y luego con while """

""" numero = int(input("Ingrese el número"))

suma=0
i=1
for i in range(1, numero+1):
    suma +=i

print(suma)

sumaWhile=0
contador = 0
while contador<=numero:    
    sumaWhile +=contador
    contador+=1
     
print(sumaWhile) """