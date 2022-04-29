print("ingrese Numero 1 para (SUMA)")
print("ingrese Numero 2 para (RESTA)")
print("ingrese Numero 3 para (MULTIPLICACION)")
print("ingrese Numero 4 para (DIVISION)")
print("ingrese Numero 0 para (PARA FINALIZAR)")


opcion= int(input("ingrese la opcion del menu : "))

if opcion == 1 :
    Numero1= int(input("ingrese Numero1 : "))
    Numero2= int(input("ingrese NUmero2 : "))
    resultado=Numero1+Numero2
    print(resultado)
    
if opcion==2 :
    Numero1= int(input("ingrese Numero1 : "))
    Numero2= int(input("ingrese NUmero2 : "))
    resultado=Numero1-Numero2
    print(resultado)
