# import time # Puedes descomentar si quieres usar time.sleep() para pausas

print("\n ----------------- SISTEMA DE GESTIÓN DE LIBROS DE BIBLIOTECA -----------------\n")

# --- Configuración ---
VALID_GENRES = ["Fiction", "NonFiction", "Science", "Biography", "Children"]
MIN_PUB_YEAR = 1800 # Año mínimo de publicación aceptado
MAX_PUB_YEAR = 2025 # Año máximo de publicación aceptado (para evitar años futuros sin datetime)

# Diccionario principal para almacenar los libros
library = {}

# --- FUNCIONES AUXILIARES ---

# Función para formatear la lista de géneros (Reutilizada)
def format_genre_list(genre_list):
    """Formatea una lista de géneros en una cadena separada por comas."""
    formatted_string = ""
    list_length = len(genre_list)

    for i in range(list_length):
        formatted_string += genre_list[i]

        if i < list_length - 1:
            formatted_string += ", "

    return formatted_string

# Función para validar cadenas de texto no vacías (Reutilizada)
def get_non_empty_string_input(prompt):
    """Solicita al usuario una cadena de texto no vacía y la retorna limpia."""
    while True:
        user_input = input(prompt).strip()

        if user_input == "":
            print("\n---------------------------------")
            print("⚠️ Entrada vacía. Por favor, ingrese un valor.")
            print("---------------------------------\n")
        else:
            return user_input

# Función para validar números enteros positivos (Reutilizada)
def get_positive_integer_input(prompt):
    """Solicita al usuario un número entero positivo."""
    while True:
        user_input = input(prompt)

        try:
            number = int(user_input)

            if number > 0:
                return number
            else:
                print("\n---------------------------------")
                print("⚠️ Ingrese un número entero positivo.")
                print("---------------------------------\n")
        except ValueError:
            print("\n---------------------------------")
            print("⚠️ Entrada inválida. Ingrese un número entero válido.")
            print("---------------------------------\n")

# Función para validar números flotantes positivos (Reutilizada)
def get_positive_float_input(prompt):
    """Solicita al usuario un número flotante positivo."""
    while True:
        user_input = input(prompt)

        try:
            number = float(user_input)

            if number >= 0:
                return number
            else:
                print("\n---------------------------------")
                print("⚠️ Ingrese un número positivo o cero.")
                print("---------------------------------\n")
        except ValueError:
            print("\n---------------------------------")
            print("⚠️ Entrada inválida. Ingrese un número válido.")
            print("---------------------------------\n")

# Función para validar el año de publicación (Reutilizada)
def get_valid_year_input(prompt):
    """Solicita al usuario un año de publicación válido."""
    while True:
        user_input = input(prompt)
        try:
            year = int(user_input)
            if MIN_PUB_YEAR <= year <= MAX_PUB_YEAR:
                return year
            else:
                print(f"\n---------------------------------")
                print(f"⚠️ Año inválido. Ingrese un valor entre {MIN_PUB_YEAR} y {MAX_PUB_YEAR}.")
                print(f"---------------------------------\n")
        except ValueError:
            print("\n---------------------------------")
            print("⚠️ Entrada inválida. Ingrese un número entero para el año.")
            print("---------------------------------\n")


# --- FUNCIONES PRINCIPALES DE GESTIÓN (Nombres en inglés) ---

# Función para buscar libros (Adaptada de find_book, ahora busca por título O autor, retorna lista)
def find_books(search_term, search_type, library_data):
    """Busca libros por título o autor (insensible a mayúsculas/minúsculas) y retorna una lista de libros que coinciden."""
    found_list = []
    cleaned_term = search_term.strip().lower()

    if search_type == "title":
        # Buscar por título (verificación directa de clave, comparando en minúsculas)
        # Recorremos las claves en minúsculas para encontrar la clave original si existe
        original_title = None
        for title_key in library_data.keys(): # Usamos .keys()
            if title_key.strip().lower() == cleaned_term:
                original_title = title_key
                break # Encontramos la clave original

        if original_title: # Si encontramos una coincidencia (insensible a mayúsculas)
            found_list.append((original_title, library_data[original_title])) # Añadir tupla (título original, detalles)

    elif search_type == "author":
        # Buscar por autor (iterar sobre valores, comparando autor en minúsculas)
        for title, details in library_data.items(): # Usamos .items()
            if details["author"].strip().lower() == cleaned_term:
                 found_list.append((title, details)) # Añadir tupla (título, detalles)

    return found_list # Retorna una lista de tuplas (título, detalles)


