import re
import time
from playwright.sync_api import expect, playwright, sync_playwright

#pytest --slowmo 1000 --headed Reto_input2_Playwright.py

#Otra forma de crear la funcion

def test_reto_playwright_input3(playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=500)
    context=browser.new_context()
    #context=browser.new_context(
       # viewport={'width':1500, 'height':800}  #esta es para que la pantalla se agrande
    #)
    
    time.sleep(2)
    context=browser.new_context(record_video_dir="Video_reto3") #para grabar videos
    page=context.new_page()
    page.set_viewport_size({"width": 1500, "height": 800}) #otra forma para agrandar la pantalla
    page.goto("https://validaciones.rodrigovillanueva.com.mx/index.html")
    expect(page).to_have_title("Formulario de Ejemplo")
    
    #tiempo de esèra
    page.set_default_timeout(5000) #1000 son 5 segundos, tiempo global para encontrar un elemento
    
    #comenzamos a llenar los datos
    page.locator("//input[@id='nombre']").fill("Eduardo Alejandro") #Tome por valor XPATH
    page.screenshot(path="Imagenes_input2/nombre.png")
    
    #Aserts o Validaciones
    apellidos=page.locator("#apellidos")
    #Que el elemento sea visible .to_be_visible
    expect(apellidos).to_be_visible() 
    page.locator("#apellidos").fill("Seijas Pacheco") #tome x valor ID
    
    
    #Que el elemento este disponible .to_be_enabled()
    tlf=page.locator("#tel")
    expect(tlf).to_be_enabled()
    #Que el campo este vacio .to_be_empty
    expect(tlf).to_be_empty()
    page.locator("#tel").fill("6748331079") #tome por valor ID
    time.sleep(1) #time forzado
    
    #Que contiene el ID
    email=page.locator("//input[@id='email']")
    expect(email).to_have_id("email") #para validar NO es como cuando el selector, no se coloca el #
    page.locator("//input[@id='email']").fill("eduardoseijas@hotmail.com") #XPATH
    
    page.locator("//input[@id='direccion']").fill("prueba de playwright") #XPATH  
    
    #Validar si esta visible
    #btn=page.locator("//button[normalize-space()='Enviar']")  
    #expect(btn).to_be_visible()
    btn=page.is_visible("//button[normalize-space()='Enviar']")
    print(btn)
    if btn:
        print("Entro al true, es decir lo encontro")
        page.locator("//button[normalize-space()='Enviar']").click()
    else:
        print("No se encontro el boton")
        print(btn)
    
    expect(page).to_have_url(re.compile(".*index.html")) #para validar la url .* y la ultima parte del enlace de la url desde el ultimo /
    time.sleep(2) #time forzado
    
    gracias=page.locator("#flashMessage")
    expect(gracias).to_contain_text("El formulario se ha enviado correctamente.")
    
    #Cerrar Context y Navegador
    context.close()
    browser.close()
    