import time

# Diccionario de vuelos
flights = {
    "VS-436": {
        "from": "Barranquilla",
        "destination": "Buenos Aires",
        "seats": ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4"],
        "seats_booked": set(),
        "schedule": (6, 45)
    },
    "SF-641": {
        "from": "Bogotá",
        "destination": "Medellín",
        "seats": ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4"],
        "seats_booked": set(),
        "schedule": (11, 55),
    },
    "AL-881": {
        "from": "Santiago de Chile",
        "destination": "Buenos Aires",
        "seats": ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4"],
        "seats_booked": set(),
        "schedule": (13, 45),
    },
    "NM-729": {
        "from": "São Paulo",
        "destination": "Bogotá",
        "seats": ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4"],
        "seats_booked": set(),
        "schedule": (12, 25),
    },
    "ER-614": {
        "from": "Medellín",
        "destination": "Ciudad de México",
        "seats": ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4"],
        "seats_booked": set(),
        "schedule": (18, 15),
    },
}

def check_strings(print_text: str) -> str:
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
        total_seats = len(flight_key["seats"]) + seats_booked  # Total = disponibles + reservados

        occupation_percentage = (seats_booked / total_seats) * 100

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
    try:
        flights_ordered = sorted(
            flights.items(),
            key=lambda flights_value: flights_value[1]["schedule"]
        )

        with open("flight_report.txt", 'w', encoding='utf-8') as f:
            f.write("✈️ Flight Report ✈️\n")
            f.write("=" * 50 + "\n\n")
            
            for flight_code, info in flights_ordered:
                hour, minute = info["schedule"]

                
                total_seats = len(info["seats"]) + len(info["seats_booked"])
                occupation_percentage = (len(info["seats_booked"]) / total_seats * 100)
                
                f.write(f"✈️ Flight: {flight_code}\n")
                f.write(f"🌎 From: {info['from']}\n")
                f.write(f"🏙️ To: {info['destination']}\n")
                f.write(f"⏰ Schedule: {hour:02d}:{minute:02d}\n")
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
    attempt_max: int = 5
    current_attempt: int = 0

    # Intent-Limiting Main Loop
    while current_attempt < attempt_max:
        # Show menu
        print("\n------------ Flight Reservation System ------------\n")
        print("1. ✅ Book Flight")  
        print("2. 📊 Calculation of occupancy percentage per flight")
        print("3. 📄 Flight Report")
        print("4. 👋 EXIT\n") 
        
        # Request the option from the user
        user_option = input("👉 Type an OPTION from 1 to 4: \n").strip()
   
        # Option 1: Book flight
        if user_option == "1":            
            book_flight()
        # Option 2: Occupancy percentage
        elif user_option == "2":
            seats_unavailable_porcentage()
        # Option 3: Flight report
        elif user_option == "3":
            flight_report()
        # Option 4: Exit
        elif user_option == "4":
            print("\n🚪 THANK YOU FOR USING THE PROGRAM!\n")
            break
        # Invalid Option
        else:
            current_attempt += 1
            print("\n--------------------------------------------------")
            print("⚠️ Error: Enter a VALID OPTION from 1 to 4.‼️")
            print("--------------------------------------------------\n")

        # Check if the attempt limit has been reached
        if current_attempt == attempt_max:
            print("\n------------------------------")
            print("⚠️ Limit of ATTEMPTS reached")
            print("------------------------------\n")

if __name__ == "__main__":
    main()