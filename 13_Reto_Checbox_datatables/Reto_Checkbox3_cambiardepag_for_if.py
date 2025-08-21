
import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_Reto_checkbox_for_if(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
    page = context.new_page()
    page.goto("https://datatables.net/extensions/select/examples/checkbox/checkbox.html")
    expect(page).to_have_title("DataTables example - No ordering")
    page.mouse.wheel(0,800)
    time.sleep(1)
    
    for i in range(1,11): 
        page.locator(f"(//input[@aria-label='Select row'])[{i}]").click()
        #Colocar limite en el 3er elemento
        if i== 10:
            page.locator("//button[normalize-space()='2']").click()
            for x in range(1,11):
                page.locator(f"(//input[@aria-label='Select row'])[{x}]").click()
                if x==10:
                    page.locator("//button[normalize-space()='3']").click()
                    for y in range(1,11):
                        page.locator(f"(//input[@aria-label='Select row'])[{y}]").click()
                    page.locator("(//input[@id='dt-search-0'])[1]").fill("Ja")
                    time.sleep(2)
                    page.locator("(//input[@aria-label='Select row'])[3]").click()
                    
                        
                        
    time.sleep(2)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    (playwright)
