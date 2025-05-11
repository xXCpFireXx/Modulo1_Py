# 1. Suma de elementos de una lista
def suma_lista_solo_bucle(lista):
  """Calcula la suma de elementos usando solo un bucle."""
  total = 0 # Inicializamos el acumulador
  # Iteramos sobre cada elemento de la lista
  for elemento in lista:
    total += elemento # Sumamos el elemento al total
  return total

# Alternativa (usando while y acceso por índice)
def suma_lista_bucle_while_indice(lista):
    """Calcula la suma de elementos usando un bucle while y acceso por índice."""
    total = 0
    indice = 0
    while indice < len(lista):
        total += lista[indice]
        indice += 1
    return total


# 2. Eliminar duplicados de una lista (manteniendo el orden)
def eliminar_duplicados_solo_bucle(lista):
  """Elimina duplicados manteniendo el orden usando un bucle y lista auxiliar."""
  lista_sin_duplicados = [] # Lista para almacenar los elementos únicos en orden
  # Iteramos sobre cada elemento de la lista original
  for elemento in lista:
    # Verificamos si el elemento ya está en la nueva lista (esta verificación es un bucle implícito)
    ya_visto = False
    for unico in lista_sin_duplicados:
        if elemento == unico:
            ya_visto = True
            break # Si lo encontramos, marcamos y salimos del bucle interno
    
    if not ya_visto:
      lista_sin_duplicados.append(elemento) # Si no se ha visto, lo añadimos
  return lista_sin_duplicados

# Nota: Sin 'set', la verificación 'elemento not in lista_sin_duplicados' 
# es la forma más directa de hacerlo solo con bucles y listas.


# 3. Invertir una lista (sin métodos built-in, solo bucle)
def invertir_lista_solo_bucle_nuevo(lista):
  """Invierte la lista creando una nueva lista en orden inverso usando bucle y acceso por índice."""
  lista_invertida = [] # Nueva lista vacía
  longitud = len(lista)
  # Iterar desde el último índice hasta el primero
  indice = longitud - 1
  while indice >= 0:
    lista_invertida.append(lista[indice]) # Añadir el elemento al final de la nueva lista
    indice -= 1
  return lista_invertida

# Alternativa (in-place, modifica la lista original)
def invertir_lista_solo_bucle_in_place(lista):
  """Invierte la lista en su lugar usando un bucle y dos punteros (modifica la lista original)."""
  izquierda = 0
  derecha = len(lista) - 1
  # Mientras los punteros no se crucen
  while izquierda < derecha:
    # Intercambiar elementos
    temporal = lista[izquierda]
    lista[izquierda] = lista[derecha]
    lista[derecha] = temporal
    # Mover punteros
    izquierda += 1
    derecha -= 1
  return lista # Retorna la lista modificada


# 4. Contador de palabras
def contador_palabras_solo_bucle(lista_palabras):
  """Cuenta la frecuencia de palabras usando solo un bucle y un diccionario."""
  conteo = {} # Diccionario vacío para almacenar los conteos
  # Iteramos sobre cada palabra de la lista
  for palabra in lista_palabras:
    # Verificamos si la palabra ya es una clave en el diccionario
    if palabra in conteo:
      conteo[palabra] += 1 # Si existe, incrementamos su valor
    else:
      conteo[palabra] = 1 # Si no existe, la añadimos con valor 1
  return conteo