# 1. Registrar nuevos libros
def register_new_book(library_data):
    """Permite al usuario registrar un nuevo libro en el catálogo."""
    print("\n---------------------------------")
    print("📚 REGISTRAR NUEVO LIBRO")
    print("---------------------------------\n")

    title = get_non_empty_string_input("👉 Ingrese el TÍTULO del libro:\n")

    # Verificar si el libro ya existe por título (insensible a mayúsculas/minúsculas)
    existing_book_list = find_books(title, "title", library_data)

    if len(existing_book_list) > 0: # Usamos len()
        # Si find_books encontró algo por título, significa que ya existe (insensible a mayúsculas)
        # existing_book_list[0][0] contiene el título original encontrado en el diccionario
        print(f"\n⚠️ El libro '{existing_book_list[0][0]}' ya existe en el catálogo.")
        print("Utilice la opción 'Actualizar información' para modificarlo.")
        # if 'time' in globals(): time.sleep(2)
        return

    # Si el libro no existe, obtenemos los demás datos
    author = get_non_empty_string_input("👉 Ingrese el AUTOR:\n")

    while True:
        genre_input = get_non_empty_string_input(f"👉 Ingrese el GÉNERO ({format_genre_list(VALID_GENRES)}):\n")
        if genre_input in VALID_GENRES:
            genre = genre_input
            break
        else:
            print(f"\n---------------------------------")
            print(f"⚠️ Género inválido. Los géneros permitidos son: {format_genre_list(VALID_GENRES)}")
            print(f"---------------------------------\n")

    year = get_valid_year_input("👉 Ingrese el AÑO de publicación:\n")
    quantity = get_positive_integer_input("👉 Ingrese la CANTIDAD DISPONIBLE inicial:\n")
    price = get_positive_float_input("👉 Ingrese el PRECIO de reposición:\n")

    # Añadir el nuevo libro al diccionario (usando el título tal como se ingresó, pero limpio de espacios)
    library_data[title.strip()] = {
        "author": author,
        "genre": genre,
        "year": year,
        "quantity": quantity,
        "price": price
    }
    print(f"\n✅ Libro '{title.strip()}' registrado correctamente.")
    # if 'time' in globals(): time.sleep(1)


# 2. Buscar libros en el catálogo
def search_book_in_catalog(library_data):
    """Permite al usuario buscar libros por título o autor y muestra los resultados."""
    print("\n---------------------------------")
    print("🔍 BUSCAR LIBROS")
    print("---------------------------------\n")

    print("Buscar por:")
    print("1. Título")
    print("2. Autor")
    search_option = get_non_empty_string_input("👉 Seleccione el tipo de búsqueda (1 o 2):\n").strip()

    search_term = get_non_empty_string_input("👉 Ingrese el término de búsqueda:\n")

    found_books = []
    if search_option == "1":
        found_books = find_books(search_term, "title", library_data)
    elif search_option == "2":
        found_books = find_books(search_term, "author", library_data)
    else:
        print("\n⚠️ Opción de búsqueda inválida. Intente de nuevo.")
        # if 'time' in globals(): time.sleep(2)
        return

    # Mostrar resultados
    if len(found_books) == 0: # Usamos len()
        print("Book not found.\n") # Mensaje en inglés
        print("¿Desea registrarlo? (Utilice la opción 1 del menú principal)")
        # if 'time' in globals(): time.sleep(2)
    else:
        print("\n--- Resultados de la Búsqueda ---")
        # Implementación simple de Bubble Sort para ordenar los resultados por título (primer elemento de la tupla)
        n = len(found_books) # Usamos len()
        for i in range(n): # Usamos range()
            for j in range(0, n - i - 1): # Usamos range()
                 # found_books es una lista de tuplas (título, detalles)
                 # Comparar por el título (found_books[j][0])
                 if found_books[j][0] > found_books[j + 1][0]: # Acceso al título en la tupla
                     temp = found_books[j]
                     found_books[j] = found_books[j + 1]
                     found_books[j + 1] = temp # <-- CORRECCIÓN: Eliminar el paréntesis extra aquí
         # Fin de la implementación Bubble Sort

        for title, details in found_books:
            print(f"Título: {title}")
            print(f"Autor: {details['author']}")
            print(f"Género: {details['genre']}")
            print(f"Año: {details['year']}")
            print(f"Cantidad Disponible: {details['quantity']}")
            print(f"Precio Reposición: ${details['price']:.2f}")
            print("---")
        print("---------------------------------\n")
        # if 'time' in globals(): time.sleep(5)


