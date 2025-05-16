import time
import random
import string

# Diccionario de vuelos inicializado vacío
flights = {}

def generate_flights() -> str:
    """Genera un código de vuelo aleatorio en formato XX-999."""
    letters = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
    digits = str(random.randint(100, 999))
    return letters + "-" + digits

def generate_domestic_cities() -> str:
    """Devuelve una ciudad nacional aleatoria."""
    domestic_cities = ["Bogotá", "Medellín", "Cali", "Cartagena", "Barranquilla"]
    return random.choice(domestic_cities)

def generate_international_cities() -> str:
    """Devuelve una ciudad internacional aleatoria."""
    international_cities = [
        "Ciudad de Panamá",
        "Ciudad de México",
        "Lima",
        "São Paulo",
        "Buenos Aires",
        "Santiago de Chile",
    ]
    return random.choice(international_cities)

def initialize_flights(min_flights: int = 3, max_flights: int = 5):
    """Genera entre min_flights y max_flights vuelos aleatorios."""
    num_flights = random.randint(min_flights, max_flights)
    default_seats = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4"]

    for _ in range(num_flights):
        # Generar código de vuelo único
        while True:
            flight_code = generate_flights()
            if flight_code not in flights:
                break

        # Generar origen y destino (mezclar nacional e internacional)
        if random.choice([True, False]):  # 50% de probabilidad para cada tipo
            origin = generate_domestic_cities()
            destination = generate_international_cities()
        else:
            origin = generate_international_cities()
            destination = generate_domestic_cities()

        # Generar horario aleatorio
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)

        # Añadir vuelo al diccionario
        flights[flight_code] = {
            "from": origin,
            "destination": destination,
            "seats": default_seats.copy(),  # Copia para evitar modificar la lista original
            "seats_booked": set(),
            "schedule": (hour, minute)
        }

def check_strings(print_text: str) -> str:
    """Valida que el input del usuario no esté vacío y lo devuelve en mayúsculas."""
    break_while = False
    while not break_while:
        name = input(print_text).strip().upper()
        if name == "":
            print("\n---------------------------------")
            print("⚠️  Empty TEXT‼️")
            print("⚠️  Enter a VALID FLIGHT‼️")
            print("---------------------------------\n")
        else:
            return name

def show_flights():
    """Muestra todos los vuelos disponibles."""
    print("-------------------------")
    print("✈️ FLIGHTS")
    print("-------------------------")
    
    for key, value in flights.items():        
        print(f"✨{key}")
        print(f"↗️ From: {value['from']}")
        print(f"↘️ To: {value['destination']}")
        print(f"⏳Schedule: {value['schedule'][0]:02d}:{value['schedule'][1]:02d}")
        print("-------------------------")

def book_flight():
    """Permite reservar un asiento en un vuelo."""
    show_flights()
    
    print("\n-------------------------")
    print("✅ BOOK FLIGHT")
    print("-------------------------")
    
    print("✈️ FLIGHTS")
    print("----------")
    for id_flight in flights.keys():
        print(f"✨{id_flight}")

    input_flight = check_strings("\n👉 Enter a FLIGHT\n")
    
    if input_flight in flights:
        flight_key = flights[input_flight]
        print("\n-------------------------")
        print("🪑SEATS")
        print(f"{flight_key['seats']}")

        input_seat = check_strings("\n👉 Enter a SEAT\n")        

        if input_seat not in flight_key["seats"]:
            print("\n---------------------------------")
            print(f"Seat '{input_seat}' not available ❌")
            print("---------------------------------\n")
            time.sleep(1)
        elif input_seat in flight_key["seats_booked"]:
            print("\n---------------------------------")
            print(f"Seat '{input_seat}' already booked ❌")
            print("---------------------------------\n")
            time.sleep(1)
        else:
            flight_key["seats_booked"].add(input_seat)
            flight_key["seats"].remove(input_seat)
            print("\n---------------------------------")
            print(f"SEAT '{input_seat}' BOOKED ✅")
            print("---------------------------------\n")
            time.sleep(1)
    else:    
        print("\n---------------------------------")
        print(f"⚠️  Flight does not EXIST.🚫")
        print("---------------------------------\n")
        time.sleep(1)

