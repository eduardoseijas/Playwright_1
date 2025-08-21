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
    page.goto("https://validaciones.rodrigovillanueva.com.mx/Campos_Dos_OK.html")
    #expect(page).to_have_title("Formulario de Ejemplo")
    #page.mouse.wheel(0,800)
    
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Validar_Url_PaginaWeb("https://validaciones.rodrigovillanueva.com.mx/Campos_Dos_OK.html",1)
    F.Validar_Titulo_PaginaWeb("Formulario de Ejemplo")
    F.Esperar(1)
    F.Scroll_x_y(0,400)
    
    #Escribir solo letras
    F.Texto("//input[@id='onlyLetters']","Estoespartedeeltestcalendario",1)
    F.Texto("//input[@id='alphanumeric']","AquiescribimosletrasyNumeros123344545343",2)
    F.Texto("//input[@id='emailFormat']","Eduardo@gmail.com")
    F.Texto("//input[@id='urlFormat']","https://validaciones.rodrigovillanueva.com.mx/Campos_Dos_OK.html",1)
    
    #Calendario
    #Otra forma de poder o ejecutar un calendario, con la opcion tab
    #Funcion tab
    F.Texto("//input[@id='dateFormat']","2025-08-23",2)
    #page.keyboard.press("Tab") #esta es la funcion tab
    #page.keyboard.press("Tab")
    #page.keyboard.press("Tab")
    #page.keyboard.press("Tab")
    
    #Con la funcion creada ya guardada en funciones globales
    F.Tab(1)
    F.Tab(1)
    F.Tab(1)
    F.Tab(1)
    
    F.Esperar(3)
    F.Click("//button[normalize-space()='Enviar']",1)