


#nuevo comando playwright codegen https://validaciones.rodrigovillanueva.com.mx/Radios_Ok.html


import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_Reto_checkboxdatatables(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(viewport={'width':1500,'height':800,}) #record_video_dir="VideosCheckboxReto")
    page = context.new_page()
    page.goto("https://datatables.net/extensions/select/examples/checkbox/checkbox.html")
    expect(page).to_have_title("DataTables example - No ordering")
    page.mouse.wheel(0,800)
    time.sleep(1)
    
    for i in range(1,11, 2): #en un for el range tiene 3 opciones, los primeros 2 valores el rango, por ejemplo aqui vamos del 1 al 11, te saldran hasta el numero 10, el 3ro es de cuanto ir incrementado
        page.locator(f"(//input[@aria-label='Select row'])[{i}]").click()
    time.sleep(2)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    (playwright)
