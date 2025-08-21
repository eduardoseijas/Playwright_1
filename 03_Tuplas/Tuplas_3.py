#Tercer ejemplo

tupla1=("Eduardo","Seijas","Pacheco",35,662555793)
tupla2=(1,2,3,4,5,6,7,3,8,9,3,3)
nom,ap,am,edad,telef=tupla1
print(nom)
print(ap)
print(am)
print(edad)
print(telef)
print(tupla1) #Con parentesis es una tupla
listatupla1=list(tupla1) #Con esta variable estas convirtiendo tupla1 a una lista
print(listatupla1) #Con corchetes una lista

print("Pacheco" in tupla1) #esta manera es para buscar datos dentro de una tupla

print(35 in listatupla1) #Esta manera es para buscar datos dentro de la lista que cree
print(tupla2.count(3)) #Con esto en tupla2 contamos cuantas veces en total se repite un valor que querramos saber
if tupla2.count(3) > 2:
    print(f"Hay mas de 2 elementos tipo 3, existen {tupla2.count(3)}")