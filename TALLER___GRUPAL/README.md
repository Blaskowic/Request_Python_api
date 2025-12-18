# iDROP LOGISTICS — Proyecto de prueba local

Documento de instrucciones y uso del proyecto.

## 🧭 Descripción

Proyecto educativo que simula un pequeño sistema de logística:
- `servidor.py`: aplicación Flask con una página HTML y un endpoint `/api/pedidos`.
- `test_api.py`: prueba que envía un POST al endpoint para crear un pedido.
- `test_web.py`: pruebas UI automáticas con Selenium que interactúan con la página.
- `main.py`: orquesta el servidor y ejecuta las pruebas en secuencia.

> Nota: Este proyecto está pensado para desarrollo local y demostraciones. No se
> recomienda el uso en producción (sin autenticación ni almacenamiento persistente).

---

## ✅ Requisitos

- Python 3.8+
- Google Chrome (para las pruebas con Selenium)

Dependencias Python principales:
- flask
- requests
- selenium
- webdriver-manager

Recomendación para instalar dependencias:

```powershell
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install --upgrade pip
pip install flask requests selenium webdriver-manager
```

> Sugerencia: puedes crear un archivo `requirements.txt` con las dependencias y
> luego ejecutar `pip install -r requirements.txt`.

---

## ▶️ Ejecutar el proyecto

1. Asegúrate de que las dependencias estén instaladas y que Chrome esté disponible.
2. Ejecuta el script principal:

```powershell
python main.py
```

`main.py` realizará lo siguiente:
- Arranca `servidor.py` en un hilo de fondo (puerto 5000).
- Espera brevemente y ejecuta `test_api.probar_api()`.
- Ejecuta `test_web.probar_web()` (abrirá un navegador Chrome real).

Si prefieres ejecutar las pruebas individualmente:

```powershell
python test_api.py
python test_web.py  # requiere Chrome
```

---

## 🔬 Ejemplo de petición manual (cURL)

```bash
curl -X POST http://127.0.0.1:5000/api/pedidos \
  -H "Content-Type: application/json" \
  -d '{"cliente":"Ejemplo S.A.S","producto":"iphone15pm","cantidad":10,"ciudad":"Bogota"}'
```

La respuesta esperada es un JSON con `status: "success"` y código 200.

---

## 📝 Estructura del proyecto

```
main.py
servidor.py
test_api.py
test_web.py
static/
  └─ logo.png
```

- `static/logo.png`: logo que aparece en la página HTML.

---

## ⚠️ Notas y solución de problemas

- Si `test_api.py` falla con error de conexión, verifica que el servidor esté
  en ejecución (`main.py` lo arranca si lo ejecutas todo junto).
- `test_web.py` abre un navegador real y puede requerir interacción si algo
  falla; revisa los logs impresos en consola.
- `webdriver-manager` descarga automáticamente el driver de Chrome compatible,
  pero necesitas tener una versión de Chrome instalada en el sistema.

---

## Autores

- Julian Corredor
- Camila Assia
- Jose Otero

## 🤝 Contribuciones

Si deseas mejorar la documentación, agregar pruebas o convertirlo en un
paquete instalable, abre un issue o PR con tu propuesta.

---

## 🏗️ Generar documentación (Sphinx)

Para generar la documentación HTML localmente con Sphinx:

```powershell
python -m pip install -r requirements-docs.txt
python -m sphinx -b html docs docs/_build/html
# o usar el script para PowerShell
.\build_docs.ps1
```

La salida estará en `docs/_build/html/index.html`.

---

## Licencia

Proyecto de ejemplo. Úsalo libremente en entornos educativos o de demostración.
