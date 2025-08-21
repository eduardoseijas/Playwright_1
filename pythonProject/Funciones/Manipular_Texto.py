
#Mayuscula con el .upper()
texto="Bienvenido a Python"
rt=texto.upper()
print(rt)

#Minuscula con el .lower()
texto="Bienvenido a Python"
rt=texto.lower()
print(rt)

#Para quitar los espacios, del inicio con el .strip()
texto="                     Bienvenido a Python         "
rt=texto.strip()
print(rt)

#Para remplazar un texto, con el .replace
texto="Bienvenido a Python"
rt=texto.replace("Python", "JavaScript")
print(rt)

#Combinando cotres, por ejemplo Para quitar los espacios, del inicio con el .strip() con el que es para remplazar un texto, con el .replace
texto="     Bienvenido a Python"
rt=texto.replace("Python", "Php").strip()
print(rt)