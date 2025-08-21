



# num=0
# while num !=3:
#     a=0
#     b=0
#     print("1. -Suma de dos numeros")
#     print("2. -Resta de dos numeros")
#     print("3. -Salir")
    
#     num=int(input("Selecciona una opcion: "))
#     if num==1 or num==2 or num==3:
#         if num==1:
#             a=float(input("Dame el Valor uno: "))
#             b=float(input("Dame el Valor dos: "))
#             suma=a+b
#             print(f"La suma es: {suma}   \n\n")
#         elif num==2:
#             a=float(input("Dame el Valor uno: "))
#             b=float(input("Dame el Valor dos: "))
#             resta=a-b
#             print(f"La resta es: {resta} \n\n")

#     else:
#      print("Selecciona una Opcion entre 1,2 o 3\n\n")


bandera=True
num=0
while bandera==True:
    a=0
    b=0
    print("1. -Suma de dos numeros")
    print("2. -Resta de dos numeros")
    print("3. -Salir")
    
    num=int(input("Selecciona una opcion: "))
    if num==1 or num==2 or num==3:
        if num==1:
            a=float(input("Dame el Valor uno: "))
            b=float(input("Dame el Valor dos: "))
            suma=a+b
            print(f"La suma es: {suma}   \n\n")
        elif num==2:
            a=float(input("Dame el Valor uno: "))
            b=float(input("Dame el Valor dos: "))
            resta=a-b
            print(f"La resta es: {resta} \n\n")
        else:
            print("Hasta Luego")
            bandera=False

    else:
     print("Selecciona una Opcion entre 1,2 o 3\n\n")