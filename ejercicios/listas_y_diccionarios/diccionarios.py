""" Contar frecuencia de palabras​
Dada una lista de palabras, crea un diccionario que muestre cuántas veces aparece cada palabra.​
Ejemplo: ["hola", "mundo", "hola"] → {"hola": 2, "mundo": 1}.​ """

def count_word_frequencies(words=[]):

    dictionare = {}

    for word in words:
        if word not in dictionare:            
            dictionare[word] = 1
    else:
        dictionare[word] += 1

    return dictionare


""" Combinar diccionarios sumando valores​
Dados dos diccionarios, combínalos sumando los valores de las claves comunes.​
Ejemplo: {"a": 10, "b": 20} y {"a": 5, "c": 30} → {"a": 15, "b": 20, "c": 30}.​ """

def merge_dicts_sum_values(dict_one={}, dict_two={}):

    dict_three = {}
    dict_three = dict_one.copy()

    for key, value in dict_two.items():
        if key not in dict_three:
            dict_three[key] = value
        else:
            dict_three[key] += value

    return dict_three


""" Clave con el valor máximo​
Encuentra la clave que tenga el valor más alto en un diccionario.​
Ejemplo: {"Juan": 85, "María": 92} → "María".​ """

def get_key_with_max_value(dict={}):

    #Con el método max()

    """ max_value = max(dict, key = dict.get)
    return max_value """

    #Opcion sin el metodo max()
    value_max = 0
    key_max = ''

    for key, value in dict.items():
        if value > value_max:
            value_max = value
            key_max = key
        else:
            return key_max

""" Filtrar por valor mínimo​
Crea un nuevo diccionario solo con las claves cuyos valores sean mayores que un umbral dado.​
Ejemplo: {"manzana": 50, "banana": 20}, umbral=30 → {"manzana": 50}.​ """

def filter_dict_by_min_value(dict={}, umbral=10):

    dictionare = {}

    for key, value in dict.items():
        if value > umbral:
            dictionare[key] = value     
            
    return dictionare


""" Invertir diccionario​
Intercambia claves y valores (asume que los valores son únicos).​
Ejemplo: {"a": 1, "b": 2} → {1: "a", 2: "b"}.​ """

def invert_dict(dict={}):

    dictionare = {}

    for key, value in dict.items():
        dictionare[value] = key     
            
    return dictionare



""" Diccionario de listas a lista de diccionarios​
Transforma un diccionario de listas en una lista de diccionarios (como una tabla).​
Ejemplo: {"nombre": ["Ana", "Juan"], "edad": [25, 30]} → [{"nombre": "Ana", "edad": 25}, {...}].​ """

def dict_of_lists_to_list_of_dicts(dict_de_listas):
    lista_de_diccionarios = []

    # Determinar el número de "filas" usando len()
    num_filas = 0
    alguna_clave = None
    for clave in dict_de_listas.keys(): # Usamos .keys()
        alguna_clave = clave
        break # Tomar la primera clave

    if alguna_clave is not None:
        num_filas = len(dict_de_listas[alguna_clave]) # Usamos len()

    # Iterar por cada "fila" usando range()
    for indice_fila in range(num_filas): # Usamos range()
        diccionario_fila = {}
        # Iterar por cada "columna" (clave) usando .keys()
        for clave in dict_de_listas.keys(): # Usamos .keys()
            lista_valores = dict_de_listas[clave]
            valor_fila = lista_valores[indice_fila]
            diccionario_fila[clave] = valor_fila

        lista_de_diccionarios.append(diccionario_fila)

    return lista_de_diccionarios


""" Eliminar claves con valores nulos​
Elimina las claves que tengan valores None, "" o 0.​
Ejemplo: {"nombre": "Carlos", "edad": 0} → {"nombre": "Carlos"}.​ """

def remove_null_values(diccionario):
    diccionario_limpio = {}
    if len(diccionario) == 0:
         return diccionario_limpio

    for clave, valor in diccionario.items(): # Usamos .items()
        if not (valor is None or valor == "" or valor == 0):
            diccionario_limpio[clave] = valor
    return diccionario_limpio

# Alternativa Fácil: (Versión in-place usando .keys() para obtener la lista de claves a iterar)
def eliminar_claves_valores_nulos_in_place_con_keys(diccionario):
    """Elimina claves con valores None, "", o 0 in-place, usando .keys() y len()."""
    if len(diccionario) == 0:
        return diccionario

    # Obtener las claves como una lista para poder iterar y modificar el dicc.
    claves_para_iterar = list(diccionario.keys()) # Usamos .keys() y list()

    for clave in claves_para_iterar:
        # Verificar si la clave todavía existe
        if clave in diccionario:
             valor = diccionario[clave]
             if valor is None or valor == "" or valor == 0:
                 del diccionario[clave]

    return diccionario

