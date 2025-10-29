"""
client_handler.py
--------------------------------
Canal WebSocket para los clientes (web o móvil).

Los clientes se conectan al backend y se suscriben a un dispositivo ESP32-CAM.
De esta forma reciben en tiempo real las traducciones generadas por el módulo
de inteligencia artificial del proyecto **SeñaVoz**.
"""

import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.ws_manager import ConnectionManager

router = APIRouter()
manager = ConnectionManager()


@router.websocket("/ws/client/{user_id}")
async def client_ws(websocket: WebSocket, user_id: str):
    """
    Canal WebSocket para comunicación en tiempo real con el cliente.

    Args:
        websocket (WebSocket): Conexión WebSocket activa.
        user_id (str): Identificador del usuario o sesión.

    Función:
        - Establece la conexión con el cliente.
        - Escucha mensajes JSON desde el frontend.
        - Maneja suscripción del cliente a un dispositivo ESP32.
        - En caso de desconexión, limpia la sesión.
    """
    await manager.connect_client(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)

            if msg.get("type") == "subscribe":
                await manager.subscribe(user_id, msg["device_id"])

    except WebSocketDisconnect:
        await manager.disconnect_client(user_id)
        print(f"⚠️ Cliente {user_id} desconectado.")