# 3. Actualizar información
def update_book_info(library_data):
    """Permite actualizar la cantidad o el precio de un libro existente."""
    print("\n---------------------------------")
    print("✏️ ACTUALIZAR INFORMACIÓN DEL LIBRO")
    print("---------------------------------\n")

    # Solicitamos el título (insensible a mayúsculas para encontrarlo)
    title_to_update = get_non_empty_string_input("👉 Ingrese el TÍTULO del libro a actualizar:\n")

    # Buscar el libro por título (usando find_books)
    found_list = find_books(title_to_update, "title", library_data)

    if len(found_list) == 0: # Usamos len()
        print("Book not found.\n")
        # if 'time' in globals(): time.sleep(2)
        return

    # Si se encontró el libro (find_books por título debería devolver 0 o 1 resultado con esta lógica)
    # found_list[0] es la tupla (título_original, detalles)
    original_title, book_details = found_list[0]

    print(f"\nLibro encontrado: '{original_title}'")
    print("¿Qué información desea actualizar?")
    print("1. Cantidad Disponible")
    print("2. Precio de Reposición")
    update_option = get_non_empty_string_input("👉 Seleccione una opción (1 o 2):\n").strip()

    if update_option == "1":
        new_quantity = get_positive_integer_input(f"👉 Ingrese la NUEVA Cantidad Disponible para '{original_title}':\n")
        book_details["quantity"] = new_quantity # Actualiza directamente en el diccionario original
        print(f"\n✅ Cantidad disponible de '{original_title}' actualizada a {new_quantity}.")
        # if 'time' in globals(): time.sleep(2)
    elif update_option == "2":
        new_price = get_positive_float_input(f"👉 Ingrese el NUEVO Precio de Reposición para '{original_title}':\n")
        book_details["price"] = new_price # Actualiza directamente
        print(f"\n✅ Precio de reposición de '{original_title}' actualizado a ${new_price:.2f}.")
        # if 'time' in globals(): time.sleep(2)
    else:
        print("\n⚠️ Opción de actualización inválida.")
        # if 'time' in globals(): time.sleep(2)


# 4. Eliminar libros obsoletos (Adaptada de delete_product)
def delete_obsolete_book(library_data):
    """Permite eliminar un libro del catálogo previa confirmación."""
    print("\n---------------------------------")
    print("🗑️ ELIMINAR LIBRO")
    print("---------------------------------\n")

    # Solicitamos el título (insensible a mayúsculas para encontrarlo)
    title_to_delete = get_non_empty_string_input("👉 Ingrese el TÍTULO del libro a eliminar:\n")

    # Buscar el libro por título (usando find_books)
    found_list = find_books(title_to_delete, "title", library_data)

    if len(found_list) == 0: # Usamos len()
        print("Book not found.\n")
        # if 'time' in globals(): time.sleep(2)
        return

    # Si se encontró el libro
    original_title, book_details = found_list[0]

    # Solicitar confirmación
    confirm = get_non_empty_string_input(f"👉 ¿Está seguro de eliminar el libro '{original_title}'? (sí/no):\n").strip().lower()

    if confirm == "sí" or confirm == "si":
        del library_data[original_title] # Elimina la entrada del diccionario
        print(f"\n✅ Libro '{original_title}' eliminado del catálogo.")
        # if 'time' in globals(): time.sleep(2)
    else:
        print(f"\n❌ Eliminación de '{original_title}' cancelada.")
        # if 'time' in globals(): time.sleep(2)


