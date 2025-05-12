# import time # Importar si quieres usar time.sleep()

print("\n ----------------- SISTEMA DE GESTIÓN DE BIBLIOTECA -----------------\n")

# Lista predefinida de géneros válidos
VALID_GENRES = ["Fiction", "NonFiction", "Science", "Biography", "Children"]

# Diccionario principal para almacenar los libros
library = {}

# --- FUNCIÓN AUXILIAR (Adaptada del código de inventario) ---
# Reemplaza el uso de .join()
def format_genre_list(genre_list):
    """Formatea una lista de géneros en una cadena separada por comas."""
    formatted_string = ""
    list_length = len(genre_list)

    for i in range(list_length):
        formatted_string += genre_list[i]

        if i < list_length - 1:
            formatted_string += ", "

    return formatted_string


# --- FUNCIONES AUXILIARES (Adaptadas del código de inventario) ---

# Función para validar cadenas de texto no vacías
def get_valid_string(print_text):
    """Solicita al usuario una cadena de texto no vacía."""
    while True:
        user_input = input(print_text).strip()

        if user_input == "":
            print("\n---------------------------------")
            print("⚠️ Texto vacío. Por favor, ingrese un valor.")
            print("---------------------------------\n")
        else:
            return user_input

# Función para validar números positivos
def get_positive_integer(print_text):
    """Solicita al usuario un número entero positivo."""
    while True:
        user_input = input(print_text)

        try:
            number = int(user_input)

            if number > 0:
                return number
            else:
                print("\n---------------------------------")
                print("⚠️ Ingrese un número positivo.")
                print("---------------------------------\n")
        except ValueError:
            print("\n---------------------------------")
            print("⚠️ Ingrese un número válido (entero).")
            print("---------------------------------\n")


# --- FUNCIONES PRINCIPALES DE LA BIBLIOTECA (Adaptadas) ---

# Función para encontrar un libro por título (Adaptada de search_product)
def find_book(book_title, library_data):
    """Busca un libro por título en el diccionario de la biblioteca."""
    search_title = book_title.strip()

    if search_title in library_data:
        return library_data[search_title]
    else:
        return None

# Función para añadir libros (Adaptada de add_product y combinada con lógica de validación y existencia)
def add_book(library_data):
    """Permite añadir un libro a la biblioteca con validaciones."""
    print("\n---------------------------------")
    print("➕ AGREGAR LIBRO")
    print("---------------------------------\n")

    title = get_valid_string("👉 Ingrese el TÍTULO del libro:\n")
    author = get_valid_string("👉 Ingrese el AUTOR del libro:\n")

    while True:
        genre_input = get_valid_string(f"👉 Ingrese el GÉNERO ({format_genre_list(VALID_GENRES)}):\n") # -> Llama a format_genre_list()
        if genre_input in VALID_GENRES:
            genre = genre_input
            break
        else:
            print(f"\n---------------------------------")
            print(f"⚠️ Género inválido. Los géneros permitidos son: {format_genre_list(VALID_GENRES)}") # -> Llama a format_genre_list()
            print(f"---------------------------------\n")

    total_copias = get_positive_integer("👉 Ingrese la CANTIDAD TOTAL de copias:\n")

    if title in library_data:
        library_data[title]["total_copias"] += total_copias
        library_data[title]["disponibles"] += total_copias
        print(f"\n✅ Libro '{title}' ya existía. Se agregaron {total_copias} copias más.")
    else:
        library_data[title] = {
            "autor": author,
            "total_copias": total_copias,
            "disponibles": total_copias,
            "genero": genre
        }
        print(f"\n✅ Libro '{title}' agregado al catálogo.")
    # if 'time' in globals(): time.sleep(1)


# Función para buscar y mostrar detalles de un libro (Adaptada de search_product para mostrar info)
def search_and_display_book(library_data):
    """Permite al usuario buscar un libro por título y muestra sus detalles."""
    print("\n---------------------------------")
    print("🔍 BUSCAR LIBRO")
    print("---------------------------------\n")

    title_to_find = get_valid_string("👉 Ingrese el TÍTULO del libro que desea buscar:\n")

    book_details = find_book(title_to_find, library_data)

    if book_details is not None:
        print("\n--- Detalles del Libro Encontrado ---")
        print(f"Título: {title_to_find}")
        print(f"Autor: {book_details['autor']}")
        print(f"Copias Totales: {book_details['total_copias']}")
        print(f"Copias Disponibles: {book_details['disponibles']}")
        print(f"Género: {book_details['genero']}")
        print("------------------------------------\n")
        # if 'time' in globals(): time.sleep(3)
    else:
        print("Book not found.\n") # Mensaje en inglés
        # if 'time' in globals(): time.sleep(2)


