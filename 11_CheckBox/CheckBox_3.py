
#OTRA FORMA DE HACER EL EJERCICIO ANTERIOR DE CHECKBOX

#nuevo comando playwright codegen https://demoqa.com/checkbox


import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_checkbox3(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context=browser.new_context(record_video_dir="VideosCheckbox")
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/checkbox")
    page.get_by_role("button", name="Toggle").click()
    page.get_by_role("listitem").filter(has_text=re.compile(r"^Desktop$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Commands").get_by_role("img").first.click()
    page.get_by_role("listitem").filter(has_text=re.compile(r"^Documents$")).get_by_label("Toggle").click()
    page.get_by_role("listitem").filter(has_text=re.compile(r"^WorkSpace$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Angular").get_by_role("img").first.click()
    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    (playwright)