# 5. Generar reportes (Adaptada)
def generate_reports(library_data):
    """Genera y muestra diferentes reportes sobre el inventario."""
    print("\n---------------------------------")
    print("📊 GENERAR REPORTES")
    print("---------------------------------\n")

    print("Seleccione el reporte a generar:")
    print("1. Valor Total de Reposición del Inventario")
    print("2. Libro más Antiguo y más Reciente por Género")
    report_option = get_non_empty_string_input("👉 Ingrese una opción (1 o 2):\n").strip()

    if report_option == "1":
        # Reporte 1: Valor Total de Reposición
        total_replacement_value = 0.0
        # Iterar sobre los valores (detalles del libro)
        for book_details in library_data.values(): # Usamos .values()
             # Asegurarse de que quantity y price existan y sean numéricos (aunque get_..._input los valida)
             # Aquí confiamos en la estructura de datos que add_book crea.
             total_replacement_value += book_details["quantity"] * book_details["price"]

        print("\n--- Reporte: Valor Total de Reposición ---")
        print(f"Valor total de reposición del inventario: ${total_replacement_value:.2f}") # Formato a 2 decimales
        print("------------------------------------------\n")
        # if 'time' in globals(): time.sleep(3)

    elif report_option == "2":
        # Reporte 2: Libro más Antiguo y más Reciente por Género
        print("\n--- Reporte: Libro más Antiguo y más Reciente por Género ---")

        # 1. Agrupar libros por género y encontrar el más antiguo y reciente en cada uno
        genre_year_info = {} # {"Genero": {"oldest": (title, year), "newest": (title, year)}}

        # Iterar sobre los items del diccionario principal
        if len(library_data) == 0: # Usamos len()
            print("No hay libros registrados para generar este reporte.")
            # if 'time' in globals(): time.sleep(2)
            return # Salir si no hay libros

        for title, details in library_data.items(): # Usamos .items()
             genre = details.get("genre", "Desconocido") # Usamos .get() para seguridad si el género falta
             year = details.get("year", MAX_PUB_YEAR + 1) # Usamos .get() y un año "futuro" si falta para no ser el más antiguo/reciente

             if genre not in genre_year_info:
                 # Si es el primer libro de este género, inicializar
                 genre_year_info[genre] = {
                     "oldest": (title, year), # Guardar como tupla (título, año)
                     "newest": (title, year)
                 }
             else:
                 # Comparar con el libro más antiguo/reciente registrado para este género
                 current_oldest_year = genre_year_info[genre]["oldest"][1] # Obtener el año del más antiguo
                 current_newest_year = genre_year_info[genre]["newest"][1] # Obtener el año del más reciente

                 if year < current_oldest_year:
                     genre_year_info[genre]["oldest"] = (title, year) # Actualizar el más antiguo
                 if year > current_newest_year:
                      genre_year_info[genre]["newest"] = (title, year) # Actualizar el más reciente

        # 2. Mostrar los resultados por género
        if len(genre_year_info) == 0: # Usamos len()
            # Este caso no debería ocurrir si library_data no estaba vacío, pero es una buena práctica.
            print("No hay información de género disponible.")
        else:
            # Iterar sobre los géneros encontrados
            for genre, year_info in genre_year_info.items(): # Usamos .items()
                 oldest_book = year_info["oldest"] # Tupla (título, año)
                 newest_book = year_info["newest"] # Tupla (título, año)

                 print(f"\nGénero: {genre}")
                 print(f"  Más antiguo: '{oldest_book[0]}' ({oldest_book[1]})")
                 print(f"  Más reciente: '{newest_book[0]}' ({newest_book[1]})")

        print("----------------------------------------------------------\n")
        # if 'time' in globals(): time.sleep(5)

    else:
        print("\n⚠️ Opción de reporte inválida. Intente de nuevo.")
        # if 'time' in globals(): time.sleep(2)


