#hacerla con menos lineas de codigo
#CON EL or
a=50
b=60
c=10


if a>b or a>c: #con el or, es:  se tiene que cumplir una de las 2 condiciones
    print("El Mayor es A")

elif b>a or b>c:#con el and, es: se tiene que cumplir una de las 2 condiciones
    print("El Mayor es B")
    
elif c>a or c>b:#con el and, es: se tiene que cumplir una de las 2 condiciones
    print("El mayor es C")

else:
    print("No cumple ninguna de las condiciones")
