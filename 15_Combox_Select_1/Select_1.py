import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion


ruta="Imagenes_Globales/Select"

def test_select1(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
    page = context.new_page()
    page.goto("https://validaciones.rodrigovillanueva.com.mx/Form1.html")
    expect(page).to_have_title("Formulario de Ejemplo")
    #page.mouse.wheel(0,800)
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Esperar(1)
    F.Scroll_x_y(0,400)
    
    #Nombre
    F.Texto_img("//input[@id='nombre']","Eduardo",ruta+"Nombre.png",1)
    F.Texto("//input[@id='apellidos']","Seijas",1)
    F.Texto_img("//input[@id='tel']","0123456789",ruta+"telefono.png",1)
    F.Texto("//input[@id='email']","Eduardo@gmail.com",1)
    F.Texto("//input[@id='direccion']","Direccion1",2)
    

 
    
    context.close()
    browser.close()