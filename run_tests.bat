@echo off
setlocal enableextensions

REM === Ruta raíz del repo (donde está este .bat) ===
set ROOT=%~dp0

REM === Crear/activar venv del proyecto ===
if not exist "%ROOT%.venv\Scripts\activate.bat" (
  "C:\Users\Usuario\AppData\Local\Programs\Python\Python313\python.exe" -m venv "%ROOT%.venv"
  call "%ROOT%.venv\Scripts\activate.bat"
  "%ROOT%.venv\Scripts\python.exe" -m pip install -U pip
  "%ROOT%.venv\Scripts\python.exe" -m pip install -r "%ROOT%requirements.txt"
  "%ROOT%.venv\Scripts\python.exe" -m playwright install
) else (
  call "%ROOT%.venv\Scripts\activate.bat"
)

REM === Añadir funciones globales al PYTHONPATH ===
set PYTHONPATH=%ROOT%;%ROOT%AA_Funciones_Globales_Total;%PYTHONPATH%

REM === Ejecutar pytest pasando todos los argumentos recibidos ===
"%ROOT%.venv\Scripts\python.exe" -m pytest %*
