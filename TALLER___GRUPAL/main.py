"""Script principal para el sistema de pruebas de iDROP LOGISTICS.

Este módulo orquesta el arranque del servidor Flask y la ejecución
secuencial de las pruebas de API y web (Selenium). Diseñado para
uso ad-hoc en entorno local de desarrollo.
"""

import threading
import time
import sys
import subprocess

# Importamos nuestros propios módulos
# (Asegúrate de que todos los archivos estén en la misma carpeta)
import servidor
import test_api
import test_web

__authors__ = ["Julian Corredor", "Camila Assia", "Jose Otero"]

# Auto-reparación de librerías (Por si acaso)
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
    """Arranca el servidor y ejecuta las pruebas de API y web.

    Flujo:
      1. Levantar el servidor Flask en un hilo daemon para que se ejecute en
         background sin bloquear el hilo principal.
      2. Esperar brevemente para dar tiempo a que el servidor inicie.
      3. Ejecutar `test_api.probar_api()` y `test_web.probar_web()` en
         secuencia.

    No tiene parámetros y no devuelve valor. Los efectos secundarios incluyen:
    - Impresión de mensajes de progreso en stdout.
    - Inicio de un hilo que ejecuta el servidor Flask (puede persistir
      hasta que termine la ejecución).
    - Posibles excepciones si las dependencias faltan o si las pruebas fallan.
    """
    print("🚀 INICIANDO SISTEMA MODULAR - iDROP LOGISTICS")
    
    # 1. Arrancar el Servidor (Módulo servidor.py) en un hilo aparte
    hilo_server = threading.Thread(target=servidor.run_app)
    hilo_server.daemon = True
    hilo_server.start()
    
    print("⏳ Esperando carga del servidor (3 seg)...")
    time.sleep(3)

    # 2. Ejecutar Prueba de API (Módulo test_api.py)
    test_api.probar_api()

    # 3. Ejecutar Prueba Web (Módulo test_web.py)
    test_web.probar_web()

    print("\n🏁 TODAS LAS PRUEBAS FINALIZADAS EXITOSAMENTE")


if __name__ == '__main__':
    ejecutar_todo()
