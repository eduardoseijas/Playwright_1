#Sirve para romper un ciclo

lista=[1,2,3,4,5,6,7,8,9]
total=0

for x in lista:
    total+=x
    if x==5:
        break
    print(f"La suma es: {total}")
        