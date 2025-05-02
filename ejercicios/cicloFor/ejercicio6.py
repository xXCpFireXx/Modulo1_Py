opcion = 0
saldo = 20459.98

while opcion!=4:
    

    print("\nBIENVENIDO")
    print("1. Ver Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Salir del Programa")

    opcion = int(input("\nSeleccione una de las OPCIONES: \n"))

    if opcion ==1:
        print(f"TU SALDO ES: ${saldo}\n")

    elif opcion ==2:
        depositar = 0.0
        print(f"\nTienes un SALDO de ${saldo}")
        depositar = float(input("INGRESA la CANTIDAD A DEPOSITAR: \n"))
        saldo += depositar
        print(f"Nuevo SALDO es ${saldo}\n")

    elif opcion == 3:
        retirar = 0.0
        print(f"\nTienes un SALDO de ${saldo}")
        retirar = float(input("INGRESA la CANTIDAD A RETIRAR: \n"))
        
        if retirar<=saldo:
            saldo = saldo - retirar
            print(f"Nuevo SALDO es ${saldo}\n")
        else:
            print("No puedes INGRESAR una CANTIDAD menor a TU SALDO")
    elif opcion == 4:
        print("GRACIAS POR USAR")
    else:
        print("OPCION INCORRECTA!!")
    
        
        