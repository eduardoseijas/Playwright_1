#Sirve para sume todos menos el que se indica en la variable

lista=[1,2,3,4,5,6,7]
total=0

for x in lista:
    if x==7 or x==5:
        continue 
    total +=x
    #Que sume todos menos el 5
    print(f"La suma es: {total}")
        