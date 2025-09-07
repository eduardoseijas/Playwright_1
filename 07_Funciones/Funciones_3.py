#Suma de 2 numeros

# def sumadeDos(a,b):
#     suma=a+b
#     print(f"\n La suma es {suma} \n")
    
# sumadeDos(3,10)

#-------------------------------------------

# def sumadeDos():
#     a=float(input("Dame el primer numero: "))
#     b=float(input("Dame el segundo numero: "))
#     if a > 0 and b> 0:
#          suma=a+b
#          print(f"\n La suma de {a} + {b} = {suma} \n")
         
#     else:
#         print("Introduce un numero mayor a 0")
    
# sumadeDos()    
    
    
#--------------------------------------------------------

def sumadeDos():
    a=float(input("Dame el primer numero: "))
    b=float(input("Dame el segundo numero: "))
    if a > 0 and b> 0:
         suma=a+b
         return suma
         
    else:
        print("Introduce un numero mayor a 0")
    
resultado=sumadeDos() #va a cambiar al valor que venga de la suma
print(f"El resultado es: {resultado}")
resultado+=10
print(f"El resultado es, resultado, sumandole 10 mas: {resultado}")