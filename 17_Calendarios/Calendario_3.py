import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random

ruta="Imagenes_Globales/Select"

def test_Calendarios(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
    page = context.new_page()
    page.goto("https://material.angularjs.org/latest/demo/datepicker")
    #expect(page).to_have_title("Formulario de Ejemplo")
    #page.mouse.wheel(0,800)
    
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Validar_Url_PaginaWeb("https://material.angularjs.org/latest/demo/datepicker",1)
    F.Validar_Titulo_PaginaWeb("AngularJS Material - Demos > Datepicker")
    F.Esperar(1)
    F.Scroll_x_y(0,2000)

    
    #Calendario
    #Otra forma de poder o ejecutar un calendario, con la opcion Click, es mas segura
    F.Click("(//td[@role='gridcell'])[110]",2)
    F.Click("(//span[@class='md-calendar-date-selection-indicator'][normalize-space()='18'])[4]",3)
    