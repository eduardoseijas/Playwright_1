import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random
import pytest
import sys #Libreria para informacion directamente del sistema operativo

#playwright codegen https://www.saucedemo.com/
tiempo=0.3
ruta="Imagenes_Globales/Select"
pdf1="C:/Practica_Playwright/18_Unpload_Files/Imagenes/Upload/Playwright_Prueba_Upload.jpg"
#invertir la diagonal, \ por /
def test_Inicio_1(set_up_session) -> None:
    page=set_up_session
    F=Funciones_Globales_Total(page)
    F.Validar_Titulo_PaginaWeb("Swag Labs")
    
def test_Seleccion_de_Articulo(set_up_session) -> None:
    page=set_up_session
    F=Funciones_Globales_Total(page)
    F.Validar_Titulo_PaginaWeb("Swag Labs")
    
    F.Click("//button[@id='add-to-cart-sauce-labs-backpack']",tiempo)
    F.Click("//button[@id='add-to-cart-sauce-labs-bike-light']",tiempo)
    F.Esperar(2)
    

def test_Ejecucion_del_Menu(set_up_session) -> None:
    page=set_up_session
    F=Funciones_Globales_Total(page)
    F.Click("//button[@id='react-burger-menu-btn']",tiempo)
    F.Click("//button[@id='react-burger-cross-btn']",tiempo)
    F.Click("//a[@class='shopping_cart_link']",tiempo)
    F.Esperar(2)
    
def test_Seleccionamos_Los_Articulos(set_up_session) -> None:
    page=set_up_session
    F=Funciones_Globales_Total(page)
    F.Click("//button[@id='checkout']",tiempo)
    
def test_Cargar_Los_Datos_Del_Comprador(set_up_session) -> None:
    page=set_up_session
    F=Funciones_Globales_Total(page)
    F.Texto("//input[@id='first-name']","Eduardo",tiempo)
    F.Texto("//input[@id='last-name']","Seijas",tiempo)
    F.Texto("//input[@id='postal-code']","45600",tiempo)
    
def test_Completamos_La_Compra(set_up_session) -> None:
    page=set_up_session
    F=Funciones_Globales_Total(page)
    F.Click("//input[@id='continue']",tiempo)
    F.Scroll_x_y(0,800)
    F.Click("//button[@id='finish']",tiempo)
    
    
def test_Regresar_A_La_Pantalla_De_Seleccion_De_Articulos(set_up_session) -> None:
    page=set_up_session
    F=Funciones_Globales_Total(page)
    F.Click("//button[@id='back-to-products']",tiempo)
    F.Esperar(2)
    
    
    
    
    
    
    
    
    
    
