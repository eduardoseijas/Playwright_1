import re
import time
from playwright.sync_api import expect


def test_reto_playwright_input(page):
    page.goto("https://demoqa.com/")
    expect(page).to_have_title("DEMOQA")
    
    #boton_uno
    #btn_uno=page.locator("text=Elements").click()
    page.locator("text=Elements").click()
    page.screenshot(path="Imagenes/Reto_1_boton_1_click.png")
    #btn_uno.click()
    #validar url
    expect(page).to_have_url(re.compile(".*elements")) #validando url
    #page.screenshot(path="Imagenes/Reto_1_pag_menu.png")
    page.locator("text=Text Box").click()
    page.screenshot(path="Imagenes/Reto_1_boton_1_TextBox.png")
    #validar url
    expect(page).to_have_url(re.compile(".*text-box")) #validando url
    
    #Primer texto a rellenar, campo nombre con el # es para ID por ejemplo #userName si fuera CSS es un . ejemplo .userName
    page.locator("#userName").fill("Eduardo Seijas") #comando .fill es para rellenar
    page.screenshot(path="Imagenes/Reto_1_boton_1_Text_nombre.png")
    
    
    #rellenar el campo del correo
    page.locator("//input[@id='userEmail']").fill("eduardoseijas@hotmail.com") #aqui use el XPATH
    page.screenshot(path="Imagenes/Reto_1_boton_1_Text_email.png")
    
    
    #Rellenar el campo de direccion/comentario
    page.locator("//textarea[@id='currentAddress']").fill("Esto es una prueba con el framework playwright") #aqui use el XPATH
    page.screenshot(path="Imagenes/Reto_1_boton_1_Text_comentario.png")
    
    
    #Rellenar el campo de direccion 2
    page.locator("//textarea[@id='permanentAddress']").fill("España - Toledo") #aqui use el XPATH
    page.screenshot(path="Imagenes/Reto_1_boton_1_Text_direccion2.png")
    time.sleep(2)
    
    