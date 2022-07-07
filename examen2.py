from tkinter import E
import numpy as nu
Entradas = nu.array([   ["","", "","", "", "","", "", "",""], 
                        ["","", "","", "", "","", "", "",""], 
                        ["","", "","", "", "","", "", "",""],
                        ["","", "","", "", "","", "", "",""],
                        ["","", "","", "", "","", "", "",""],
                        ["","", "","", "", "","", "", "",""],
                        ["","", "","", "", "","", "", "",""],
                        ["","", "","", "", "","", "", "",""],
                        ["","", "","", "", "","", "", "",""],
                        ["","", "","", "", "","", "", "",""] ], dtype = object)








# definir funciones
def comprar(Entradas):
    print("=== Asientos ===") 
    print("1.- Platinum, $120.000. (Asientos del 1 al 20).")
    print("2.- Gold, $80.000. (Asientos del 21 al 50).")
    print("3.- Silver, $50.000. (Asientos del 51 al 100.).")
    eleccion = int(input("Ingrese la opción: "))
    try:
        if eleccion == 1:
            print("**** Platinum ****")
            try:
                numfila = int(input("Ingrese número de fila (1 o 2): "))
                if numfila >= 3 or numfila<= 0:
                    print("Error en el ingreso de la opción.")
                    return
                else:
                    ent = numfila - 1
                    asientosdisponibles(Entradas, ent)
                    nrocolumna = int(input("Ingrese número de columna (1 al 10): "))
                    if nrocolumna >= 11 or nrocolumna <=0:
                        print("Error en el ingreso de la opción.")
                        return
                    else:
                        columna = nrocolumna - 1
                        nombre = input("Ingrese el nombre          : ")
                        Entradas[ent, columna] = nombre
            except:
                print("=== Error: Opción no válida")
                input("Presione enter para continuar...") 

        if eleccion == 2:
            print("**** GOLD ****")
            try:
                numfila = int(input("Ingrese número de fila (3 al 5): "))
                if numfila >= 6 or numfila<= 2:
                    print("Error en el ingreso de la opción.")
                    return
                else:
                    ent = numfila - 1
                    asientosdisponibles(Entradas, ent)
                    nrocolumna = int(input("Ingrese número de columna (1 al 10): "))
                    if nrocolumna >= 11 or nrocolumna <=0:
                        print("Error en el ingreso de la opción.")
                        return
                    else:
                        columna = nrocolumna - 1
                        nombre = input("Ingrese el nombre          : ")
                        Entradas[ent, columna] = nombre
            except:
                print("=== Error: Opción no válida")
                input("Presione enter para continuar...")

        if eleccion == 3:
            print("**** SILVER ****")
            try:
                numfila = int(input("Ingrese número de fila (6 al 10): "))
                if numfila >= 11 or numfila<= 5:
                    print("Error en el ingreso de la opción.")
                    return
                else:
                    ent = numfila - 1
                    asientosdisponibles(Entradas, ent)
                    nrocolumna = int(input("Ingrese número de columna (1 al 10): "))
                    if nrocolumna >= 11 or nrocolumna <=0:
                        print("Error en el ingreso de la opción.")
                        return
                    else:
                        columna = nrocolumna - 1
                        nombre = input("Ingrese el nombre          : ")
                        Entradas[ent, columna] = nombre
            except:
                print("=== Error: Opción no válida")
                input("Presione enter para continuar...")
    except:
        print("=== Error: Opción no válida")
        input("Presione enter para continuar...")


def asientosdisponibles(casillero, fila):
    print("Columnas disponibles de la fila ", fila+1)
    nroCasillero = 1
    for columna in casillero[fila]:
        if columna == "":
            print("Columna ", nroCasillero)
        nroCasillero += 1


def mostrarUbicaciones(casillero):
    print("*** Disponibilidad de casilleros ***")
    filas = ""
    nroCasillero = 1
    valor = ""
    for fila in casillero:
        for columna in fila:
            if columna == "":
                valor = str(nroCasillero)
            else:
                valor = "X"
            filas += valor + " " 
            nroCasillero += 1
        filas += "\n"
    print(filas)
    input("Presione enter para continuar...") 


def mostrarNombre(casillero):
    print("Clientes de los casilleros")
    listado = ""
    nroCasillero = 1
    for fila in casillero:
        for columna in fila:
 #           if columna != "":
            print("casillero: ", nroCasillero, "nombre:", columna)
            nroCasillero += 1
    input("Presione enter para volver al menú...")

def calcularGanancias(casillero):
    total = 0
    fil = 1
    for fila in casillero:
        for columna in fila:
            if columna != "":
                if fil == 1 or fil ==2:
                    total += 120000
                elif fil == 3 or fil==4 or fil ==5:
                    total += 80000
                elif fil == 6 or fil==7 or fil==8 or fil==9 or fil==10:
                    total += 50000            
        fil += 1
    print("Total de ganancias:", total)
    input("Presione enter para volver al menú...")

def AsientosD(Asientos):
    print(" Disponibilidad de casilleros ")
    filas = ""
    nroAsiento = 1
    valor = ""
    for fila in Asientos:
        for columna in fila:
            if columna == "":
                valor = str(nroAsiento)
            else:
                valor = "X"
            filas += valor + " " 
            nroAsiento += 1
        filas += "\n"
    print(filas)
    input("Presione enter para continuar...")    

# definir aplicacion
opcion= 0
listadoDeOpciones = ["1", "2", "3", "4", "5"]
while opcion != "5":
    print("===== CREATIVOS.CL =====")
    print("1.- Comprar entradas")
    print("2.- Mostrar ubicaciones disponibles")
    print("3.- Ver listado de asistentes")
    print("4.- Mostrar ganancias totales")
    print("5.- Salir")
    opcion = input("Seleccione opción:")

    if opcion not in listadoDeOpciones:
        print("=== Error: Opción no válida")
        input("Presione enter para continuar...")
        continue
    if opcion == "5":
        print("Adios, gracias por visitar CREATIVOS.CL.")
        print("App Version 4.3. By Marco Elias Peña Castillo, 07-07-2022")
    else:
        if opcion == "1":
            comprar(Entradas)
        elif opcion == "2":
            mostrarUbicaciones(Entradas)
        elif opcion == "3":
            mostrarNombre(Entradas)
        elif opcion == "4":
            calcularGanancias(Entradas)


           