# Función para registrar un préstamo (Nueva funcionalidad, sigue el patrón)
def register_loan(library_data):
    """Registra el préstamo de un libro, disminuyendo las copias disponibles."""
    print("\n---------------------------------")
    print("📚 REGISTRAR PRÉSTAMO")
    print("---------------------------------\n")

    title_to_loan = get_valid_string("👉 Ingrese el TÍTULO del libro a prestar:\n")

    book_details = find_book(title_to_loan, library_data)

    if book_details is not None:
        if book_details["disponibles"] > 0:
            book_details["disponibles"] -= 1
            print(f"\n✅ Préstamo registrado para '{title_to_loan}'. Copias disponibles: {book_details['disponibles']}")
        else:
            print(f"\n⚠️ No hay copias disponibles de '{title_to_loan}' para prestar.")
        # if 'time' in globals(): time.sleep(2)
    else:
        print("Book not found.\n")
        # if 'time' in globals(): time.sleep(2)


# Función para registrar una devolución (Nueva funcionalidad, sigue el patrón)
def return_book(library_data):
    """Registra la devolución de un libro, aumentando las copias disponibles."""
    print("\n---------------------------------")
    print("🔙 REGISTRAR DEVOLUCIÓN")
    print("---------------------------------\n")

    title_to_return = get_valid_string("👉 Ingrese el TÍTULO del libro devuelto:\n")

    book_details = find_book(title_to_return, library_data)

    if book_details is not None:
        if book_details["disponibles"] < book_details["total_copias"]:
            book_details["disponibles"] += 1
            print(f"\n✅ Devolución registrada para '{title_to_return}'. Copias disponibles: {book_details['disponibles']}")
        else:
            print(f"\n⚠️ Todas las copias de '{title_to_return}' ya están en la biblioteca.")
        # if 'time' in globals(): time.sleep(2)
    else:
        print("Book not found.\n")
        # if 'time' in globals(): time.sleep(2)


# Función para eliminar un libro (Adaptada de delete_product)
def delete_book(library_data):
    """Elimina un libro del catálogo si no tiene copias prestadas."""
    print("\n---------------------------------")
    print("🗑️ ELIMINAR LIBRO")
    print("---------------------------------\n")

    title_to_delete = get_valid_string("👉 Ingrese el TÍTULO del libro a eliminar:\n")

    book_details = find_book(title_to_delete, library_data)

    if book_details is not None:
        if book_details["disponibles"] == book_details["total_copias"]:
            del library_data[title_to_delete]
            print(f"\n✅ Libro '{title_to_delete}' eliminado del catálogo.")
        else:
            prestadas = book_details['total_copias'] - book_details['disponibles']
            print(f"\n⚠️ No se puede eliminar '{title_to_delete}'. Hay {prestadas} copia(s) actualmente en préstamo.")
        # if 'time' in globals(): time.sleep(2)
    else:
        print("Book not found.\n")
        # if 'time' in globals(): time.sleep(2)


# Función para listar libros por género (Adaptada de show_products, pero con filtro)
def list_books_by_genre(library_data):
    """Muestra todos los libros disponibles de un género específico."""
    print("\n---------------------------------")
    print("📋 LISTAR LIBROS POR GÉNERO")
    print("---------------------------------\n")

    while True:
        genre_to_list = get_valid_string(f"👉 Ingrese el GÉNERO a listar ({format_genre_list(VALID_GENRES)}):\n") # -> Llama a format_genre_list()
        if genre_to_list in VALID_GENRES:
            genre = genre_to_list
            break
        else:
            print(f"\n---------------------------------")
            print(f"⚠️ Género inválido. Los géneros permitidos son: {format_genre_list(VALID_GENRES)}") # -> Llama a format_genre_list()
            print(f"---------------------------------\n")

    print(f"\n--- Libros en Género: {genre} ---")
    found_books = []
    for title, details in library_data.items():
        if details["genero"] == genre:
            found_books.append(title)

    if len(found_books) == 0:
        print(f"No se encontraron libros en el género '{genre}'.")
    else:
         # Implementación simple de Bubble Sort para ordenar los títulos encontrados
         n = len(found_books)
         for i in range(n):
             for j in range(0, n - i - 1):
                 if found_books[j] > found_books[j + 1]:
                     temp = found_books[j]
                     found_books[j] = found_books[j + 1]
                     found_books[j + 1] = temp

         for title in found_books:
             book_details = library_data[title]
             print(f"Título: {title}, Autor: {book_details['autor']}, Disponibles: {book_details['disponibles']}")

    print("---------------------------------\n")
    # if 'time' in globals(): time.sleep(3)


