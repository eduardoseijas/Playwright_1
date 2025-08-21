

#Librerias
import re
from playwright.sync_api import expect

def test_uno(page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    
    boton_uno=page.locator("text=Get started")
    expect(boton_uno).to_have_attribute("href","/docs/intro")
    
    boton_uno.click()
    
    #Tomar foto - Funcion screen shot
    
    page.screenshot(path="imagenes/test_uno.png")
    
    #Validando el resultado de la pagina destino
    
    expect(page).to_have_url(re.compile(".*docs/intro"))