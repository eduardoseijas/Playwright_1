import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random
import pytest
import sys #Libreria para informacion directamente del sistema operativo

#playwright codegen https://www.saucedemo.com/
tiempo=1.6
ruta="Imagenes_Globales/Select"
pdf1="C:/Practica_Playwright/18_Unpload_Files/Imagenes/Upload/Playwright_Prueba_Upload.jpg"
#invertir la diagonal, \ por /
def test_Inicio(set_up) -> None:
    page=set_up
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Validar_Url_PaginaWeb(".*/basic-html-form-test.html",1)
    F.Validar_Titulo_PaginaWeb(" HTML Form Elements",1)
    

#Termina un bloque, Coimenza el nuevo 
#----------------------------------------------------------------------------------------

def test_Carga_de_texto(set_up) -> None:
    page=set_up
    
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Texto("//input[@name='username']","Eduardo",1)
    F.Texto("//input[@name='password']","1233231212",1)
    F.Clear("//textarea[@name='comments']",1)
    F.Texto("//textarea[@name='comments']","Esta es una prueba de multiples test",2)
    
    
#@pytest.mark.skip(reason="Este Modulo esta inhabilitado Upload")    
def test_Unpload(set_up) -> None:
    page=set_up
    
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Texto("//input[@name='username']","Eduardo",1)
    F.Texto("//input[@name='password']","1233231212",1)
    F.Clear("//textarea[@name='comments']",1)
    F.Texto("//textarea[@name='comments']","Esta es una prueba de multiples test",2)
    
    #Upload test
    F.Upload_Files("//input[@name='filename']",pdf1,2)
    F.Esperar(2)
    
@pytest.mark.skipif(sys.platform=="win62",reason="No corre el test porque la plataforma es del tipo win32")  
def test_CheckBox(set_up) -> None:
    page=set_up
    
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Texto("//input[@name='username']","Eduardo",1)
    F.Texto("//input[@name='password']","1233231212",1)
    F.Clear("//textarea[@name='comments']",1)
    F.Texto("//textarea[@name='comments']","Esta es una prueba de multiples test",2)
    
    #Upload test
    F.Upload_Files("//input[@name='filename']",pdf1,2)
    F.Esperar(2)
    
    #Checkbox
    F.Click("//input[@value='cb3']",1)
    F.Click("//input[@value='cb2']",2)
    F.Click("//input[@value='rd1']",2)
    F.Scroll_x_y(0,800)
    F.Esperar(1)
    F.Combo_Value("//select[@name='multipleselect[]']","ms4",1)
    F.Combo_Value("//select[@name='multipleselect[]']","ms3",1)
    
    #Dropdown
    F.Combo_Value("//select[@name='dropdown']","dd5",2)
    
    #Fin hacer click en el boton
    F.Click("//input[@value='submit']",2)
    F.Scroll_x_y(0,800)
    F.Esperar(2)
    
    #print (sys.float_info)
    
    
    
    
