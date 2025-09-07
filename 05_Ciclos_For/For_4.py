#Ciclo for, recorriendo todos los valores de una lista

#Valores de una lista

frutas=["Pera", "Manzana", "Melon", "Sandia", "Platano", "Mango"]
x=0
# for fru in frutas:
#     x+=1
#     print(f"Mis fruta {x}: {fru}")

for fru in frutas:
    x+=1
    if fru=="Manzana":
        print(f"Mi fruta favorita es : {x} = {fru}")
    else:
        print(f"Las otras frutas son: {x} - {fru}")