"""Módulo servidor: aplicación Flask de ejemplo para el flujo de importaciones.

Proporciona una página HTML con formulario y un endpoint API para crear pedidos.
Endpoints:
  - GET  / -> Página HTML con formulario
  - POST /api/pedidos -> Recibe JSON con datos del pedido y lo almacena en memoria

Advertencia: este servidor está pensado para entorno local/educativo; no es seguro
para producción (no autenticación, almacenamiento en memoria).
"""

# flake8: noqa: E501

from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)
pedidos = []

__authors__ = [
    "Julian Corredor",
    "Camila Assia",
    "Jose Otero",
]


def validar_pedido(datos: dict) -> bool:
    """Valida la estructura mínima esperada para un pedido.

    Comprueba que `datos` sea un diccionario con las claves
    `cliente`, `producto`, `cantidad` y `ciudad` y que `cantidad` sea un
    entero mayor que 0.

    Ejemplos:
    >>> validar_pedido({'cliente':'X','producto':'Y','cantidad':1,'ciudad':'Z'})
    True
    >>> validar_pedido({'cliente':'X','producto':'Y','cantidad':0,'ciudad':'Z'})
    False
    >>> validar_pedido({'cliente':'X','producto':'Y','ciudad':'Z'})  # sin cantidad
    False
    """
    if not isinstance(datos, dict):
        return False
    required = {'cliente', 'producto', 'cantidad', 'ciudad'}
    if not required.issubset(datos.keys()):
        return False
    try:
        cantidad = int(datos.get('cantidad', 0))
        if cantidad <= 0:
            return False
    except Exception:
        return False
    return True

# --- VISTA HTML (Actualizada con Logo UTO) ---
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Importaciones UTO SAS - Logística</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f4; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); width: 380px; text-align: center; border-top: 5px solid #2E7D32; /* Verde corporativo */ }
        
        /* LOGO */
        .logo-img { width: 200px; margin-bottom: 15px; }
        
        h2 { color: #333; margin-bottom: 20px; font-size: 22px; }
        
        input, select { width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }
        
        /* Botón Naranja Corporativo */
        button { width: 100%; background-color: #EF6C00; color: white; padding: 14px; border: none; border-radius: 6px; font-size: 16px; cursor: pointer; font-weight: bold; margin-top: 10px; transition: background 0.3s; }
        button:hover { background-color: #E65100; }
        
        .success { color: #2E7D32; margin-top: 15px; display: none; font-weight: bold; }
        /* Marca de agua de autores */
        .watermark { position: fixed; right: 12px; bottom: 8px; opacity: 0.6; font-size: 12px; color: #333; }
    </style>
</head>
<body>
    <div class="container">
        <img src="/static/logo.png" alt="Logo UTO SAS" class="logo-img">
        
        <h2>Registro de Importación</h2>
        <form id="orderForm">
            <input type="text" id="cliente" placeholder="Nombre del Cliente / Empresa">
            <select id="producto">
                <option value="">Seleccione Producto</option>
                <option value="iphone15pm">iPhone 15 Pro Max</option>
                <option value="macbookair">MacBook Air M3</option>
                <option value="ipadpro">iPad Pro 12.9"</option>
            </select>
            <input type="number" id="cantidad" placeholder="Cantidad (Unidades)">
            <input type="text" id="direccion" placeholder="Dirección de Entrega">
            <input type="text" id="ciudad" placeholder="Ciudad Destino">
            <button type="button" onclick="enviarPedido()">CONFIRMAR ENVÍO</button>
        </form>
        <p id="mensaje" class="success">✅ ¡Solicitud creada exitosamente!</p>
    </div>

    <script>
        function enviarPedido() {
            document.getElementById('mensaje').style.display = 'block';
            document.getElementById('orderForm').style.opacity = '0.5';
        }
    </script>
    <div class="watermark">Autores: Julian Corredor · Camila Assia · Jose Otero</div>
</body>
</html>
"""

@app.route('/')
def home():
    """Renderiza la página HTML principal del sistema.

    Devuelve el HTML con el formulario de registro de importación. No recibe
    parámetros; retorna la respuesta Flask generada por
    `render_template_string(HTML_PAGE)`.
    """
    return render_template_string(HTML_PAGE)


@app.route('/api/pedidos', methods=['POST'])
def crear_pedido():
    """Crea un nuevo pedido desde una petición POST.

    Espera un JSON con la siguiente estructura (ejemplo):
      {
        'cliente': 'Tech Solutions S.A.S',
        'producto': 'MacBook Pro M3',
        'cantidad': 5,
        'ciudad': 'Cartagena'
      }

    Valida el payload mediante `validar_pedido`. Si el payload es inválido
    devuelve `400` con un mensaje de error; en caso válido, añade el pedido a
    la lista global `pedidos` y devuelve un JSON con estado y código HTTP 200.
    """
    datos = request.json
    if not validar_pedido(datos):
        return jsonify({"status": "error", "mensaje": "Payload inválido"}), 400
    pedidos.append(datos)
    print(f"📦 [LOGÍSTICA] Nueva orden UTO: {datos['producto']} -> {datos['cliente']}")
    return jsonify({"status": "success", "mensaje": "Recibido en Centro de Distribución"}), 200


@app.route('/api/autores', methods=['GET'])
def autores() -> tuple:
    """Devuelve la lista de autores del proyecto en formato JSON.

    Responde con un objeto JSON del tipo:
      {"autores": ["Nombre 1", "Nombre 2", ...]}

    Este endpoint es útil para registrar metadatos del proyecto.
    """
    return jsonify({"autores": __authors__}), 200


def run_app() -> None:
    """Inicia la aplicación Flask en el puerto 5000.

    Se utiliza `use_reloader=False` porque el servidor puede iniciarse en un hilo
    (evita arranques múltiples durante desarrollo). No devuelve valor.
    """
    app.run(port=5000, use_reloader=False)


if __name__ == '__main__':
    run_app()
