#Funcion predefinida

def sumadeDos(a,b):
    suma=a+b
    return suma
def pedirDos():
    a=float(input("\nDame el primer valor: "))
    b=float(input("\nDame el segundo valor: "))
    return a,b

x1,x2=pedirDos()
resultado=sumadeDos(x1,x2)
print(f"\nLa suma es: {resultado}\n")


