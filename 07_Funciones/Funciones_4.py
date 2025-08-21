#De una funcion regresar varios resultados

def sumadeDos():
    a=float(input("Dame el primer numero: "))
    b=float(input("Dame el segundo numero: "))
    if a > 0 and b> 0:
         suma=a+b
         resta=a-b
         multi=a*b
         return suma, resta, multi
         
    else:
        print("Introduce un numero mayor a 0")
    
# resultado=sumadeDos() #va a cambiar al valor que venga de la suma
# print(f"El resultado es: {resultado}")
# print(type(resultado)) #es una tupla

# for num in resultado:
#     print(num)

rs,rr,rm=sumadeDos()
print(f"\n La suma es: {rs} \n")
print(f" La resta es: {rr} \n")
print(f" La multiplicacion es: {rm} \n")

operacion=rs+rr+rm
print(f"\n La suma de todos los resultados es: {operacion} \n")