

import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random

#PARA LANZAR UN DEBUG, EL COMANDO ES EL SIGUIENTE
#Set PWDEBUG=1
#pytest Debug_test_1.py -s
#en mi caso que lo corro desde la raiz 
#python -m pytest .\21_Debug_test\Debug_test_1.py -s

ruta="Imagenes_Globales/Select"
pdf1="C:/Practica_Playwright/18_Unpload_Files/Imagenes/Upload/Playwright_Prueba_Upload.jpg"
#invertir la diagonal, \ por /
def test_Upload_Files(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
   
   
    page = context.new_page()
    page.goto("https://testpages.eviltester.com/styled/file-upload-test.html")
    #expect(page).to_have_title("Formulario de Ejemplo")
    #page.mouse.wheel(0,800) #scroll hacia abajo
    
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Validar_Url_PaginaWeb(".*/file-upload-test.html",1)
    F.Validar_Titulo_PaginaWeb("Upload a File",1)
    
#Para entrar modo DEBUG  
    page.pause()
    
#Upload File
    F.Upload_Files("//input[@id='fileinput']",pdf1,1)
    #F.Upload_Files_img("//input[@id='fileinput']",pdf1,ruta+"Uploadprueba.png",1)
    F.Click("//input[@id='itsanimage']",1)
    F.Click("//input[@name='upload']",2)
    F.Esperar(2)
    

    
    context.close()
    browser.close()
