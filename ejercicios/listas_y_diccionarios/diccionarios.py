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

def dict_of_lists_to_list_of_dicts():

    return


""" Eliminar claves con valores nulos​
Elimina las claves que tengan valores None, "" o 0.​
Ejemplo: {"nombre": "Carlos", "edad": 0} → {"nombre": "Carlos"}.​ """

def remove_null_values():

    return


""" Aplanar diccionario anidado​
Convierte un diccionario anidado en uno plano con claves compuestas.​
Ejemplo: {"persona": {"nombre": "Ana"}} → {"persona_nombre": "Ana"}.​ """

def flatten_nested_dict():

    return


""" Ordenar diccionario por valor​
Ordena las claves de un diccionario por sus valores (ascendente o descendente).​
Ejemplo: {"A": 150, "B": 80} → {"B": 80, "A": 150} (ascendente).​ """

def csort_dict_by_value():

    return


""" Validar claves comunes entre diccionarios​
Verifica si dos diccionarios tienen al menos una clave en común.​
Ejemplo: {"a": 1} y {"b": 2} → False; {"a": 1} y {"a": 2} → True. """

def have_common_keys():

    return


"""
----------------------------------------------------------------------
"""

def main():
    print(count_word_frequencies(["hola", "mundo", "hola"]))
    print(merge_dicts_sum_values({"a": 10, "b": 20}, {"a": 5, "c": 30}))
    print(get_key_with_max_value({"Juan": 85, "María": 92, "Camilo": 25}))
    print(filter_dict_by_min_value({"manzana": 50, "banana": 20},30))
    print(invert_dict({"A": 150, "B": 80}))
    print(dict_of_lists_to_list_of_dicts())
    #print(remove_null_values())
    #print(flatten_nested_dict())
    #print(csort_dict_by_value())
    #print(have_common_keys())
main()