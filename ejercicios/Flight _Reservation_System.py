import time

# Dictionary with the flights
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

# Function to validate strings 
# (receives by parameter, the text that is printed to the user)
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

# Function to display the list of available flights
def show_flights():
    
    print("-------------------------")
    print("✈️ FLIGHTS")
    print("-------------------------")

    hour = 0
    minute = 0
    
    for key, value in flights.items():  

        hour = value['schedule'][0]
        minute = value['schedule'][1]

        print(f"✨{key}")
        print(f"↗️ From: {value['from']}")
        print(f"↘️ To: {value['destination']}")
        print(f"⏳Schedule: {hour}:{minute}")
        print("-------------------------")

# Function to book the seats
def book_flight():
    #It allows you to reserve a seat on a flight."
    show_flights()
    
    print("\n-------------------------")
    print("✅ BOOK FLIGHT")
    print("-------------------------")
    
    # Show a list of flight codes
    print("✈️ FLIGHTS")
    print("----------")
    for id_flight in flights.keys():
        print(f"✨{id_flight}")

    # Allow to enter the flight code
    input_flight = check_strings("\n👉 Enter a FLIGHT\n")
    
    if input_flight in flights:
        flight_key = flights[input_flight]
        print("\n-------------------------")
        print("🪑SEATS")
        print(f"{flight_key['seats']}") # print the seats of the entered flight

        # Allows you to enter the seat you want
        input_seat = check_strings("\n👉 Enter a SEAT\n")        

        # Validations
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
            # Add the desired seat to the dictionary "seats_booked"
            flight_key["seats_booked"].add(input_seat)

            # Remove the desired seat from the dictionary "seats"
            flight_key["seats"].remove(input_seat)

            print("\n---------------------------------")
            print(f"SEAT '{input_seat}' BOOKED ✅")
            print("---------------------------------\n")
            time.sleep(1)
    else:    
        print("\n---------------------------------")
        print("⚠️  Flight does not EXIST.🚫")
        print("---------------------------------\n")
        time.sleep(1)

# Function to calculate the occupancy percentage per flight
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
        print(f"✨{id_flight}") # print the list of flight codes
    
    # Allow to enter the flight code
    input_flight = check_strings("\n👉 Enter a FLIGHT\n")
    
    if input_flight in flights:
        flight_key = flights[input_flight]

        # Save the number of data that is in "seats_booked"
        seats_booked = len(flight_key["seats_booked"])

        # Save the number of data that is in "seats"
        seats = len(flight_key["seats"])

        # The sum of the two lists is made to know the total number of seats.
        total_seats = seats + seats_booked

        # Operation to know the flight occupancy percentage
        occupation_percentage = (seats_booked / total_seats) * 100

        print("\n---------------------------------")
        print(f"✈️  FLIGHT: {input_flight}")
        print(f"📊 OCCUPANCY PERCENTAGE: {occupation_percentage:.1f}%")
        print("---------------------------------\n")
        time.sleep(1)
    else:    
        print("\n---------------------------------")
        print("⚠️  Flight does not EXIST.🚫")
        print("---------------------------------\n")
        time.sleep(1)

# Function to generate the report in .txt
def flight_report():
    try:
        flights_ordered = {}

        # Saves the flights sorted by schedule
        flights_ordered = sorted(
            flights.items(),
            key=lambda flights_value: flights_value[1]["schedule"]
        )

        report_file_name = "flight_report.txt"

        """ A function that allows working with files, in this case "w" 
        allows writing to a file and if the file does not exist, it is created automatically. """
        with open(report_file_name, 'w', encoding='utf-8') as txt_flights:
            txt_flights.write("✈️ Flight Report ✈️\n")
            txt_flights.write("=" * 40 + "\n\n")
            
            for flight_code, dicts_value_flights in flights_ordered:

                hour = dicts_value_flights["schedule"][0] # Save hours
                minute = dicts_value_flights["schedule"][1] # Save minutes

                # Save the number of data that is in "seats_booked"
                seats_booked = len(dicts_value_flights["seats_booked"])

                # Save the number of data that is in "seats"
                seats = len(dicts_value_flights["seats"])

                # The sum of the two lists is made to know the total number of seats.
                total_seats = seats + seats_booked

                # Operation to know the flight occupancy percentage
                occupation_percentage = (seats_booked / total_seats) * 100
                
                txt_flights.write(f"✈️ Flight: {flight_code}\n")
                txt_flights.write("-----------------------------\n")
                txt_flights.write(f"🌎 From: {dicts_value_flights['from']}\n")
                txt_flights.write(f"🏙️ To: {dicts_value_flights['destination']}\n")
                txt_flights.write(f"⏰ Schedule: {hour:02d}:{minute:02d}\n")
                txt_flights.write(f"🪑 Available Seats: {seats}\n")
                txt_flights.write(f"✅ Booked Seats: {seats_booked}\n")
                txt_flights.write(f"📊 Occupancy Percentage: {occupation_percentage:.1f}%\n")
                txt_flights.write("-" * 30 + "\n")

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