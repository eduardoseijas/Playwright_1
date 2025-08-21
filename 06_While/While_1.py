#Ciclo While
#Es parecido al ciclo for pero la condicionante va por fuera y la repeticion la pone dentro del while

# x=0
# while x < 10:
#     print(f"El numero es: {x}")
#     x+=1
    

bandera=True
contador=0
while bandera== True:
    print(f"Hola mundo {contador}")
    contador+=1
    if contador==100:
        bandera=False
        
