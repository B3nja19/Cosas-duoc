from distutils.util import subst_vars


subtotal = 0
valor = 0
descuento = 0
total = 0
total2 = 0
print("Hola mundo")
print("~~~Bienvenido a su tienda de articulos de limpieza~~~")
print("Tiene los siguientes articulos disponibles:")
print("Mascarillas clínicas $1.000\nGuantes clínicos $1.000\nDelantal clínico $2.000\nAmonio Cuaternario $3.000 ")

unimascarilla=int(input("Ingrese la cantidad de mascarillas:"))
uniguantes=int(input("Ingrese la cantidad de Guantes:"))
unidelantal=int(input("Ingrese la cantidad de delantales:"))
uniamonio=int(input("Ingrese la cantidad de Amonio:"))
if unimascarilla == 1:
    valor = 1000
subtotal = subtotal + valor * unimascarilla
if uniguantes == 1:
    valor = 1000 
subtotal = subtotal + valor * uniguantes
if unidelantal == 1:
    valor = 2000
    subtotal = subtotal + valor * unidelantal
if uniamonio == 1:
    valor = 3000
    subtotal = subtotal + valor * uniamonio

print("El total de la compra es:")
print("subtotal      :",subtotal)
descuento = float (input("¿Posee algun tipo de descuento 1.-Si 2.No?"))
total = descuento * subtotal
total2 = subtotal - total 
print("Precio final es de ", int(total2))


