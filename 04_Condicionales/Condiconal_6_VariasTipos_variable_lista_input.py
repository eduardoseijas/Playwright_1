nom="Eduardo"
nom2="eduardo"

# if nom==nom2:
#     print("Son iguales")
# else:
#     print("No son iguales")

#-----------------------------------

#or

# if nom=="Eduardo" or nom2=="eduardo":
#     print("Son iguales")
# else:
#     print("Son Distintos")

#---------------------------

# a="N"

# if a in ["y","Y","YES","yes"]:
#     print("Si existe el Elemento en la lista")
# else:
#     print("No existe el elemento en la lista")

#-------------------------

#usando imput

nom=input("Dame tu nombre: ")
#nom="eduardo"
print(nom)

# if nom=="eduardo":
#     print("Tu nombre es eduardo")
# else:
#     print("Tu nombre no es eduardo o no esta en minuscula")

#minuscula con el .lower()

# if nom.lower()=="eduardo":
#     print("Bienvenido al sistema eduardo")
# else:
#     print("Tu nombre no es eduardo")



# lista=["eduardo","pedro","darlin"]

# if nom.lower() in lista:
#     print("El usuario " + str(nom) + " tiene el acceso permitido")
# else:
#     print("El usuario no tiene acceso")

#Mayusculas .upper()

# lista=["EDUARDO","PEDRO","DARLIN"]

# if nom.upper() in lista:
#     print("El usuario " + str(nom) + " tiene el acceso permitido")
# else:
#     print("El usuario no tiene acceso")

#Primera letra Mayuscula .title()

# lista=["Eduardo","Pedro","Darlin"]

# if nom.title() in lista:
#     print("El usuario " + str(nom) + " tiene el acceso permitido")
# else:
#     print("El usuario no tiene acceso")
    
    
a="Edu"
b="Rodrigo"

if len(a)>len(b):
    print("A es el Mayor")
else:
    print("B es el Mayor")
    
#Con len(), ves el numero de caracteres que tiene
print("A tiene " + str(len(a)) + " Caracteres")
print("B tiene " + str(len(b)) + "Caracteres")