# 5. Combinar dos listas ordenadas
def combinar_listas_ordenadas_solo_bucle_merge(lista1, lista2):
    """Combina dos listas ordenadas usando solo bucles y acceso por índice (algoritmo de fusión)."""
    combinada = [] # Lista para la combinación
    i = 0 # Índice para lista1
    j = 0 # Índice para lista2
    # Mientras haya elementos en ambas listas
    while i < len(lista1) and j < len(lista2):
        # Comparamos los elementos actuales
        if lista1[i] < lista2[j]:
            combinada.append(lista1[i]) # Añadimos el de lista1 si es menor
            i += 1 # Movemos el puntero de lista1
        else:
            combinada.append(lista2[j]) # Añadimos el de lista2 si es menor o igual
            j += 1 # Movemos el puntero de lista2

    # Añadir elementos restantes de lista1 (si los hay)
    while i < len(lista1):
        combinada.append(lista1[i])
        i += 1

    # Añadir elementos restantes de lista2 (si los hay)
    while j < len(lista2):
        combinada.append(lista2[j])
        j += 1

    return combinada

# Nota: La alternativa de concatenar y luego ordenar está prohibida por la restricción de no usar sort().


# 6. Mayor y menor de una tupla
def mayor_menor_tupla_solo_bucle(tupla):
  """Encuentra el mayor y menor de una tupla usando solo un bucle y acceso por índice."""
  if not tupla: # Manejar caso de tupla vacía
      return (None, None)

  # Inicializamos mayor y menor con el primer elemento
  mayor = tupla[0]
  menor = tupla[0]

  # Iteramos desde el segundo elemento hasta el final
  indice = 1
  while indice < len(tupla):
    elemento = tupla[indice]
    # Comparamos y actualizamos mayor si es necesario
    if elemento > mayor:
      mayor = elemento
    # Comparamos y actualizamos menor si es necesario
    if elemento < menor:
      menor = elemento
    indice += 1

  return (mayor, menor)

# Alternativa (usando for)
def mayor_menor_tupla_bucle_for(tupla):
  """Encuentra el mayor y menor de una tupla usando solo un bucle for."""
  if not tupla:
      return (None, None)

  mayor = tupla[0]
  menor = tupla[0]

  for elemento in tupla:
      if elemento > mayor:
          mayor = elemento
      if elemento < menor:
          menor = elemento
  return (mayor, menor)


# 7. Desempaquetado de tuplas
def desempaquetar_tupla_solo_indice(tupla):
    """Desempaqueta la tupla accediendo solo por índice."""
    # Asignar cada valor a una variable usando su índice
    # (Asumimos que la tupla siempre tiene 4 elementos para este ejemplo)
    if len(tupla) == 4:
        a = tupla[0]
        b = tupla[1]
        c = tupla[2]
        d = tupla[3]
        # Imprimir los resultados (la impresión sí usa función built-in 'print', que asumimos permitida para mostrar resultados)
        print(f"a={a}, b={b}, c={c}, d={d}")
    else:
        print("La tupla no tiene 4 elementos para desempaquetar con esta función.")

# Nota: El desempaquetado directo `a, b, c, d = tupla` es una sintaxis especial, 
# no un bucle o acceso por índice estricto, por lo que se evita según la restricción.


# 8. Convertir tupla a lista y viceversa
def tupla_a_lista_solo_bucle(tupla_original):
  """Convierte una tupla a lista usando solo un bucle."""
  lista = [] # Creamos una lista vacía
  # Iteramos sobre cada elemento de la tupla
  for elemento in tupla_original:
    lista.append(elemento) # Añadimos el elemento a la lista
  return lista

# Añadir un elemento a la lista (ya convertida) es una operación básica de lista:
# lista.append(elemento_a_añadir)

# *** Limitación bajo las restricciones: ***
# Convertir una lista de nuevo a una tupla sin usar la función 'tuple()'
# o la concatenación de tuplas con el operador '+' NO es posible
# usando solo bucles y operaciones básicas de lista/tupla en Python,
# debido a la inmutabilidad de las tuplas. No hay una forma de construir
# una tupla elemento a elemento en un bucle y que el resultado sea un objeto tupla,
# excepto creando nuevas tuplas por concatenación en cada paso, lo cual 
# sigue usando sintaxis de tupla y el operador '+'.
# Por lo tanto, solo podemos mostrar la conversión de tupla a lista con bucles.


