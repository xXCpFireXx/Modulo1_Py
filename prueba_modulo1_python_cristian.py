import time # import the "Time" module

# Global variable
stock_products = {} # Dictionary that stores all products

# ------------------------------- COMPLEMENTARY FUNCTIONS -------------------------------
# Function to validate strings 
# (receives by parameter, the text that is printed to the user)
def check_strings(print_text):
     
    break_while = False

    while break_while is not True:
        name_product = input(print_text).strip().title() # it asks the user for the string, removes the spaces and finally saves it in the variable

        if name_product == "": # This does the validation if it is empty
            print("\n---------------------------------")
            print("⚠️  Empty TEXT‼️")
            print("⚠️  Enter a VALID PRODUCT‼️")
            print("---------------------------------\n")
        else:
            return name_product

# function to validate that the numbers are positive 
# (receives by parameter the text to be printed to the user and the type of numerical data)
def check_numbers(print_text,type_number):
     
    break_while = False

    while break_while is not True:
        number = input(print_text) #It asks the user for the value and saves it in the "number" variable

        try:
            number = type_number(number) #converts the value to the type of data that was passed by parameter

            if number > 0: # this does the validation to see if it is positive
                return number
            else:
                print("\n---------------------------------")
                print("⚠️  Enter a POSITIVE NUMBER‼️")
                print("---------------------------------\n")
        except ValueError:
            print("\n---------------------------------")
            print("⚠️  Enter a VALID NUMBER‼️")
            print("---------------------------------\n")

# Function to display the list of available products
def show_products():

    # Define and initialize the variables
    name_product:str = ""

    print("---------------------------------")
    print("📋 LIST OF PRODUCTS")
    print("---------------------------------")
    
    for product_key in stock_products.keys(): # Iterate the dictionary 
        name_product = product_key # Save the product name              
        print(f"✨ {name_product}")
    
    print("---------------------------------\n")

# function to load the first products
def preload_products():

    # Define and initialize the variables
    name_product:str = ""
    price:float = 0.0
    amount:int = 0
    count_first_products = 0

    preloads_products = {
        "Huevo": (600,56),
        "Libra de Sal": (1000,36),
        "libra Frijoles": (3500.95,8),
        "Detergente 1kl": (5099.99,15),
        "Queso 1lb": (4500,10)
    }

    for product_key, product_value in preloads_products.items(): # Iterate the dictionary 
        name_product = product_key.strip().title() # Save the product name
        price = float(product_value[0]) # Save the price of the product
        amount = product_value[1] # Save the amount of the product

        if name_product == "": # This does the validation if it is empty
            print("\n---------------------------------")
            print("⚠️ Empty TEXT!")
            print("⚠️ Enter a VALID PRODUCT‼️")
            print("---------------------------------\n")

        elif price < 0: # this does the validation to see if it is negative price         
            print("---------------------------------")
            print("⚠️ NEGATIVE NUMBER in the PRICE‼️")
            print(f"⚠️ Unable to add the product {name_product}")
            print("---------------------------------")

        elif amount < 0: # this does the validation to see if it is negative amount
            print("---------------------------------")
            print("⚠️ NEGATIVE NUMBER in the AMOUNT‼️")
            print(f"⚠️ Unable to add the product {name_product}")
            print("---------------------------------")

        else:
            stock_products[name_product] = (price, amount) # Save the first products in the dictionary
            count_first_products = len(stock_products) # Save theamount of the entered products
    
    # A final verification is made to see if there are 5 preloaded products.
    if count_first_products < 5:
        print("---------------------------------")
        print("⚠️ It is not possible to add the first 5 products")
        print("---------------------------------")
        return False # if there are no 5 preloaded products, it returns 'False'

# -------------------------------- MAIN FUNCTIONS ----------------------------------------
# Function to add products to the dictionary
def add_product(product_name :str, product_price :float, product_amount :int):
    stock_products[product_name] = (product_price, product_amount) # Save the name of the product in the KEY and save the price and amount in a tuple in the VALUE
    
    # Prints message that the process is ready
    print("\n---------------------------------")
    print(f"✅ Product: '{product_name}' ADDED")
    print("---------------------------------\n")
    time.sleep(1)

