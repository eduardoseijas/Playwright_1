import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random

ruta="Imagenes_Globales/Select"
pdf1="C:/Practica_Playwright/18_Unpload_Files/Imagenes/Upload/Playwright_Prueba_Upload.jpg"
#invertir la diagonal, \ por /
def test_Upload_Files(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
    page = context.new_page()
    page.goto("https://www.perplexity.ai/")
    
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Validar_Url_PaginaWeb("https://www.perplexity.ai/",1)
    F.Validar_Titulo_PaginaWeb("Perplexity",1)
    F.Scroll_x_y(0,400)
    F.Texto("//div[@id='ask-input']//p","Ferr",2)
    F.Click_First("text=Ferrari",1)
    F.Esperar(3)