# 9. Diccionario desde lista de tuplas
def dict_desde_lista_tuplas_solo_bucle(lista_tuplas):
  """Convierte lista de tuplas (clave, valor) a diccionario usando solo un bucle."""
  diccionario = {} # Creamos un diccionario vacío
  # Iteramos sobre cada tupla en la lista
  for tupla_kv in lista_tuplas:
    # Accedemos a la clave (primer elemento de la tupla)
    clave = tupla_kv[0]
    # Accedemos al valor (segundo elemento de la tupla)
    valor = tupla_kv[1]
    # Asignamos el par clave-valor al diccionario
    diccionario[clave] = valor
  return diccionario


# 10. Ordenar lista de tuplas por elemento
def ordenar_lista_tuplas_burbuja(lista_tuplas, indice):
  """Ordena lista de tuplas por el elemento en el índice especificado usando Bubble Sort (solo bucles)."""
  longitud = len(lista_tuplas)
  # Implementación de Bubble Sort
  # Bucle exterior para controlar las pasadas
  for i in range(longitud):
    # Bucle interior para comparar elementos adyacentes
    # La última i elementos ya están en su lugar
    for j in range(longitud - i - 1):
      # Comparamos los elementos en el 'indice' especificado de las tuplas adyacentes
      if lista_tuplas[j][indice] > lista_tuplas[j + 1][indice]:
        # Si están en el orden incorrecto, los intercambiamos
        temporal = lista_tuplas[j]
        lista_tuplas[j] = lista_tuplas[j + 1]
        lista_tuplas[j + 1] = temporal
  return lista_tuplas # Retorna la lista modificada (ordenada in-place)

# Alternativa (usando Insertion Sort)
def ordenar_lista_tuplas_insercion(lista_tuplas, indice):
    """Ordena lista de tuplas por el elemento en el índice especificado usando Insertion Sort (solo bucles)."""
    longitud = len(lista_tuplas)
    # Implementación de Insertion Sort
    # Iteramos desde el segundo elemento hasta el final
    for i in range(1, longitud):
        elemento_actual = lista_tuplas[i]
        posicion = i

        # Mover elementos de la sublista ordenada que son mayores 
        # que elemento_actual (basado en el 'indice')
        while posicion > 0 and lista_tuplas[posicion - 1][indice] > elemento_actual[indice]:
            lista_tuplas[posicion] = lista_tuplas[posicion - 1]
            posicion -= 1

        # Insertar elemento_actual en la posición correcta
        lista_tuplas[posicion] = elemento_actual

    return lista_tuplas # Retorna la lista modificada (ordenada in-place)

# Nota: Aquí hemos implementado algoritmos de ordenación básicos usando solo bucles y 
# acceso por índice para cumplir la restricción de no usar sort() o sorted() con 'key'.


# --- Ejemplos de uso con las funciones que cumplen las restricciones ---
print("--- 1. Suma de elementos de una lista (solo bucle) ---")
mi_lista_suma = [1, 2, 3, 4, 5]
print(f"Lista: {mi_lista_suma}")
print(f"Suma (solo bucle): {suma_lista_solo_bucle(mi_lista_suma)}")
print(f"Suma (bucle while indice): {suma_lista_bucle_while_indice(mi_lista_suma)}")

print("\n--- 2. Eliminar duplicados de una lista (solo bucle, manteniendo orden) ---")
mi_lista_duplicados = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(f"Lista original: {mi_lista_duplicados}")
print(f"Sin duplicados (solo bucle, ordenado): {eliminar_duplicados_solo_bucle(mi_lista_duplicados)}")

print("\n--- 3. Invertir una lista (solo bucle) ---")
mi_lista_invertir = [10, 20, 30, 40]
print(f"Lista original: {mi_lista_invertir}")
print(f"Lista invertida (solo bucle, nuevo): {invertir_lista_solo_bucle_nuevo(mi_lista_invertir)}")
# Creamos una copia para el in-place
mi_lista_invertir_inplace = [10, 20, 30, 40]
print(f"Lista invertida (solo bucle, in-place): {invertir_lista_solo_bucle_in_place(mi_lista_invertir_inplace)}")

