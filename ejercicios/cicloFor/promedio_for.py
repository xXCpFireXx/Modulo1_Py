i:int= 0
suma:float = 0.0
valor:float = 0.0

for i in range (0,10,1):
    
    valor = int(input(f"ingresa el número {i+1}: "))
    suma = suma+valor
    

promedio = suma/10

print(f"El promedio es: {promedio} y la suma es: {suma}")
