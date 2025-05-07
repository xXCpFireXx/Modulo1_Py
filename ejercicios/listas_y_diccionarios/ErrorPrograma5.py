"""El siguiente código intenta sumar los precios de un diccionario, pero no funciona. 
Encuentra el error y corrígelo para que calcule correctamente el total.
python"""

precios = {"manzana": 1.5, "banana": 0.8, "pera": 1.2}
total = 0
for precio in precios.values():
    total += precio
print(total)