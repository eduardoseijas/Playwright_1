import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from Funciones_Globales import Funciones_Globales  #para llamar las funciones viene de la carpeta y funcion
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion, esta es una global que cree

def test_select1(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
    page = context.new_page()
    page.goto("https://testpages.eviltester.com/styled/basic-html-form-test.html")
    expect(page).to_have_title("HTML Form Elements")
    #page.mouse.wheel(0,800)
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales(page)
    F.Esperar()
    F.Scroll_x_y(0,400)
    
    context.close()
    browser.close()