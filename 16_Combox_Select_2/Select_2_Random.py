import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random

ruta="Imagenes_Globales/Select"

def test_select2(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
    page = context.new_page()
    page.goto("https://validaciones.rodrigovillanueva.com.mx/Form1.html")
    #expect(page).to_have_title("Formulario de Ejemplo")
    #page.mouse.wheel(0,800)
    
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Validar_Url_PaginaWeb("https://validaciones.rodrigovillanueva.com.mx/Form1.html",1)
    F.Validar_Titulo_PaginaWeb("Formulario de Ejemplo")
    F.Esperar(1)
    F.Scroll_x_y(0,400)
    
#Variable, para random
    numA2=random.sample(range(1,100000),6)
    
#Nombre
    F.Texto("//input[@id='nombre']","Eduardo"+str(numA2[0]),1) #Recordar el str cuanco concatenes en string
    F.Texto_img("//input[@id='apellidos']","Seijas"+str(numA2[0]),ruta+"Fotoapellidoconnumerorandom"+str(numA2[0])+".png",2)
    F.Texto("//input[@id='tel']","1234567890"),1
    F.Texto("//input[@id='email']","Eduardo@gmail.com",1)
    F.Texto("#direccion","Direccion1",2)