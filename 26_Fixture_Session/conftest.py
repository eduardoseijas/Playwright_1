import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random
import pytest
import sys #Libreria para informacion directamente del sistema operativo

tiempo=0.3
ruta="Imagenes_Globales/Select"
pdf1="C:/Practica_Playwright/18_Unpload_Files/Imagenes/Upload/Playwright_Prueba_Upload.jpg"
#invertir la diagonal, \ por /
Url="https://www.saucedemo.com/"

@pytest.fixture(scope="session") # entre las comillas puedes usar tambien "session"
def set_up_session(playwright)-> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
    
    #Iniciar Trace Viewer
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto(Url)
    page.set_default_timeout(5000)
    F=Funciones_Globales_Total(page)
    F.Validar_Titulo_PaginaWeb("Swag Labs")
    #page.mouse.wheel(0,400)
    F.Scroll_x_y(0,400)
    F.Esperar(tiempo)
    
    #INICIAR SESION DE LA PAG WEB
    F.Texto("//input[@id='user-name']","standard_user",tiempo)
    F.Texto("//input[@id='password']","secret_sauce", tiempo)
    F.Click("//input[@id='login-button']",tiempo)
    
    yield page #esta es como un return
    context.close()
    browser.close()
    