print("\n--- 4. Contador de palabras (solo bucle) ---")
mi_lista_palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]
print(f"Lista de palabras: {mi_lista_palabras}")
print(f"Conteo (solo bucle): {contador_palabras_solo_bucle(mi_lista_palabras)}")

print("\n--- 5. Combinar dos listas ordenadas (solo bucle merge) ---")
lista_a = [1, 3, 5]
lista_b = [2, 4, 6]
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Combinada (solo bucle merge): {combinar_listas_ordenadas_solo_bucle_merge(lista_a, lista_b)}")

print("\n--- 6. Mayor y menor de una tupla (solo bucle) ---")
mi_tupla_minmax = (5, 2, 9, 1, 7, 2)
print(f"Tupla: {mi_tupla_minmax}")
print(f"Mayor y menor (solo bucle while): {mayor_menor_tupla_solo_bucle(mi_tupla_minmax)}")
print(f"Mayor y menor (solo bucle for): {mayor_menor_tupla_bucle_for(mi_tupla_minmax)}")

print("\n--- 7. Desempaquetado de tuplas (solo índice) ---")
mi_tupla_desempaquetar = (3, 5, 7, 9)
print(f"Tupla a desempaquetar: {mi_tupla_desempaquetar}")
print("Desempaquetado (solo índice):")
desempaquetar_tupla_solo_indice(mi_tupla_desempaquetar)

print("\n--- 8. Convertir tupla a lista (solo bucle) ---")
mi_tupla_convertir = (1, 2, 3)
elemento_nuevo = 4
print(f"Tupla original: {mi_tupla_convertir}")
lista_resultante = tupla_a_lista_solo_bucle(mi_tupla_convertir)
print(f"Convertida a lista (solo bucle): {lista_resultante}")
lista_resultante.append(elemento_nuevo) # Añadir elemento a la lista
print(f"Lista con elemento añadido: {lista_resultante}")
# Explicación de la limitación para convertir de vuelta a tupla sin built-ins
print("\n*** Nota sobre convertir lista a tupla sin built-ins ***")
print("Bajo la restricción de usar solo bucles y operaciones básicas,")
print("no es posible convertir una lista de nuevo a una tupla sin usar")
print("la función 'tuple()' o la concatenación de tuplas, debido a la inmutabilidad.")


print("\n--- 9. Diccionario desde lista de tuplas (solo bucle) ---")
mi_lista_tuplas_dict = [("a", 1), ("b", 2), ("c", 3), ("a", 10)] # Nota: Si hay claves repetidas, la última prevalece
print(f"Lista de tuplas: {mi_lista_tuplas_dict}")
print(f"Diccionario (solo bucle): {dict_desde_lista_tuplas_solo_bucle(mi_lista_tuplas_dict)}")

print("\n--- 10. Ordenar lista de tuplas por elemento (solo bucles de ordenación) ---")
mi_lista_tuplas_ordenar = [(1, 4), (3, 2), (5, 1), (2, 4)]
print(f"Lista de tuplas original: {mi_lista_tuplas_ordenar}")
# Crear copias porque los algoritmos de ordenación modifican la lista original
lista_burbuja = [tupla for tupla in mi_lista_tuplas_ordenar] # Copia manual con bucle
lista_insercion = [tupla for tupla in mi_lista_tuplas_ordenar] # Copia manual con bucle

print(f"Ordenada por 2do elem (Bubble Sort): {ordenar_lista_tuplas_burbuja(lista_burbuja, 1)}")
print(f"Ordenada por 2do elem (Insertion Sort): {ordenar_lista_tuplas_insercion(lista_insercion, 1)}")