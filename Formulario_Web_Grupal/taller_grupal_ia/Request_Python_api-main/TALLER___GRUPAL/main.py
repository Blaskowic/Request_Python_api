"""Script principal para el sistema de pruebas de IMPORTACIONES UTO SAS.

Este módulo orquesta el arranque del servidor Flask y la ejecución
secuencial de las pruebas de API y web (Selenium). Diseñado para
uso ad-hoc en entorno local de desarrollo.
"""

import threading
import time
import sys
import subprocess

# Importamos nuestros propios módulos y nos aseguramos de que todos los archivos estén en la misma carpeta
import servidor
import test_api
import test_web

__authors__ = ["Julian Corredor", "Camila Assia", "Jose Otero"]

# Hacemos Auto-reparación de librerías (Por si acaso)
try:
    import requests  # noqa: F401
    from selenium import webdriver  # noqa: F401
except ImportError:
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "flask",
            "requests",
            "selenium",
            "webdriver-manager",
        ]
    )


def ejecutar_todo() -> None:
    """Se arranca el servidor y ejecuta las pruebas de API y web.

    Flujo:
      1. Se Levanta el servidor Flask en un hilo daemon para que se ejecute en
         background sin bloquear el hilo principal.
      2. Esperamos brevemente para dar tiempo a que el servidor inicie.
      3. Ejecuta test api y test web en secuencia.

    No tiene parámetros y no devuelve valor. Los efectos secundarios incluyen:
    - Impresión de mensajes de progreso en stdout.
    - Inicio de un hilo que ejecuta el servidor Flask (puede persistir
      hasta que termine la ejecución).
    - Posibles excepciones si las dependencias faltan o si las pruebas fallan.
    """
    print("INICIANDO SISTEMA - Importaciones UTO SAS")
    
    # Arranca el Servidor 
    hilo_server = threading.Thread(target=servidor.run_app)
    hilo_server.daemon = True
    hilo_server.start()
    
    print("Esperando servidor...")
    time.sleep(3)

    # Ejecutamos Prueba de API 
    test_api.probar_api()

    # Ejecutamos Prueba Web
    test_web.probar_web()

    print("\nTODAS LAS PRUEBAS FINALIZADAS EXITOSAMENTE")


if __name__ == '__main__':
    ejecutar_todo()