# --- INICIALIZACIÓN DE DATOS (Precargar 5 libros) ---
# Usamos la función register_new_book para añadir los libros iniciales de forma limpia
# Esto garantiza que pasen por las validaciones y se añadan correctamente
def preload_initial_books(library_data):
     """Precarga 5 libros ejemplo en la biblioteca."""
     print("Precargando libros iniciales...")
     # Llamamos directamente la lógica de register_new_book con datos fijos
     # No es ideal, pero simula el proceso sin entrada de usuario en el inicio.
     # Una forma más limpia sería tener una función interna add_book_data(details)
     # y que register_new_book la llame después de validar inputs.
     # Para este ejemplo, simulemos la adición directa para 5 libros.

     books_to_preload = [
         {"title": "Cien años de soledad", "author": "Gabriel García Márquez", "genre": "Fiction", "year": 1967, "quantity": 5, "price": 25.50},
         {"title": "1984", "author": "George Orwell", "genre": "Fiction", "year": 1949, "quantity": 3, "price": 18.00},
         {"title": "Cosmos", "author": "Carl Sagan", "genre": "Science", "year": 1980, "quantity": 4, "price": 30.75},
         {"title": "La sombra del viento", "author": "Carlos Ruiz Zafón", "genre": "Fiction", "year": 2001, "quantity": 2, "price": 22.00},
         {"title": "Ensayo sobre la ceguera", "author": "José Saramago", "genre": "Fiction", "year": 1995, "quantity": 3, "price": 20.00},
         # Puedes añadir más aquí si quieres probar con más datos
     ]

     for book_data in books_to_preload:
         # Asegurarse de que el título no esté vacío antes de añadir
         if book_data["title"].strip() != "":
              # Añadir directamente al diccionario, simulando la salida validada de get_..._input
              # Esto omite la verificación de duplicados al inicio, pero es solo para precarga.
              library_data[book_data["title"].strip()] = {
                  "author": book_data["author"].strip(),
                  "genre": book_data["genre"], # Asumimos género válido en precarga
                  "year": book_data["year"], # Asumimos año válido
                  "quantity": book_data["quantity"], # Asumimos cantidad válida
                  "price": book_data["price"] # Asumimos precio válido
              }
     print(f"Se precargaron {len(books_to_preload)} libros.") # Usamos len()
     # if 'time' in globals(): time.sleep(1)


# --- FUNCIÓN PRINCIPAL (Menú Interactivo) ---
def main():
    # Precargar los libros iniciales antes de iniciar el menú
    preload_initial_books(library)

    while True:
        print("\n------------ MENÚ PRINCIPAL DE GESTIÓN DE LIBROS ------------\n")
        print("1. 📚 Registrar Nuevo Libro")
        print("2. 🔍 Buscar Libro en Catálogo")
        print("3. ✏️ Actualizar Información de Libro")
        print("4. 🗑️ Eliminar Libro Obsoleto")
        print("5. 📊 Generar Reportes")
        print("6. 👋 SALIR\n")

        user_option = input("👉 Ingrese una OPCIÓN (1-6): \n").strip()

        if user_option == "1":
            register_new_book(library)
        elif user_option == "2":
            search_book_in_catalog(library)
        elif user_option == "3":
            update_book_info(library)
        elif user_option == "4":
            delete_obsolete_book(library)
        elif user_option == "5":
            generate_reports(library)
        elif user_option == "6":
            print("\n🚪 Saliendo del Sistema de Gestión de Libros. ¡Adiós!\n")
            break
        else:
            print("\n⚠️ Error: Ingrese una opción válida del 1 al 6.\n")

# Llamar a la función principal al ejecutar el script
if __name__ == "__main__":
    main()