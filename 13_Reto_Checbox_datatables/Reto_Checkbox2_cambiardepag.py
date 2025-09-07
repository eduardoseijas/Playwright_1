
import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_Reto_checkboxcambiardepg(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(viewport={'width':1500,'height':800,}) #record_video_dir="VideosCheckboxReto")
    page = context.new_page()
    page.goto("https://datatables.net/extensions/select/examples/checkbox/checkbox.html")
    expect(page).to_have_title("DataTables example - No ordering")
    page.mouse.wheel(0,800)
    time.sleep(1)
    
    for i in range(1,11): 
        page.locator(f"(//input[@aria-label='Select row'])[{i}]").click()
        
        #Colocar limite en el 3er elemento
        if i== 3:
            page.locator("//button[normalize-space()='2']").click()
        if i== 6:
            page.locator("//button[normalize-space()='3']").click()
    time.sleep(2)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    (playwright)
