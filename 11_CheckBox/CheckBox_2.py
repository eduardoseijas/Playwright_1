

#OTRA FORMA DE HACER EL EJERCICIO ANTERIOR DE CHECKBOX


import re
import time
from playwright.sync_api import expect, playwright, sync_playwright


#Siempre debe ir test_ y de resto el nombre que quieras para que jale y funcione
def test_checkBox_2(playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=1000)
    context=browser.new_context(record_video_dir="VideosCheckbox")
    page=context.new_page()
    page.set_viewport_size({"width":1500,"height":800})
    page.goto("https://demoqa.com/checkbox")
    expect(page).to_have_title("DEMOQA")
    time.sleep(1)
    
    #primer elemento
    page.locator("[aria-label=Toggle]").click() # tomando comando button del f12 de la pag quitandole las comillas al togle y colocando todo en []
    
    #segundo elemento
    page.locator("[aria-label=Toggle]").nth(1).click() #el .nth() te permite ir haciendo de elemento en elemento q este basado en ese nombre
    
    #tercer elemento
    #page.locator("text=Notes").click()
    
    #otra forma es agarrando el elemento svg
    page.locator("text=NotesCommands >> svg").nth(2).click()
    
    context.close()
    browser.close()