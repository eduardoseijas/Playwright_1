import re
import time
from playwright.sync_api import Page, Playwright, sync_playwright, expect

class Funciones_Globales:
    #El __init__() es el constructor, iniciador
    def __init__(self,page):
        self.page=page
        
        
    def Esperar(self,tiempo=0.5): #les puedo colocar un valor por default al tiempo q en este caso es 0.5
        time.sleep(tiempo)
    
    def Scroll_x_y(self,x,y,tiempo=0.5): #les puedo colocar un valor por default al tiempo q en este caso es 0.5
        self.page.mouse.wheel(x,y)
        time.sleep(tiempo)
    
    def Texto(self,selector,texto,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()
        t.fill(texto)
        time.sleep(tiempo)
        
    def Texto_img(self,selector,texto,ruta,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()
        t.fill(texto)
        self.page.screenshot(path=ruta)
        time.sleep(tiempo)
        
    def Click(self,selector,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        time.sleep(tiempo)
        
    def Click_img(self,selector,ruta,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        self.page.screenshot(path=ruta)
        time.sleep(tiempo)
        
    def Combo_Value(self,selector,valor,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(valor)
        time.sleep(tiempo)
        
    def Combo_Value_img(self,selector,valor,ruta,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(valor)
        self.page.screenshot(path=ruta)
        time.sleep(tiempo)
        
    def Combo_label(self,selector,valor,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(label=valor)
        time.sleep(tiempo)
        
    def Combo_label_img(self,selector,valor,ruta,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(label=valor)
        self.page.screenshot(path=ruta)
        time.sleep(tiempo)
        
    def Validar_Titulo_PaginaWeb(self,texto,tiempo=0.5):
        expect(self.page).to_have_title(texto)
        time.sleep(tiempo)
        
    def Validar_Url_PaginaWeb(self,texto,tiempo=0.5):
        expect(self.page).to_have_url(re.compile(texto))
        time.sleep(tiempo)

    def Validar_Texto(self,selector,texto,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_contain_text(texto)
        time.sleep(tiempo)
        
    def Validar_Texto_img(self,selector,texto,ruta,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_contain_text(texto)
        self.page.screenshot(path=ruta)
        time.sleep(tiempo)

    def Mouse_X_Y(self,x,y,tiempo=0.5):
        self.page.mouse.click(x,y)
        time.sleep(tiempo)
    
    def Tab(self,tiempo=0.5):
        self.page.keyboard.press("Tab")
        time.sleep(tiempo)
        
    def Upload_Files(self,selector,archivo,tiempo=0.5):
        self.page.locator(selector).set_input_files(archivo)
        time.sleep(tiempo)
        
    def Upload_Files_img(self,selector,archivo,ruta,tiempo=0.5):
        self.page.locator(selector).set_input_files(archivo)
        self.page.screenshot(path=ruta)
        time.sleep(tiempo)
        
    def Upload_Files_Remover(self,selector,archivo,tiempo=0.5):
        self.page.locator(selector).set_input_files([])
        time.sleep(tiempo)
        
    def Clear(self,selector,tiempo=0.5):
        self.page.locator(selector).clear()
        time.sleep(tiempo)