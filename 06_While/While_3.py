

num=1
bandera=True

while bandera==True:
    a=0
    b=0
    print("1.- Suma de dos numeros")
    print("2.- Resta de dos numeros")
    print("3.- Salir")
    
    num=int(input("Selecciona una opcion: "))
    if num==1 or num==2 or num==3:
        if num==1:
            a=float(input("Dame el primer numero: "))
            b=float(input("Dame el segundo numero: "))
            suma=a+b
            print(f"La suma es {suma} \n")
        elif num==2:
            a=float(input("Dame el primer numero: "))
            b=float(input("Dame el segundo numero: "))
            resta=a-b
            print(f"La resta es {resta} \n")
        else:
            print("Hasta Luego \n")
            bandera=False
            
    else:
        print("No es una opcion, desbes elegir entre 1,2 o 3 \n")