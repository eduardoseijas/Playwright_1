#Manipular tabuladores (Escape)
#Con la comillas solas me da error si uso el slash invertido \al abrir la comida y cerrar, me permite colocarlas dentro de las comillas de texto
texto="Esto es un texto de \"Python\""
print(texto)

#con el \t haces un tabulador con el \n bajas la linea y si le agrego \t\t le agrego doble tabulador
texto2="\tEsto tiene un espacion al inicio tab\n\t\tEsto es otra linea\n\t\t\tEsta es la tercera linea pero sin tab"
print(texto2)