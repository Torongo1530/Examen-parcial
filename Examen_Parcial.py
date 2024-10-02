#Menu principal con todos los programas

while True:

    menuPrincipal = input("""\nElija una opcion:
                          
    1. Calculadora simple
    2. Conversion de temperatura
    3. Area de un triangulo
    4. Descuento de compra
    5. Calculadora de IMC
    6. Calculadora de area de un circulo
    7. Conversion de moneda
    8. Calculadora de edad
    9. Descuento por cantidad
    10. Validador de edad
        \n""")

    #------Calculadora simple--------

    if menuPrincipal == "1":
        while True:
                
            num1 = int(input("\nIngrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))

            menuCalculadora = input("""\nElija una opcion: 
                                    
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Division
            5. Volver al menu principal
                \n""")

            if menuCalculadora == "1":
                print(f"\n{num1} mas {num2} es igual a: {num1 + num2}")
            elif menuCalculadora == "2":
                print(f"\n{num1} menos {num2} es igual a: {num1 - num2}")
            elif menuCalculadora == "3":
                print(f"\n{num1} multiplicado por {num2} es igual a: {num1 * num2}")
            elif menuCalculadora == "4":
                print(f"\n{num1} divido entre {num2} es igual a: {num1 / num2}")

            elif menuCalculadora == "5":
                break

            else:
                print("Opcion incorrecta, intente nuevamente\n")

    #----------Conversion de temperatura-------------
    
    elif menuPrincipal == "2":

        def grados_Fahrenheit(celsius):
            F = (celsius*(9/5)) + 32
            return F

        while True:

            menuConversionTemperatura = input("""Elija una opcion:
                                              
            1. Convertir de celsius a fahrenheit
            2. Volver al menu principal
            \n""")

            if menuConversionTemperatura == "1":
                grados_Celsius = float(input("Ingrese la temperatura en grados Celsius: "))
                print(f"\n{grados_Celsius} grados celsius es igual a {grados_Fahrenheit(grados_Celsius)} grados fahrenheit\n")
            
            elif menuConversionTemperatura == "2":
                break
            
            else:
                print("Opcion incorrecta, intente nuevamente\n")

    #--------------Area de un Triangulo-------------

    elif menuPrincipal == "3":

        def Area_triangulo(Base, Altura):
            Area = (Base * Altura) / 2
            return Area

        while True:

            menuAreaTriangulo = input("""Elija una opcion:
                                      
            1. Area de triangulo
            2. Volver al menu principal
            \n""")

            if menuAreaTriangulo == "1":
                Base_Triangulo = float(input("Ingrese la base del triangulo: "))
                Altura_Triangulo = float(input("Ingrese la altura del triangulo: "))
                print(f"\nEl area del triangulo es: {Area_triangulo(Base_Triangulo, Altura_Triangulo)}\n")

            elif menuAreaTriangulo == "2":
                break

            else:
                print("Opcion incorrecta, intente nuevamente\n")
    
    #------------Descuento por compra-------------

    elif menuPrincipal == "4":
        
        while True:

            menuDescuentoCompra = input("""Elija una opcion:
                                        
            1. Descuento de compra
            2. Volver al menu principal
            \n""")

            if menuDescuentoCompra == "1":

                precioOriginal = float(input("Ingrese el precio original del producto: "))
                porcentajeDescuento = int(input("Ingrese el porcentaje de descuento: "))
                porcentajeDescuento /= 100
                precioDescuento = precioOriginal - (precioOriginal*porcentajeDescuento)
                print(f"""\n
                Precio original:        {precioOriginal} pesos
                precio con descuento:   {precioDescuento} pesos
                \n""")

            elif menuDescuentoCompra == "2":
                break

            else:
                print("Opcion incorrecta, intente nuevamente\n")

    #------------Calculadora de IMC (Índice de Masa Corporal)-------------

    elif menuPrincipal == "5":

        while True:

            menuCalculadoraIMC = input("""Elija una opcion:
                                       
            1. Calculadora de Índice de Masa Corporal
            2. Volver al menu principal
            \n""")
            if menuCalculadoraIMC == "1":

                peso = float(input("Ingrese su peso en Kg: "))
                altura = float(input("Ingrese su altura en Metros: "))
                IMC = peso / (altura * altura)
                print(f"\nSu indice de masa corporal es {IMC} Kg/m2\n")

            elif menuCalculadoraIMC == "2":
                break

            else:
                print("Opcion incorrecta, intente nuevamente\n")
        
    #------------Calculadora de area de un circulo-------------  
    
    elif menuPrincipal == "6":

        while True:

            menuAreaCirculo = input("""Elija una opcion:
                                    
            1. Calculadora de area de un circulo
            2. Volver al menu principal
            \n""")

            if menuAreaCirculo == "1":

                radio = float(input("\nIngrese el radio del circulo: "))
                pi = 3.14159
                areaCirculo = pi*(radio*radio)
                print(f"\nEl area del circulo es {areaCirculo}\n")
            
            elif menuAreaCirculo == "2":
                break

            else:
                print("Opcion incorrecta, intente nuevamente\n")

    #------------Conversion de moneda------------- 

    elif menuPrincipal == "7":

        while True:

            menuConversionMoneda = input("""Elija una opcion:
                                         
            1. Conversion de moneda
            2. Volver al menu principal
            \n""")

            if menuConversionMoneda == "1":

                monedaOrigen = float(input("\nIngrese la cantidad de moneda de origen: "))
                tasaCambio = float(input("\nIngrese la tasa de cambio: "))
                monedaDestino = monedaOrigen *tasaCambio
                print(f"\nLa moneda de destino es igual a {monedaDestino}\n")
            
            elif menuConversionMoneda == "2":
                break

            else:
                print("Opcion incorrecta, intente nuevamente\n")

    #------------Calculadora de edad------------- 

    elif menuPrincipal == "8":

        while True:

            menuCalculadoraEdad = input("""Elija una opcion:
                                        
            1. Calculadora de edad
            2. Volver al menu principal
            \n""")

            if menuCalculadoraEdad == "1":
                
                from datetime import datetime

                while True:

                    fechaActual = int(datetime.now().strftime("%Y"))
                    anioNacimiento = int(input("\nIngrese su anio de nacimiento: "))
                    yaCumplioAnios = input(f"Ya cumplio anios en el {fechaActual}? y/n: ")

                    if yaCumplioAnios == "y" or yaCumplioAnios == "Y":
                        edad = fechaActual - anioNacimiento
                        print(f"\nUsted tiene {edad} anios de edad\n")
                        break

                    elif yaCumplioAnios == "n" or yaCumplioAnios == "N":
                        edad = fechaActual - anioNacimiento - 1
                        print(f"\nUsted tiene {edad} anios de edad\n")
                        break
                    
                    else:
                        print("Opcion incorrecta, intente nuevamente")
                        break

            elif menuCalculadoraEdad == "2":
                break

            else:
                print("Opcion incorrecta, intente nuevamente\n")

    #------------Descuento por cantidad------------- 

    elif menuPrincipal == "9":

        while True:

            menuDescuentoCantidad = input("""Elija una opcion:
                                          
            1. Descuento por cantidad
            2. Volver al menu principal
            \n""")

            if menuDescuentoCantidad == "1":

                precioArticulo = float(input("Ingrese el precio del articulo: "))
                CantidadArticulos = int(input("Ingrese la cantidad de unidades que desea comprar: "))
                total = (precioArticulo*CantidadArticulos)
                if CantidadArticulos >= 10:
                    total = total - (total*0.10)
                    print(f"\nEl total de la compra es {total} pesos\n")
                else:
                    print(f"\nEl total de la compra es {total} pesos\n")
            
            elif menuDescuentoCantidad == "2":
                break

            else:
                print("Opcion incorrecta, intente nuevamente")

    #------------Validador de edad------------- 

    elif menuPrincipal == "10":

        while True:

            menuValidadorEdad = input("""Elija una opcion:
                                      
            1. Validador de edad
            2. Volver al menu principal
            """)

            if menuValidadorEdad == "1":

                edad = int(input("Ingrese su edad: "))
                if edad >= 18 and edad <= 65:
                    print("\nSu edad cumple los requisitos para participar\n")
                else:
                    print("\nSu edad NO cumple los requisitos para participar\n")
            
            elif menuValidadorEdad == "2":
                break

            else:
                print("\nOpcion incorrecta, intente nuevamente\n")
    else:
        print("\nOpcion incorrecta, intente nuevamente\n")