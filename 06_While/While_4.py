


num=10
bandera=True

while bandera==True:
    n=int(input("Dame un numero del 1 al 20: "))
    if n > 0 and n <= 20:
        if n == num:
            print("Adivinaste el numero, Felicidades")
            bandera=False
        elif n > num:
            print(f"El numero {n} es mayor, introduce uno menor")
            
        elif n< num:
            print(f"El numero es menor que la meta, pon un numero mayor")
            
    else:
        print("El numero tiene que ser del 1 al 20 \n")