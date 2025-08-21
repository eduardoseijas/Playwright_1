#Capitalize: la primera letra la pone en mayuscula
dir="demo de la direccion 1"
dir=dir.capitalize()
print(dir)

#Casefold: Convierte a minusculas
nom="Eduardo Seijas Pacheco"
nom=nom.casefold()
print(nom)

#Center: Deja un espacio entre los caracteres y nos centra el texto
dato="Ferrary"
dato=dato.center(20)
print(dato)

#Count: Sirve para contar el numero de veces que se repite un elemento.
dato1="Las manzanas son rojas, las manzanas rojas son mi frutas favoritas y la manzanas verdes son las que mas me gustan"
dato1=dato1.count("manzanas",0,100)
print("Existen la palabra (manzanas), este numero de veces: "+str(dato1))

#Endwith: Si la cadena de texto termina con la palabra que coloquemos, indicara si es TRUE o FALSE
dato2="Hola Bienvenido a Mundo de Python"
dato2=dato2.endswith("Python")
print(dato2)

#Find: Buscar contenido
dato3="Esto es un ejemplo de texto"
dato3=dato3.find("ejemplo")
print("En que opcion se enceuntra la palabra: " +str(dato3))