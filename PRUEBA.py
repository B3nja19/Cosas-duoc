from numpy import random
print("Hola mundo")

a1 = random.randint(1500,3500, size=1)
opcion=0
tipo=""
patente=""
marca=""
precio=0
multat=0
conta=""
fecha=""
dueno=""
registros=[]
vehiculo =[]

#funciones

#funcion 1
def grabar():
    print("Registro del vehículo") 

    tipo=input("Ingrese el Tipo de vehículo: ")

    try:
        patente=input("Ingrese la patente del vehículo: ")
        patente=patente.upper()
        if patente.count("") !=7 and patente.count(int) !=7:
            raise("Error de rango")
    except:
        print("Error:Número de patente fuera de rango")
        input("Presione para continuar...")
        return
    try:
        marca=input("Ingrese la marca del vehículo: ")
        if marca.count("") >15:
            raise("Error de rango")
        elif marca.count("") <=2:
            raise("Error de rango")
    except:
        print("Error:Nombre de marca fuera de rango")
        input("Presione para continuar...")
        return
    try:
        precio=int(input("Ingrese el precio del vehículo: "))
        if precio <= 4999999:
            raise("Error de rango")
    except:
        print("ERROR:Precio fuera de rango")
        input("Presione enter para continuar...")
        return
    try:
        multat=int(input("Ingrese el monto total de multas: "))
        if multat=="":
            raise("ERROR")
    except:
        print("Error: Número no valido")
        input("Presione enter para continuar...")
        return
    conta=input(" Aprobación de emision de contaminante:\n1.-Si\n2.-No\nIngrese Opción: ")
    if conta== "1":
        conta="Si"
    elif conta=="2":
        conta="No"
    else:
        print("Error: Tipo no es válido")
        input("Presione enter para continuar....")
        return
    
    try:
        fecha=input("Ingrese la fecha de registro del vehículo Ej: 00/00/0000\nIngrese fecha: ")
        if fecha.count("/") !=2:
            raise("Error")
    except:
        print("Error:Fecha no valida")
        input("Presiona enter para continuar...")
        return
    try:
        dueno=input("Ingrese el nombre del dueño actual: ")
        if dueno.count("") <=5:
            raise("Error de rango")
    except:
        print("Error:Nombre fuera de rango")
        input("Presione para continuar...")
        return  
    registro=[tipo,patente,marca,precio,multat,conta,fecha,dueno]
    registros.append(registro)

#funcion 2
def buscar():
    print("Seleccionó la opción 2") 
    patente=input("Ingrese la patente: ")
    patente=patente.upper()
    Datosregistro = []

    for registro in registros:
        if registro[1] == patente:
            Datosregistro = registro
            break 

    if  len(Datosregistro) ==0:
        print("La patente no fue encontrada")
    else:
        print("================= Datos del Vehículo =================")
        print("Tipo                                 :", Datosregistro[0])
        print("Patente                              :", Datosregistro[1])
        print("Marca                                :", Datosregistro[2])
        print("Precio                               :", Datosregistro[3])
        print("Monto total de multas                :", Datosregistro[4])
        print("Aprobación de emisión de contaminante:", Datosregistro[5])
        print("Fecha                                :", Datosregistro[6])
        print("Dueño                                :", Datosregistro[7])
        print("=====================================================")
        return
#Funcion 3
def imprimir():
    print("Seleccionó Imprimir el certificado de su vehículo") 
    patente=input("Ingrese la patente: ")
    patente=patente.upper()
    Datosregistro = []

    for registro in registros:
        if registro[1] == patente:
            Datosregistro = registro
            break 

    if  len(Datosregistro) ==0:
        print("La patente no fue encontrada")
    else:
        print(f"El monto a cobrar por el certificado es de:{a1}")
        print("================= Datos del Vehículo =================")
        print("Tipo                                 :", Datosregistro[0])
        print("Patente                              :", Datosregistro[1])
        print("Marca                                :", Datosregistro[2])
        print("Precio                               :", Datosregistro[3])
        print("Monto total de multas                :", Datosregistro[4])
        print("Aprobación de emisión de contaminante:", Datosregistro[5])
        print("Fecha                                :", Datosregistro[6])
        print("Dueño                                :", Datosregistro[7])
        print("=====================================================")
        return

#aplicacion
listadoDeOpciones = [1,2,3,4]
while  opcion  !=  4 :
    print ( "=============== Auto Seguro ===============" )
    print ( "1.- Grabar" )
    print ( "2.- Buscar" )
    print ( "3.- Imprimir certificado" )
    print ( "4.- Salir" )
    print("=====================================================")
    opcion  =  int ( input ( "Ingrese la opción:" ))

    if opcion not in listadoDeOpciones:
        print("=== Error: Opción no válida")
        input("Presione enter para continuar...")
        continue
        
    if opcion ==4:
        print("Gracias por preferir Auto Seguro")
        print("Aplicacion By Riquelme and Fazio corp. Version 7.1 (beta) ")
        print("Adios :)")
    else:
        if opcion == 1:
            grabar() 
        elif opcion ==2:
            buscar()
        elif opcion ==3:
            imprimir()
