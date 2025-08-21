import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random

#playwright codegen https://www.saucedemo.com/

ruta="Imagenes_Globales/Select"
pdf1="C:/Practica_Playwright/18_Unpload_Files/Imagenes/Upload/Playwright_Prueba_Upload.jpg"
#invertir la diagonal, \ por /
def test_Generate(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
   
   
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    #expect(page).to_have_title("Formulario de Ejemplo")
    #page.mouse.wheel(0,800) #scroll hacia abajo
    
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Validar_Url_PaginaWeb("https://www.saucedemo.com/",1)
    F.Validar_Titulo_PaginaWeb("Swag Labs",1)
    
    page.locator('[data-test="username"]').click();
    page.locator('[data-test="username"]').fill('standard_user');
    page.locator('[data-test="username"]').click();
    page.locator('[data-test="password"]').click();
    page.locator('[data-test="password"]').fill('secrert_sauce');
    page.locator('[data-test="login-button"]').click();
    page.locator('[data-test="password"]').click();
    page.locator('[data-test="password"]').fill('secret_sauce');
    page.locator('[data-test="login-button"]').click();
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click();
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click();
    page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click();
    time.sleep(3)

    
    context.close()
    browser.close()
