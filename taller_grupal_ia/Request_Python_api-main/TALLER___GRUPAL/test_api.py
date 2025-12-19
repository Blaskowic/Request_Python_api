"""Comprobación rápida y manual de la API del servidor local.

Este script envía una petición POST de ejemplo a `/api/pedidos` en
`http://127.0.0.1:5000` y muestra en consola un resultado amigable.

Diseñado para uso manual por desarrolladores: arranca el servidor
local y luego ejecuta este archivo para verificar que la ruta responde correctamente.

Nota: no es un test automático para CI, sino una herramienta de
verificación sencilla y directa durante el desarrollo.
"""

import requests
import time

__authors__ = ["Julian Corredor", "Camila Assia", "Jose Otero"]


def probar_api() -> None:
    """Enviar un pedido de ejemplo y mostrar el resultado de forma clara.

    La función no devuelve nada; imprime mensajes útiles para entender
    si la API contestó correctamente o qué pasos seguir si hubo un fallo.
    """
    print("\n" + "=" * 40)
    print("[MÓDULO 1] Prueba rápida de la API (backend)")
    print("=" * 40)

    url = "http://127.0.0.1:5000/api/pedidos"
    payload = {
        "cliente": "Tech Solutions S.A.S",
        "producto": "MacBook Pro M3",
        "cantidad": 5,
        "ciudad": "Cartagena",
    }

    try:
        print(f"Probando conexión con la API en: {url}")
        respuesta = requests.post(url, json=payload)

        if respuesta.status_code == 200:
            print("[OK] La API respondió 200 — petición exitosa.")
            try:
                print("  Respuesta (JSON):", respuesta.json())
            except Exception:
                print("  Respuesta recibida, pero no es JSON válido.")
        else:
            print(f"[ERROR] Código {respuesta.status_code} recibido.")
            print("  Sugerencia: revisa los logs del servidor para más detalles.")

    except Exception as e:
        print("[CONEXIÓN FALLIDA] No se pudo conectar con la API.")
        print("  ¿Está el servidor local en marcha? Puedes ejecutar:")
        print("    python servidor.py")
        print("  y volver a intentar. Detalle del error:", e)

    print("\nMostrando evidencia breve (pausa de 5 segundos)...")
    time.sleep(5)


if __name__ == "__main__":
    probar_api()