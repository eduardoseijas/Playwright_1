import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion


ruta="Imagenes_Globales/Select"

def test_select1(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
    page = context.new_page()
    page.goto("https://validaciones.rodrigovillanueva.com.mx/Radios_Ok.html")
    expect(page).to_have_title("Formulario de Ejemplo")
    #page.mouse.wheel(0,800)
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Esperar(1)
    F.Scroll_x_y(0,400)
    
    #Nombre
    F.Texto("//input[@id='campo1']","Eduardo",1)
    F.Texto("//input[@id='campo2']","1234567890",1)
    
    #Click
    F.Click("//input[@id='opcion1']",1)
    F.Click_img("//input[@id='opcion2']",ruta+"Click2.png",2)