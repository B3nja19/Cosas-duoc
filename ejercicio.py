from re import A


print ("Hola Mundo")
cont = 1
acumulador = 1
numero = int(input("Ingrese un numero:"))

while cont  <= numero:
    acumulador *= cont
    cont += 1 
print("El factorial de", numero)
print ("es",acumulador)
