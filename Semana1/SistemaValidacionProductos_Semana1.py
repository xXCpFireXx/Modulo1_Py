print("\n------- BIENVENIDO CLIENTE ------")

nombreProducto = input("\nIngresa el NOMBRE del producto: \n")
nombreProducto = nombreProducto.upper() #Convierte el NOMBRE DEL PRODUCTO a MAYUSCULAS

# Bucle While que valida el dato ingresado para el precio del producto.
while True:
    try:
        precioUnidad = float(input("\n\nIngresa el PRECIO del producto: \n"))

        if precioUnidad < 0:
            print("\nEL PRECIO DEBE SER UN VALOR POSITIVO!! \n")
            print("VUELVA a INGRESAR el PRECIO del producto")
        else:
            break
    except:
        print("Dato INVALIDO, INTENTALO OTRA VEZ!! \n")

# Bucle While que valida el dato ingresado para la cantidad de productos.
while True:
    try:
        cantidadProducto = int(input("\n\nINGRESA la CANTIDAD de productos: \n"))

        if cantidadProducto < 0:
            print("\nLA CANTIDAD DEBE SER UN VALOR POSITIVO!! \n")
            print("VUELVA a INGRESAR la CANTIDAD del producto")
        else:
            break
    except:
        print("Dato INVALIDO, INTENTALO OTRA VEZ!! \n")

# Bucle While que valida el dato ingresado para los descuentos de productos.
while True:
    try:
        opcionDescuento = input("\n\n¿Este producto tiene un DESCUENTO?\nIngresa S ó N\n")

        if opcionDescuento == "S" or opcionDescuento == "s":
            
            porcentajeDescuento = int(input("\nIngresa el PORCENTAJE del DESCUENTO: \n"))

            if porcentajeDescuento < 0 or porcentajeDescuento > 100:
                print("\nEL PORCENTAJE DEBE SER UN VALOR ENTRE 0 A 100!! \n")
                print("VUELVA a INGRESAR el PORCENTAJE del producto")
            else:
                costoSinDescuento = precioUnidad * cantidadProducto
                costoTotal = costoSinDescuento * (porcentajeDescuento / 100)
                costoTotal = costoSinDescuento - costoTotal   

            break
        else:            
            porcentajeDescuento = 0
            costoTotal = precioUnidad * cantidadProducto
            break
    except: 
        print("Dato INVALIDO, INTENTALO OTRA VEZ!! \n")

#Print que muestra de forma formateada el nombre del Producto, costoTotal y porcentaje de Descuento
print("\nPRODUCTO:{} COSTO TOTAL:${:.2f} DESCUENTO:{}%\n".format(nombreProducto, costoTotal, porcentajeDescuento))
