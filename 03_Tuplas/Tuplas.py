#Las tuplas son listas inmutables, no se pueden modificar con append, extend, remove
#utilidad->Mas rapidas, formatan un strings, se puede utilizar con claves para diccionarios

#Primer ejemplo:

frutas=tuple(("Melon","Papaya","Sandia","Banana"))
print(frutas)
print(frutas[0])
print(frutas[2])
print(len(frutas)) #Con la funcion len vemos el numero total de frutas que tiene esa tuple
print(type(frutas)) #con esta funcion type, vemos la clase que es, una tuple