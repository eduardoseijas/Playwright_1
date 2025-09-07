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
pdf1="D:/Practica_Playwright/18_Unpload_Files/Imagenes/Upload/Playwright_Prueba_Upload.jpg"
#invertir la diagonal, \ por /

#@pytest.mark.parametrize("Numero,Esperando", [("3+5", 8), ("2+4", 6),("6*9", 42),("9*5",45)])
@pytest.mark.parametrize("Nombre, Apellido,Tlf, Email, Direccion", [("Eduardo","Seijas","1234567890","eduardo@gmail.com","Paris 1"), 
                                              ("Pedro","Perez","1029384756","pedro@gmail.com","Paris 2"),
                                              ("Lucia","Martin","1029384756","lucia@gmail.com","Paris 3"),
                                              ("Darlin","Seijas","2389674512","darlin@gmail.com","Paris 4")])
def test_parametrizacion(set_up_parametrizacion,Nombre,Apellido,Tlf,Email,Direccion):
    page=set_up_parametrizacion
    F=Funciones_Globales_Total(page)
    F.Validar_Titulo_PaginaWeb("Formulario de Ejemplo")
    F.Scroll_x_y(0,400)
    F.Texto("//input[@id='nombre']",Nombre,1)
    F.Texto("//input[@id='apellidos']",Apellido,1)
    F.Texto("//input[@id='tel']",Tlf,1)
    F.Texto("//input[@id='email']",Email,1)
    F.Texto("//input[@id='direccion']",Direccion,1)
    F.Esperar(1)