#Mayor de dos numeros

def mayorDos(num1,num2):
    if (type(num1)==int or type(num1)==float):
        if(type(num2)==int or type(num2)==float):
            if num1 > num2:
                print(f"El mayor es: {num1}")
            elif num1 == num2:
                print("Son iguales")
            else:
                print(f"El mayor es: {num2}")
        else:
            print(f"El numero {num2} no es un numero entero o flotante")
    else:
        print(f"El numero {num1} no es un numero entero o flotante")

mayorDos(12,20)