def seats_unavailable_porcentage():
    """Calcula el porcentaje de ocupación de un vuelo específico."""
    total_seats = 0
    seats_booked = 0
    occupation_percentage = 0

    print("\n--------------------------------------------------")
    print("📊 CALCULATION OF OCCUPANCY PERCENTAGE PER FLIGHT")
    print("--------------------------------------------------\n")

    print("✈️ FLIGHTS")
    print("----------")
    for id_flight in flights.keys():
        print(f"✨{id_flight}")
    
    input_flight = check_strings("\n👉 Enter a FLIGHT\n")
    
    if input_flight in flights:
        flight_key = flights[input_flight]
        seats_booked = len(flight_key["seats_booked"])
        total_seats = len(flight_key["seats"]) + seats_booked

        occupation_percentage = (seats_booked / total_seats * 100) if total_seats > 0 else 0

        print("\n---------------------------------")
        print(f"✈️  FLIGHT: {input_flight}")
        print(f"📊 OCCUPANCY PERCENTAGE: {occupation_percentage:.1f}%")
        print("---------------------------------\n")
        time.sleep(1)
    else:    
        print("\n---------------------------------")
        print(f"⚠️  Flight does not EXIST.🚫")
        print("---------------------------------\n")
        time.sleep(1)

def flight_report():
    """Genera un reporte de todos los vuelos ordenados por horario en un archivo de texto con emojis."""
    try:
        def get_schedule(flight):
            """Extrae el campo schedule del diccionario del vuelo."""
            return flight[1]["schedule"]

        flights_ordered = sorted(
            flights.items(),
            key=get_schedule
        )

        with open("flight_report.txt", 'w', encoding='utf-8') as f:
            f.write("✈️ Flight Report ✈️\n")
            f.write("=" * 50 + "\n\n")
            
            for flight_code, info in flights_ordered:
                hora, minuto = info["schedule"]
                total_seats = len(info["seats"]) + len(info["seats_booked"])
                occupation_percentage = (len(info["seats_booked"]) / total_seats * 100) if total_seats > 0 else 0
                
                f.write(f"✈️ Flight: {flight_code}\n")
                f.write(f"🌎 From: {info['from']}\n")
                f.write(f"🏙️ To: {info['destination']}\n")
                f.write(f"⏰ Schedule: {hora:02d}:{minuto:02d}\n")
                f.write(f"🪑 Available Seats: {len(info['seats'])}\n")
                f.write(f"✅ Booked Seats: {len(info['seats_booked'])}\n")
                f.write(f"📊 Occupancy Percentage: {occupation_percentage:.1f}%\n")
                f.write(f"🔽 Seats Available: {', '.join(info['seats'])}\n")
                f.write(f"🔼 Seats Booked: {', '.join(info['seats_booked']) if info['seats_booked'] else 'None'}\n")
                f.write("-" * 50 + "\n")

        print("\n---------------------------------")
        print("📄 Report generated in 'flight_report.txt' ✅")
        print("---------------------------------\n")
        time.sleep(1)

    except Exception as e:
        print("\n---------------------------------")
        print(f"⚠️ Error generating report: {e} ‼️")
        print("---------------------------------\n")
        time.sleep(1)

def main():
    # Generar vuelos aleatorios al inicio
    initialize_flights(min_flights=3, max_flights=5)
    print("\n---------------------------------")
    print(f"✈️ Generated {len(flights)} flights")
    show_flights()
    print("---------------------------------\n")
    time.sleep(1)

    attempt_max: int = 5
    current_attempt: int = 0

    while current_attempt < attempt_max:
        print("\n------------ Flight Reservation System ------------\n")
        print("1. ✅ Book Flight")  
        print("2. 📊 Calculation of occupancy percentage per flight")
        print("3. 📄 Flight Report")
        print("4. 👋 EXIT\n") 
        
        user_option = input("👉 Type an OPTION from 1 to 4: \n").strip()
   
        if user_option == "1":            
            book_flight()
        elif user_option == "2":
            seats_unavailable_porcentage()
        elif user_option == "3":
            flight_report()
        elif user_option == "4":
            print("\n🚪 THANK YOU FOR USING THE PROGRAM!\n")
            break
        else:
            current_attempt += 1
            print("\n--------------------------------------------------")
            print("⚠️ Error: Enter a VALID OPTION from 1 to 4.‼️")
            print("--------------------------------------------------\n")

        if current_attempt == attempt_max:
            print("\n------------------------------")
            print("⚠️ Limit of ATTEMPTS reached")
            print("------------------------------\n")

if __name__ == "__main__":
    main()



""" def generate_flights():
    id_flight: str = ""
    letters: str = ""
    digits: str = ""

    letters = random.choice(string.ascii_uppercase) + random.choice(
        string.ascii_uppercase
    )
    digits = str(random.randint(100, 999))
    id_flight = letters + "-" + digits
    return id_flight


print(generate_flights())


def generate_domestic_cities():
    domestic_cities: str = ["Bogotá", "Medellín", "Cali", "Cartagena", "Barranquilla"]
    return random.choice(domestic_cities)


def generate_international_cities():
    international_cities: str = [
        "Ciudad de Panamá",
        "Ciudad de México",
        "Lima",
        "São Paulo",
        "Buenos Aires",
        "Santiago de Chile",
    ]
    return random.choice(international_cities)

 """

