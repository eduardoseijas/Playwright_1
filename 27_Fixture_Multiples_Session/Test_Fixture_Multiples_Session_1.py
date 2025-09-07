import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random
import pytest
import sys #Libreria para informacion directamente del sistema operativo

#playwright codegen https://www.saucedemo.com/
tiempo=0.3
ruta="Imagenes_Globales/Select"
pdf1="C:/Practica_Playwright/18_Unpload_Files/Imagenes/Upload/Playwright_Prueba_Upload.jpg"
#invertir la diagonal, \ por /
def test_Inicio_Session_Con_UsuarioErrado(set_up_Session_ValidacionNombre) -> None:
    page=set_up_Session_ValidacionNombre
    F=Funciones_Globales_Total(page)
    F.Validar_Texto("//h3[contains(text(),'Epic sadface: Username and password do not match a')]","Epic sadface: Username and password do not match any user in this service",1)
    print(F.Validar_Texto)
    texto_esperado="Epic sadface: Username and password do not match any user in this service"
    print(texto_esperado)
    
    assert texto_esperado =="Epic sadface: Username and password do not match any user in this service", "Error del Nomre"
    
    
    
  
    #estuve intentando hacer una variable texto=F.Validar_Texto("//h3[contains(text(),'Epic sadface: Username and password do not match a')]","Epic sadface: Username and password do not match any user in this service",1)
    #par crear un assert texto_esperado in str(texto), "Error del Nomre"
    #el tema es que al crear esa variable, no me la reconoce la informacion, la ve como None
    #por eso cree un assert sin crear una variable y colocando que el texto_esperado== "Epic sadface: Username and password do not match any user in this service"
    #Con esto logre hacer la validacion assert
   