""" Aplanar diccionario anidado​
Convierte un diccionario anidado en uno plano con claves compuestas.​
Ejemplo: {"persona": {"nombre": "Ana"}} → {"persona_nombre": "Ana"}.​ """

def flatten_nested_dict(diccionario_anidado):
    diccionario_plano = {}
    if len(diccionario_anidado) == 0:
        return diccionario_plano

    for clave_exterior, valor_exterior in diccionario_anidado.items(): # Usamos .items()
        # Intentamos iterar el valor exterior para "adivinar" si es un diccionario anidado
        es_posible_diccionario_anidado = True
        try:
            for _ in valor_exterior: # Intentar iterar
                break
        except Exception:
             es_posible_diccionario_anidado = False

        if es_posible_diccionario_anidado:
             # Si parece un dict anidado, iteramos sobre sus items también
             for clave_interior, valor_interior in valor_exterior.items(): # Usamos .items() de nuevo
                 clave_plana = clave_exterior + "_" + clave_interior
                 diccionario_plano[clave_plana] = valor_interior
        else:
             # Si no es un dict anidado, copiar directamente
             diccionario_plano[clave_exterior] = valor_exterior

    return diccionario_plano


""" Ordenar diccionario por valor​
Ordena las claves de un diccionario por sus valores (ascendente o descendente).​
Ejemplo: {"A": 150, "B": 80} → {"B": 80, "A": 150} (ascendente).​ """

def csort_dict_by_value(diccionario, ascendente=True):
    lista_items = list(diccionario.items()) # Usamos .items() y list() para obtener la lista de pares

    longitud = len(lista_items) # Usamos len()

    if longitud == 0:
         return {} # Diccionario vacío

    # Implementar Bubble Sort directamente en la lista_items
    for i in range(longitud): # Usamos range()
        for j in range(longitud - i - 1): # Usamos range()
            # Comparar elementos basados en el valor (índice 1 de la tupla)
            val1_item = lista_items[j]
            val2_item = lista_items[j + 1]

            comp1 = val1_item[1] # Valor del primer item
            comp2 = val2_item[1] # Valor del segundo item

            intercambiar = False
            if ascendente:
                if comp1 > comp2:
                    intercambiar = True
            else: # Descendente
                if comp1 < comp2:
                    intercambiar = True

            if intercambiar:
                temp = lista_items[j]
                lista_items[j] = lista_items[j + 1]
                lista_items[j + 1] = temp

    # Crear un nuevo diccionario a partir de la lista ordenada de tuplas
    diccionario_ordenado = {}
    for item in lista_items: # Iterar sobre la lista ya ordenada
        clave = item[0]
        valor = item[1]
        diccionario_ordenado[clave] = valor # Los dicc. mantienen orden de inserción

    return diccionario_ordenado


""" Validar claves comunes entre diccionarios​
Verifica si dos diccionarios tienen al menos una clave en común.​
Ejemplo: {"a": 1} y {"b": 2} → False; {"a": 1} y {"a": 2} → True. """

def have_common_keys(dict1, dict2):
     # Iterar sobre las claves del primer diccionario
    for clave in dict1:
        # Verificar si esta clave existe en el segundo diccionario
        if clave in dict2:
            return True # Si se encuentra una clave común, retornar True inmediatamente

    # Si el bucle termina sin encontrar claves comunes
    return False


"""
----------------------------------------------------------------------
"""

def main():
    print(count_word_frequencies(["hola", "mundo", "hola"]))
    print(merge_dicts_sum_values({"a": 10, "b": 20}, {"a": 5, "c": 30}))
    print(get_key_with_max_value({"Juan": 85, "María": 92, "Camilo": 25}))
    print(filter_dict_by_min_value({"manzana": 50, "banana": 20},30))
    print(invert_dict({"A": 150, "B": 80}))
    print(dict_of_lists_to_list_of_dicts({"nombre": ["Ana", "Juan", "Elena"], "edad": [25, 30, 28], "ciudad": ["A", "B", "A"]}))
    print(remove_null_values({"nombre": "Carlos", "edad": 0, "ciudad": "", "país": None, "activo": True, "saldo": 100}))
    print(eliminar_claves_valores_nulos_in_place_con_keys({"nombre": "Carlos", "edad": 0, "ciudad": "", "país": None, "activo": True, "saldo": 100}))
    print(flatten_nested_dict({"persona": {"nombre": "Ana", "edad": 30}, "producto": {"tipo": "libro", "precio": 20}, "id": 123}))
    print(csort_dict_by_value({"A": 150, "B": 80, "C": 200, "D": 50}))
    print(have_common_keys({"a": 1, "b": 2},{"e": 5, "b": 6}))
main()