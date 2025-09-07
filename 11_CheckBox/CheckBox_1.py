import re
import time
from playwright.sync_api import expect, playwright, sync_playwright


#Siempre debe ir test_ y de resto el nombre que quieras para que jale y funcione
def test_checkBox_1(playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=1000)
    context=browser.new_context(record_video_dir="VideosCheckbox")
    page=context.new_page()
    page.set_viewport_size({"width":1500,"height":800})
    page.goto("https://demoqa.com/checkbox")
    expect(page).to_have_title("DEMOQA")
    time.sleep(1)
    
    check1=page.locator("//button[@title='Toggle']//*[name()='svg']")
    expect(check1).to_be_visible()
    check1.click()
    check2=page.locator("(//button[@title='Toggle'])[2]")
    check2.click()
    
    clickcheck=page.locator("(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[4]")
    #otra opcion es por texto que podria ser page.locator("text=commands") despues del = el nombre del texto q tenga ese selector, en este caso es commands
    clickcheck.click()
    
    #Cerrar Context y Navegador
    context.close()
    browser.close()