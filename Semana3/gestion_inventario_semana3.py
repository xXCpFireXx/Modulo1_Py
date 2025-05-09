print("\n ----------------- WELCOME -----------------\n")

#Variable global
stock_products = {}

def check_strings(print_text):
     
    break_while = False

    while break_while is not True:
        name_product = input(print_text).strip().title()

        if not name_product:
            print("\n⚠️ Empty TEXT!")
            print("⚠️ Enter a VALID PRODUCT\n")
            print("---------------------------------")
        else:
            return name_product
        
def check_numbers(print_text,type_number):
     
    break_while = False

    while break_while is not True:
        number = input(print_text)

        try:
            number = type_number(number)
            if number > 0:
                return number
            else:
                print("⚠️ Enter a POSITIVE NUMBER\n")
                print("---------------------------------")
        except ValueError:
            print("⚠️ Enter a VALID NUMBER\n")
            print("---------------------------------")

def add_product(product_name :str, product_price :float, product_amount :int):
    stock_products[product_name] = (product_price, product_amount)

def search_product(product_name :str):
    
    if product_name in stock_products:
        product_searched = stock_products[product_name]
        return product_searched
    else:
        return None

def update_price(product_name :str, new_product_price :float, product_amount):
    stock_products[product_name] = (new_product_price, product_amount)
    print(f"✅ \nPrice of '{product_name}' updated to ${new_product_price:.2f}")

def delete_product(product_name :str):
    del stock_products[product_name]
    print(f"✅ \nProduct '{product_name}' DELETED")

def get_total_value():
    pass

def menu():
    attempt_max: int = 5
    current_attempt: int = 0

    # Bucle principal con límite de intentos
    while current_attempt < attempt_max:
        
        # Variable para la opción del menú
        user_option: str = ""

        # Mostrar el menú
        print("------------ MAIN MENU ------------\n")
        print("1. ➕ Add products")  
        print("2. 🔍 Search products")
        print("3. ✏️ Update prices")
        print("4. 🗑️ Delete products")
        print("5. 📊 Calculate the total value of inventory")
        print("6. 👋 EXIT\n") 
        
        # Solicitar la opción al usuario
        user_option = input("👉 Type an OPTION from 1 to 6: \n")
   
        # Option 1: Determinar estado de aprobación
        if user_option == "1":
            
            #local variables
            name_product_input:str = ""
            price_product_input:float = 0.0
            amount_product_input:int = 0

            print("\n---------------------------------")
            print("➕ ADD PRODUCTS")
            print("---------------------------------\n")

            # Llama a la función de validación para el nombre
            name_product_input = check_strings("👉 Type the PRODUCT NAME\n")
            
            # Llama a la función de validación para el precio
            price_product_input = check_numbers("👉 Type the PRODUCT PRICE\n",float)
            
            # Llama a la función de validación para la cantidad
            amount_product_input = check_numbers("👉 Type the PRODUCT AMOUNT\n",int)   
            
            add_product(name_product_input, price_product_input, amount_product_input)
            
        # Option 2: Calcular promedio
        elif user_option == "2":
            print("\n---------------------------------")
            print("🔍 SEARCH PRODUCTS")
            print("---------------------------------\n")

            name_product_input:str = ""
            
            name_product_input = check_strings("👉 Type the PRODUCT NAME that you WANT to FIND\n")
            product_searched_return = search_product(name_product_input)

            if product_searched_return is not None:
               price = product_searched_return[0]
               amount = product_searched_return[1]

               print("\n🔎 SEARCH RESULTS\n")
               print(f"✨PRODUCT: {name_product_input}")
               print(f"💲PRICE: {price}")
               print(f"📦AMOUNT: {amount}\n")
            else:
                print(f"⚠️ Product '{name_product_input}' does not EXIST.\n")

        # Option 3: Contar calificaciones mayores que un valor
        elif user_option == "3":
            
            print("\n---------------------------------")
            print("✏️ UPDATE PRICES")
            print("---------------------------------\n")
            
            name_product_input:str = ""
            price_product_input:float = 0.0
            
            name_product_input = check_strings("👉 Type the PRODUCT NAME that you WANT to UPDATE its price\n")
            product_searched_return = search_product(name_product_input)

            if product_searched_return is not None:
               price_product_input = check_numbers("👉 Enter the NEW PRICE\n",float)
               amount = product_searched_return[1]

               update_price(name_product_input,price_product_input,amount)
            else:
                print(f"⚠️ Product '{name_product_input}' does not EXIST.\n")
            
        
        # Option 4: Contar calificaciones específicas
        elif user_option == "4":

            print("\n---------------------------------")
            print("🗑️ DELETE PRODUCTS\n")
            print("---------------------------------\n")
            
            name_product_input:str = ""
            
            name_product_input = check_strings("👉 Type the PRODUCT NAME that you WANT to DELETE\n")
            product_searched_return = search_product(name_product_input)

            if product_searched_return is not None:
               delete_product(name_product_input)
            else:
                print(f"⚠️ Product '{name_product_input}' does not EXIST.\n")
            

        # Option 5: Contar calificaciones específicas
        elif user_option == "5":
            
            print("\n📊 CALCULAR EL VALOR TOTAL DEL INVENTARIO\n")
            get_total_value()

        # Option 6: Salir
        elif user_option == "6":
            print("\n🚪 ¡GRACIAS POR USAR EL PROGRAMA!")
            break  # Salir del bucle
        
        # Option inválida
        else:
            current_attempt += 1
            print("\n⚠️ Error: Ingrese una OPCIÓN VÁLIDA del 1 al 6.!!\n")

        # Verificar si se alcanzó el límite de intentos
        if current_attempt == attempt_max:
            print("\n⚠️ Límite de INTENTOS alcanzado")


def main():
    menu()

main()