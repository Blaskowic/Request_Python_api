"""Módulo de pruebas de API para el servidor Flask local.

Contiene una prueba sencilla que envía un POST a `/api/pedidos` y valida que
la respuesta tenga código 200. Este test asume que el servidor está
corriendo en `http://127.0.0.1:5000` antes de ejecutarlo.

Ejemplo de uso (no ejecutable como doctest localmente):

# Este ejemplo realiza una petición real al servidor (necesita servidor en marcha)
# import requests  # doctest: +SKIP
# requests.post(
#     "http://127.0.0.1:5000/api/pedidos",
#     json={"cliente": "X", "producto": "Y", "cantidad": 1, "ciudad": "Z"},
# )  # doctest: +SKIP
"""

import requests
import time

__authors__ = ["Julian Corredor", "Camila Assia", "Jose Otero"]

def probar_api() -> None:
    """Envía un POST de prueba a `/api/pedidos` y verifica el código HTTP.

    No recibe parámetros. Imprime por consola el estado del test. Se
    recomienda ejecutar este script con el servidor en marcha.
    """
    print("\n" + "="*40)
    print("📡 [MÓDULO 1] TEST DE API (BACKEND)")
    print("="*40)
    
    url = "http://127.0.0.1:5000/api/pedidos"
    payload = {
        "cliente": "Tech Solutions S.A.S",
        "producto": "MacBook Pro M3",
        "cantidad": 5,
        "ciudad": "Cartagena"
    }

    try:
        print(f"Enviando datos a: {url}")
        respuesta = requests.post(url, json=payload)
        
        if respuesta.status_code == 200:
            print("✅ [PASS] Estado 200 OK recibido.")
            print(f"   Respuesta JSON: {respuesta.json()}")
        else:
            print(f"❌ [FAIL] Error {respuesta.status_code}")
            
    except Exception as e:
        print(f"❌ [ERROR CRÍTICO] No hay conexión con la API: {e}")

    print("\n📸  >>> FOTO EVIDENCIA API (5 seg) <<<")
    time.sleep(5)

if __name__ == '__main__':
    probar_api()