# Función para mostrar el resumen del inventario (Adaptada, similar a calcular valor total pero con otras métricas)
def show_inventory_summary(library_data):
    """Muestra un resumen del inventario de la biblioteca."""
    print("\n---------------------------------")
    print("📊 RESUMEN DE INVENTARIO")
    print("---------------------------------\n")

    total_distinct_books = len(library_data)
    total_all_copies = 0
    total_available_copies = 0

    for book_details in library_data.values():
        total_all_copies += book_details["total_copias"]
        total_available_copies += book_details["disponibles"]

    print("--- Estadísticas del Inventario ---")
    print(f"Total de títulos de libros distintos: {total_distinct_books}")
    print(f"Total de copias en la biblioteca: {total_all_copies}")
    print(f"Total de copias disponibles para préstamo: {total_available_copies}")
    print("---------------------------------\n")
    # if 'time' in globals(): time.sleep(3)


# --- INICIALIZACIÓN DE DATOS ---
# Añadir libros iniciales directamente al diccionario
initial_books_data = {
    "The Lord of the Rings": {"autor": "J.R.R. Tolkien", "total_copias": 5, "disponibles": 5, "genero": "Fiction"},
    "Sapiens: A Brief History of Humankind": {"autor": "Yuval Noah Harari", "total_copias": 3, "disponibles": 3, "genero": "NonFiction"},
    "Cosmos": {"autor": "Carl Sagan", "total_copias": 4, "disponibles": 4, "genero": "Science"},
    "Steve Jobs": {"autor": "Walter Isaacson", "total_copias": 2, "disponibles": 2, "genero": "Biography"},
    "The Cat in the Hat": {"autor": "Dr. Seuss", "total_copias": 10, "disponibles": 10, "genero": "Children"},
    "Dune": {"autor": "Frank Herbert", "total_copias": 3, "disponibles": 3, "genero": "Fiction"},
    "A Brief History of Time": {"autor": "Stephen Hawking", "total_copias": 3, "disponibles": 3, "genero": "Science"},
    "Becoming": {"autor": "Michelle Obama", "total_copias": 2, "disponibles": 2, "genero": "Biography"},
    "Green Eggs and Ham": {"autor": "Dr. Seuss", 8: "Children"}, # Error en key aquí, debería ser el género
    "1984": {"autor": "George Orwell", "total_copias": 4, "disponibles": 4, "genero": "Fiction"},
    "Brave New World": {"autor": "Aldous Huxley", "total_copias": 3, "disponibles": 3, "genero": "Fiction"}
}
# Corregir el error en la inicialización de "Green Eggs and Ham"
initial_books_data["Green Eggs and Ham"] = {"autor": "Dr. Seuss", "total_copias": 8, "disponibles": 8, "genero": "Children"}
# Asegurar que hay al menos 10 títulos distintos
if len(initial_books_data) < 10:
     print("⚠️ Advertencia: Menos de 10 libros iniciales definidos.")


# Copiar los datos iniciales al diccionario principal de la biblioteca
for title, details in initial_books_data.items():
    library[title] = details

# Añadir copias extra a un libro existente para probar esa funcionalidad
if "Cosmos" in library:
    library["Cosmos"]["total_copias"] += 2
    library["Cosmos"]["disponibles"] += 2


# --- FUNCIÓN PRINCIPAL (Adaptada del código de inventario) ---
def main():
    valid_genres_string = format_genre_list(VALID_GENRES) # Llama a format_genre_list() una vez al inicio

    while True:
        print("\n------------ MENÚ PRINCIPAL DE LA BIBLIOTECA ------------\n")
        print("1. ➕ Agregar Libro")
        print("2. 🔍 Buscar Libro por Título")
        print("3. 📚 Registrar Préstamo")
        print("4. 🔙 Registrar Devolución")
        print("5. 🗑️ Eliminar Libro del Catálogo")
        print("6. 📋 Listar Libros por Género")
        print("7. 📊 Mostrar Resumen de Inventario")
        print("8. 👋 SALIR\n")

        user_option = input("👉 Ingrese una OPCIÓN (1-8): \n").strip()

        if user_option == "1":
            add_book(library)
        elif user_option == "2":
            search_and_display_book(library)
        elif user_option == "3":
            register_loan(library)
        elif user_option == "4":
            return_book(library)
        elif user_option == "5":
            delete_book(library)
        elif user_option == "6":
            list_books_by_genre(library)
        elif user_option == "7":
            show_inventory_summary(library)
        elif user_option == "8":
            print("\n🚪 Gracias por usar el Sistema de Gestión de Biblioteca. ¡Adiós!\n")
            break
        else:
            print("\n⚠️ Error: Ingrese una opción válida del 1 al 8.\n")

# Llamar a la función principal al ejecutar el script
if __name__ == "__main__":
    main()