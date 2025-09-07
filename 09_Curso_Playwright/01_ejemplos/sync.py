#sync es sincronico

#Librerias
import asyncio
from logging import handlers
from playwright.sync_api import sync_playwright #a diferencia del otro no olvidar que es sync

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False, slow_mo=3000)
    page=browser.new_page()
    page.goto("https://demoqa.com/text-box")#url
    print(page.title())
    browser.close()
    
