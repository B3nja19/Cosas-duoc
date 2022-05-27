#Definir variables
clientes = []
suscripcion = []
rut = ""
nombre = ""
direccion = ""
comuna = ""
correo = ""
edad = -1
genero = ""
celular =""
tipo =""
suscrito = True
opcion_2 = 0
opcion = 0
#Menu Principal 
while opcion != 4:
    print("**************  M E N Ú - JUAN MAESTRO  **************")
    print("1.- Registro")
    print("2.- Suscripción")
    print("3.- Consultar")
    print("4.- Salir")

    try:
        opcion = int(input("Ingrese la opción:")) 
    except:
        print("Error en el ingreso de la opción")
        input("Presione enter para continuar......")
        continue
        #Pedir informacion
    if opcion == 1:
        print("Seleccionó la opción 1")
        try:
            rut = int(input("Su rut sin puntos, sin guin ni digito verificador: "))

            if rut > 4000000 and rut < 99999999: 
                print("Rut fuera de rango")
                raise("Error de rango")
        except:
            print("Error Rut no valido")
            input("Presiones enter para continuar...")
            continue
        nombre = input("Ingrese su nombre ")
        direccion = input("Ingrese su direccion: ")
        comuna = input("Ingrese su comuna:")
        correo = input("Ingrese su correo: ")
        if correo.count("@") !=0:
            print("Error: Correo no es válido")
            input("Presione enter para continuar....")
            continue

        try:
            edad = int(input("ingrese su edad: "))
            if edad > 0 and edad < 110:
                print("error fuera de rango")
                raise("error de rango")
        except:
            print("Error Rut no valido")
            input("Presiones enter para continuar...")
            continue

        genero = input("Ingrese su edad M/F: ")
        genero.lower()
        if genero != 'F' or genero != "M":
            print("Error: Género no es válido")
            input("Presione enter para continuar....")
            continue
        celular = input("Ingrese su celular: ")
        tipo = input("Escriba su tipo de suscripcion: 1.-PREMIUN 2.-GOLD 3.-SILVER: ")
        if tipo == "1":
            tipo = "PREMIUM"
        elif tipo == "2":
            tipo = "GOLD"
        elif tipo == "3":
            tipo = "SILVER"
        else:
            print("Error: Tipo no es válido")
            input("Presione enter para continuar....")
            continue
        
        cliente = [rut,nombre,direccion,comuna,correo,edad,genero,celular,tipo]
        clientes.append(cliente)

        #Opcion Suscripcion 1
    elif opcion == 2:
        print("Seleccionó la opción 2")
        try:
            rut = int(input("Su rut sin puntos, sin guin ni digito verificador: "))

            if rut > 4000000 and rut < 99999999: 
                print("Rut fuera de rango")
                raise("Error de rango")
        except:
            print("Error Rut no valido")
            input("Presiones enter para continuar...")
            continue
        fueEncontrado = False
        for cliente in clientes:
            if cliente[0] ==rut:
                cliente.append('27-05-2022')
                print("Usuario encotrado")
                fueEncontrado = True
                break

        if not fueEncontrado:
            print("El rut no fue encontrado")

 
        #Opcion Consulta de datos
    elif opcion == 3:

        print("Seleccionó la opción 3")
        try:
            rut = int(input("Ingrese rut:"))

            if rut < 4000000 or rut > 99999999:
                print("Rut fuera de rango")
                raise("Error de rango")
        except:
            print("Error: Rut no es válido")
            input("Presione enter para continuar....")
            continue

        clienteEncontrado = []
        for cliente in clientes:
            if cliente[0] == rut:
                clienteEncontrado = cliente
                break
        
        if  len(clienteEncontrado) == 0:
            print("El rut no fue encontrado")
        else:
            print("*****  Datos del cliente ******")
            print("Rut           :", clienteEncontrado[0])
            print("Nombre           :", clienteEncontrado[1])
            print("Dirección        :", clienteEncontrado[2])
            print("Comuna           :", clienteEncontrado[3])
            print("Correo           :", clienteEncontrado[4])
            print("Edad             :", clienteEncontrado[5])
            print("Genero           :", clienteEncontrado[6])
            print("Celular          :", clienteEncontrado[7])
            print("Tipo             :", clienteEncontrado[8])
            print("Fecha Suscripción:", clienteEncontrado[10])  
        #Opcion salir
    elif opcion == 4:
        print("Aplicación cerrada")

    
    input("Presione enter para continuar.....")