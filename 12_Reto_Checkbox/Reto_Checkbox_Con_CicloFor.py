
import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_Reto_checkbox1(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(viewport={'width':1500,'height':800,}) #record_video_dir="VideosCheckboxReto")
    page = context.new_page()
    page.goto("https://validaciones.rodrigovillanueva.com.mx/Radios_Ok.html")
    expect(page).to_have_title("Formulario de Ejemplo")
    time.sleep(2)
    
    #Nombre
    page.locator("(//input[@id='campo1'])[1]").fill("Eduardo A. Seijas")
    
    #Telefono
    page.locator("#campo2").fill("1234567890")
    
    #hacer scroll en la pag web
    page.mouse.wheel(0,300)
    
    #seleccionar una opcion
    page.locator("#opcion2").click()
    
    #ESTA ES UNA 3RA FORMA DE HACER EL TIPO DE SELECCION
    opciones=["#opcionA","#opcionB"]
    for opcion in opciones:  #creo una variable que se llame opciones, con los ID de ese selector para ubicarlos
        page.check(opcion)
   
 
    #expect(page).to_have_url(re.compile(".*Radios_Ok.htmll"))
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    (playwright)
