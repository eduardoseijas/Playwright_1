#For anidado
#El for anidado lo que hace es que una vez, termine el primer ciclo


# for a in range (1,11):
#     for b in range (1,11):
#         #a * b = a * b
#         print(f" {a} x {b} = {a*b}")

#For para caracteres

# texto="Esto es un texto de ejemplo"
# x=0 #creo esta variable para que me haga un contador por cada letra
# for vt in texto:
#     x+=1 # creo el numero por cada letra al colocar la varibble x+=1 para que vaya sumando de 1 en 1 
#     print(f"{x} - {vt}")
    
# texto="Eduardo Seijas Pacheco"
# buscar="a"
# contador=0
# convertir=texto.lower()
# #print(convertir)

# for t in convertir:
#     if (t==buscar):
#         contador+=1
# print(f"Existen {contador} letras {buscar}")

#Numero de vocales en un texto

texto="Eduardo Seijas Pacheco"
contador=0
convertir=texto.lower()
print(convertir)

for t in convertir:
    if (t=="a" or t== "e" or t== "i" or t== "o" or t== "u"):
        contador+=1
        print(f"La vocal encotrada - {t} - es el numero: {contador}")