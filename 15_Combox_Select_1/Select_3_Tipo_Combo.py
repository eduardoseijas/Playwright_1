import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion


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
    F.Validar_Titulo_PaginaWeb("Formulario de Ejemplo",2) #hace lo mismo que expect(page).to_have_title("Formulario de Ejemplo"),es la funcion
    F.Validar_Url_PaginaWeb("https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html",1)
    F.Esperar(1)
    F.Scroll_x_y(0,400)
    
    #Combo Value
    F.Combo_Value("//select[@id='comboBox1']","3",2)
    F.Combo_Value_img("//select[@id='comboBox1']","4",ruta+"Combovalue.png",2)
    
    #Combo Label
    F.Combo_label("//select[@id='comboBox2']","Valor 3",2)
    F.Combo_label_img("//select[@id='comboBox2']","Valor 2",ruta+"Comobolabel.png",2)
    
    #Click
    F.Click("//button[normalize-space()='Enviar']",2)
    
    #Confirmacion
    F.Validar_Texto("//small[@id='error3']","Por favor, seleccione un sistema operativo.",2)
    F.Validar_Texto_img("//small[@id='error3']","Por favor, seleccione un sistema operativo.",ruta+"Respuesta.png",2)
    
