import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random

ruta="Imagenes_Globales/Select"

def test_select1(playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={'width':1450,'height':800,}) #record_video_dir="VideosCheckboxReto")
    page = context.new_page()
    page.goto("https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html")
    #expect(page).to_have_title("Formulario de Ejemplo")
    #page.mouse.wheel(0,800)
    
#creando nuestro Objeto de tipo Funciones_Globales
    F=Funciones_Globales_Total(page)
    F.Validar_Url_PaginaWeb("https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html",1)
    F.Validar_Titulo_PaginaWeb("Formulario de Ejemplo")
    F.Esperar(1)
    F.Scroll_x_y(0,400)
    
    #Combox 1
    F.Combo_Value("//select[@id='comboBox1']","3",2)
    
    #Combox 2
    F.Combo_label("//select[@id='comboBox2']","Valor 4",2)
    
    #Sistema Operativo
    F.Combo_Value("//select[@id='os']","Linux",2)
    
    #Metodo random
    numA=random.sample(range(1,4),1)
    print(numA)
    #F.Combo_label("//select[@id='version']",)
    if numA[0]==1:
        F.Combo_label("//select[@id='version']","Ubuntu",2)
        print("Es el uno")
    elif numA[0]==2:
        F.Combo_label("//select[@id='version']","Fedora",2)
        print("Es el dos")
    elif numA[0]==3:
        F.Combo_label("//select[@id='version']","Debian",2)
        print("Es el tres")
        
        