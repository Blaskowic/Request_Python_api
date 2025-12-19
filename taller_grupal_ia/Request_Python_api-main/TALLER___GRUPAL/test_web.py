"""Pruebas web automatizadas con Selenium para la interfaz local.

Este módulo abre un navegador Chrome (gestor `webdriver-manager`) y realiza
una interacción simple con el formulario de la página principal. Requiere
que el servidor esté en ejecución en `http://127.0.0.1:5000`.

Ejemplo (no ejecutable como doctest localmente):

>>> # Ejecuta la prueba web  # doctest: +SKIP
>>> from test_web import probar_web  # doctest: +SKIP
>>> probar_web()  # doctest: +SKIP
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

__authors__ = ["Julian Corredor", "Camila Assia", "Jose Otero"]

def probar_web() -> None:
    """Automatiza la interacción con la UI y toma evidencia visual.

    Flujo principal:
      1. Se abre Chrome mediante `webdriver-manager`.
      2. Carga la página local y rellenar el formulario de importación.
      3. Pulsa el botón de confirmación y esperar para generar evidencia.

    Nota: este test usa un navegador real y puede necesitar control manual
    (cerrar ventanas) si algo falla; se recomienda ejecutar en un entorno de
    desarrollo con Chrome instalado.
    """
    print("\n" + "="*40)
    print("TEST DE WEB (SELENIUM)")
    print("="*40)
    
    driver = None
    try:
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        
        # 1. Navegación
        driver.get("http://127.0.0.1:5000")
        print("Página cargada.")
        time.sleep(2)

        # 2. Interacción
        print("Llenando formulario de importación...")
        driver.find_element(By.ID, "cliente").send_keys("Camila Imports")
        time.sleep(0.5)
        
        driver.find_element(By.ID, "producto").click()
        driver.find_element(By.XPATH, "//option[@value='iphone15pm']").click()
        time.sleep(0.5)
        
        driver.find_element(By.ID, "cantidad").send_keys("50")
        driver.find_element(By.ID, "direccion").send_keys("Bodega Manga")
        driver.find_element(By.ID, "ciudad").send_keys("Cartagena")
        time.sleep(1)

        # 3. Confirmación
        driver.find_element(By.TAG_NAME, "button").click()
        print("Botón presionado.")
        
        print("\n >>> EVIDENCIA WEB <<<")
        time.sleep(20)

    except Exception as e:
        print(f"Error en Selenium: {e}")
    finally:
        if driver:
            driver.quit()


if __name__ == '__main__':
    probar_web()
