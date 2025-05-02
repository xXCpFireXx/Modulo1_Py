# Definir e inicializar variables globales
intento_max: int = 5
intento_actual: int = 0
operacion_exitosa: bool = False

print("\n ----------------- BIENVENIDO -----------------\n")

# Bucle principal con límite de intentos
while intento_actual < intento_max and not operacion_exitosa:
    intento_actual += 1

    # Variable para la opción del menú
    opcion: str = ""

    # Mostrar el menú
    print("------------ MENÚ ------------\n")
    print("✅ 1. Determinar estado de aprobación")
    print("📊 2. Calcular promedio")
    print("📈 3. Contar calificaciones mayores que un valor")
    print("🔍 4. Contar calificaciones específicas")
    print("🚪 5. SALIR\n")
    
    # Solicitar la opción al usuario
    opcion = input("👉 Ingrese una OPCIÓN del 1 al 5: \n")
    
    # Reinicia para permitir más intentos
    operacion_exitosa = False
    
    # Opción 1: Determinar estado de aprobación
    if opcion == "1":
        
        print("\n✅ DETERMINAR ESTADO DE APROBACIÓN")

        # Variable para ingresar la calificación a evaluar
        entrada_calificacion: float = 0.0   
        
        try:
            entrada_calificacion = float(input("👉 Ingrese una CALIFICACIÓN del 0 al 100: \n"))
            
            if entrada_calificacion >= 0 and entrada_calificacion <= 100:
                
                if entrada_calificacion >= 70: #Condición minima para obtener APROBADO
                    print("\n✅ APROBADO!!")
                else:
                    print("\n❌ !!!REPROBADO!!!")

                operacion_exitosa = True  # Operación exitosa

            else:
                print("\n⚠️ ERROR: LA CALIFICACIÓN DEBE ESTAR ENTRE 0 Y 100.\n")
        except ValueError:
            print("\n⚠️ ERROR: INGRESE UN NÚMERO VALIDO!!.\n")
    
    # Opción 2: Calcular promedio
    elif opcion == "2":
        
        print("\n📊 CALCULAR PROMEDIO")
        
        lista_calificaciones: list[float] = [] # Lista para guardar las calificaciones
        entrada_calificaciones: str = ""     # Guardar las calificaciones ingresadas separada por coma
        numero_actual: str = ""              # Guarda el carácter que es diferente de ","
        
        entrada_calificaciones = input("👉 Ingrese los NÚMEROS separados por COMAS, por ejemplo (34,56,1,76): \n")
        
        for i in entrada_calificaciones:
            if i != ",":
                numero_actual += i
            else:
                valor: float = float(numero_actual) #Guarda en la variable valor el carácter convertido en float
                lista_calificaciones.append(valor)  #Agrega el valor a la lista calificaciones
                numero_actual = ""
                
        
        # Procesar el último número
        if numero_actual != "":
                valor: float = float(numero_actual)
                lista_calificaciones.append(valor)
                
        # Calcular
        suma_total: float = 0.0
        cantidad_numeros: int = 0
        promedio: float = 0.0

        for i in lista_calificaciones:
            suma_total += i      # Hace la suma de los números de la lista

        cantidad_numeros = len(lista_calificaciones) #Guarda la cantidad de datos que hay en la lista
        promedio = suma_total / cantidad_numeros     #Hace el promedio de las calificaciones

        #Mostrar resultados        
        print(f"\n📊 El PROMEDIO de las CALIFICACIONES {lista_calificaciones} es: {promedio:.2f}")            
        operacion_exitosa = True

    # Opción 3: Contar calificaciones mayores que un valor
    elif opcion == "3":
        
        print("\n📈 CONTAR CALIFICACIONES MAYORES QUE UN VALOR")
        lista_calificaciones: list[float] = [21,32,78,99,32,3,45,6,78,92,33,45,65,89,67,41] # Lista para guardar las calificaciones
        valor_para_comparar:float = 0.0 # Variable para ingresar el valor para comparar con las otras calificaciones
        contador_mayores:int = 0
        
        valor_para_comparar = float(input("👉 Ingrese una CALIFICACIÓN del 0 al 100: \n"))
            
        if valor_para_comparar >= 0 and valor_para_comparar <= 100:
            
            for i in lista_calificaciones:
                if i>valor_para_comparar:
                    contador_mayores += 1

            print(f"\n⭐ HAY {contador_mayores} CALIFICACIONES MAYORES QUE {valor_para_comparar} 🚀\n")           
            operacion_exitosa = True  # Operación exitosa
        else:
            print("\n⚠️ ERROR: LA CALIFICACIÓN DEBE ESTAR ENTRE 0 Y 100.\n")
    
    # Opción 4: Contar calificaciones específicas
    elif opcion == "4":
        
        print("\n🔍 CONTAR CALIFICACIONES ESPECÍFICAS\n")
        lista_calificaciones: list[float] = [] # Lista para guardar las calificaciones
        entrada_calificaciones: str = ""     # Guardar las calificaciones ingresadas separada por coma
        numero_actual: str = ""              # Guarda el carácter que es diferente de ","
        calificacion_especifica:float = 0.0  # Guarda la calificación especifica
        contador_calificaciones:int = 0
        
        entrada_calificaciones = input("👉 Ingrese los NÚMEROS separados por COMAS, por ejemplo (34,56,1,76): \n")
        
        for i in entrada_calificaciones:
            if i != ",":
                numero_actual += i
            else:
                valor: float = float(numero_actual)
                lista_calificaciones.append(valor)
                numero_actual = ""
                
        
        # Procesar el último número
        if numero_actual != "":
                valor: float = float(numero_actual)
                lista_calificaciones.append(valor)
                
        calificacion_especifica = float(input("\n👉 Ingrese una CALIFICACIÓN en ESPECÍFICO: \n"))
        
        if calificacion_especifica >= 0 and calificacion_especifica <= 100:
            
            #Recorre la lista para buscar cuantas veces esta la calificación especifica ingresada
            for i in lista_calificaciones:
                
                if i==calificacion_especifica:
                    contador_calificaciones += 1
                    
            print(f"\n⭐ APARECE LA CALIFICACIÓN {calificacion_especifica} EN LA LISTA {contador_calificaciones} VECES ⭐\n")   
            operacion_exitosa = True  # Operación exitosa
        else:
            print("\n⚠️ ERROR: LA CALIFICACIÓN DEBE ESTAR ENTRE 0 Y 100.\n")
                
    # Opción 5: Salir
    elif opcion == "5":
        print("\n🚪 ¡GRACIAS POR USAR EL PROGRAMA!")
        operacion_exitosa = True  # Salida exitosa
        break  # Salir del bucle
    
    # Opción inválida
    else:
        print("\n⚠️ Error: Ingrese una OPCIÓN VÁLIDA del 1 al 5.!!\n")

    # Verificar si se alcanzó el límite de intentos
    if intento_actual == intento_max and not operacion_exitosa:
        print("\n⚠️ Límite de INTENTOS alcanzado")
