import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random
import pytest
import sys #Libreria para informacion directamente del sistema operativo

tiempo=1.6
ruta="Imagenes_Globales/Select"
pdf1="C:/Practica_Playwright/18_Unpload_Files/Imagenes/Upload/Playwright_Prueba_Upload.jpg"
#invertir la diagonal, \ por /
Url="https://testpages.eviltester.com/styled/basic-html-form-test.html"

@pytest.fixture(scope="function") # entre las comillas puedes usar tambien "session"
def set_up(playwright)-> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
    
    #Iniciar Trace Viewer
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto(Url)
    page.set_default_timeout(5000)
    
    yield page #esta es como un return
    context.close()
    browser.close()
    