# Function to search for the name of the submitted product by parameter within the dictionary
def search_product(product_name :str):
    
    if product_name in stock_products: # Check with the name of the product entered in the dictionary
        product_searched = stock_products[product_name] # it saves in the variable the value which is the tuple
        return product_searched
    else:
        return None

# Function to change the price of the entered product
def update_price(product_name :str, new_product_price :float, product_amount):

    # First of all, a tuple will not be modified, therefore, it will overwrite the data with the new price, 
    # but maintaining the previous data of the product    
    stock_products[product_name] = (new_product_price, product_amount)

    # Prints message that the process is ready
    print("\n---------------------------------")
    print(f"✅ Price of '{product_name}' updated to ${new_product_price:.2f}")
    print("---------------------------------\n")
    time.sleep(1)

# Function to remove a product from the dictionary
def delete_product(product_name :str):
    del stock_products[product_name] # Using "Del" removes the item from the dictionary with the name of the product entered by the user
    
    # Prints message that the process is ready
    print("\n---------------------------------")
    print(f"✅ Product '{product_name}' DELETED")
    print("---------------------------------\n")
    time.sleep(1)

# Main Function
# Function containing the entire interactive menu
def main():
    attempt_max: int = 5
    current_attempt: int = 0

    # Intent-Limiting Main Loop
    while current_attempt < attempt_max:
        
        # Variable for Menu Option
        user_option: str = ""

        # Show menu
        print("\n------------ INVENTORY MANAGEMENT MENU ------------\n")
        print("1. ➕ Add products")  
        print("2. 🔍 Search products")
        print("3. ✏️  Update prices")
        print("4. 🗑️  Delete products")
        print("5. 📊 Calculate the total value of inventory")
        print("6. 👋 EXIT\n") 
        
        # Request the option from the user
        user_option = input("👉 Type an OPTION from 1 to 6: \n").strip()
   
        # Option 1: Add new products
        if user_option == "1":
            
            #local variables
            name_product_input:str = ""
            price_product_input:float = 0.0
            amount_product_input:int = 0

            print("\n---------------------------------")
            print("➕ ADD PRODUCTS")
            print("---------------------------------\n")

            # Call the validation function for the name
            name_product_input = check_strings("👉 Type the PRODUCT NAME\n")
            
            # Call the validation function for the price
            price_product_input = check_numbers("👉 Type the PRODUCT PRICE\n",float)
            
            # Call the validation function for the amount
            amount_product_input = check_numbers("👉 Type the PRODUCT AMOUNT\n",int)   
            
            # Call add products function 
            add_product(name_product_input, price_product_input, amount_product_input)
            
        # Option 2: Search products
        elif user_option == "2":
            print("\n---------------------------------")
            print("🔍 SEARCH PRODUCTS")
            print("---------------------------------")

            show_products() # Call the "show_products" function to display all the products in the inventory

            # local variable
            name_product_input:str = ""
            
            # Using the "check_strings" function, it validates and then saves the returned value.
            name_product_input = check_strings("👉 Type the PRODUCT NAME that you WANT to FIND\n")

            # Using the "search_product" function, first verify the existence of the product and the tuple or "None" returns.
            product_searched_return = search_product(name_product_input) 

            if product_searched_return is not None:
               price = product_searched_return[0] # Save the PRICE of the product which is in index 0 of the tuple
               amount = product_searched_return[1] # Save the AMOUNT of the product which is in index 1 of the tuple

               # Prints all the information on the product
               print("\n---------------------------------")
               print("🔎 SEARCH RESULTS\n")
               print(f"✨PRODUCT: {name_product_input}")
               print(f"💲PRICE: {price}")
               print(f"📦AMOUNT: {amount}")
               print("---------------------------------\n")

               time.sleep(3) # Using the "Time" module with the "Sleep" function, a wait is made so that the result is better visualized
            else:
                print("\n---------------------------------")
                print(f"⚠️  Product '{name_product_input}' does not EXIST.🚫") # if the "search_product" function returns "None", it displays this message
                print("---------------------------------\n") 

        # Option 3: Update product prices
        elif user_option == "3":
            
            print("\n---------------------------------")
            print("✏️ UPDATE PRICES")
            print("---------------------------------")
            
            # local variables
            name_product_input:str = ""
            price_product_input:float = 0.0
            
            show_products() # Call the "show_products" function to display all the products in the inventory

            name_product_input = check_strings("👉 Type the PRODUCT NAME that you WANT to UPDATE its price\n")
            product_searched_return = search_product(name_product_input)

            if product_searched_return is not None:
               price_product_input = check_numbers("👉 Enter the NEW PRICE\n",float)
               amount = product_searched_return[1] #Save the quantity of the product

               # Call the "update_price" function to 
               update_price(name_product_input,price_product_input,amount)
            else:
                print("\n---------------------------------")
                print(f"⚠️  Product '{name_product_input}' does not EXIST.🚫")
                print("---------------------------------\n")
            
        
        # Option 4: Delete products
        elif user_option == "4":

            print("\n---------------------------------")
            print("🗑️ DELETE PRODUCTS")
            print("---------------------------------\n")
            
            # local variable
            name_product_input:str = ""

            show_products() # Call the "show_products" function to display all the products in the inventory
            
            name_product_input = check_strings("👉 Type the PRODUCT NAME that you WANT to DELETE\n")
            product_searched_return = search_product(name_product_input)

            if product_searched_return is not None:
               
                # it asks the user for confirmation to delete the product
                choosing = input(f"\n⁉️  Do you want to delete '{name_product_input}'? 👉 (Y/N)\n").strip().capitalize()
                             
                if choosing == "Y": # verify the USER'S ENTERED selection (Y/N)
                    delete_product(name_product_input)
                else:
                    print("\n---------------------------------")
                    print(f"🚫 Product '{name_product_input}' not DELETED")
                    print("---------------------------------\n")
                    time.sleep(1)
            else:
                print("\n---------------------------------")
                print(f"⚠️  Product '{name_product_input}' does not EXIST.🚫")
                print("---------------------------------\n")

        # Option 5: Calculate the total value of inventory
        elif user_option == "5":

            print("\n---------------------------------")
            print("📊 CALCULATE THE TOTAL VALUE OF INVENTORY")
            print("---------------------------------\n")
            
            # local variables
            total_sum = 0 # Variable to save the sum
            price:float = 0.0
            amount:int = 0

            for product_value in stock_products.values():
                price = product_value[0] # Save the price
                amount = product_value[1]  # Save the amount

                value_total = lambda price, amount: price * amount # lambda function where the price is multiplied by the quantity 

                total_sum += value_total(price,amount) # variable that in each iteration stores the result returned by the lambda function
            
            print("⏳ Calculating...")
            time.sleep(1)

            print("\n---------------------------------")
            print(f"The total INVENTORY CALCULATION is: 💲{total_sum:.2f}") # Displays the total of the calculation
            print("---------------------------------\n")
            
            time.sleep(3)
        # Option 6: Exit
        elif user_option == "6":
            print("\n🚪 THANK YOU FOR USING THE PROGRAM!\n")
            break  # Exit of the loop
        
        # Invalid Option
        else:
            current_attempt += 1
            print("\n--------------------------------------------------")
            print("⚠️ Error: Enter a VALID OPTION from 1 to 6.‼️")
            print("--------------------------------------------------\n")

        # Check if the attempt limit has been reached
        if current_attempt == attempt_max:
            print("\n------------------------------")
            print("⚠️ Limit of ATTEMPTS reached")
            print("------------------------------\n")

# ------------------------------------------------------------------------------------------------------
# Save what the function 'preload_products' returns
start_program = preload_products() 

if start_program is not False:
    # If it did not return False, the program runs normally.
    main() # Call MAIN FUNCTION
else:
    # If False is returned, show a message and do not call the 'main' function.
    print("---------------------------------")
    print("⚠️ It is not possible START the PROGRAM")
    print("---------------------------------")
    