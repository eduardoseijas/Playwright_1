

#Condicional elif, vienen siempre despues del if, y para cerrar es con un else: al final y lanzas algo a imprimir print()
a=5
b=5

if a>b:
    print("A es Mayor")
    print(str(a) + " Es Mayor que " + str(b))
    
elif a<b:
    print("B es Mayor")
    print(str(b) + " Es Mayor que " + str(a))

elif a==b:
    print("A es igual que B")
    print(str(a) + " = " + str(b))
    
elif a!=b:
    print("A es diferente B")
    print(str(a) + " distinto " + str(b))
    
else:
    print("No es una opcion condicionada")
    