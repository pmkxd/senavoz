"""
esp_handler.py
--------------------------------
Módulo encargado de gestionar la conexión WebSocket con la ESP32-CAM.

Recibe frames JPEG desde el dispositivo, los decodifica y los envía
al módulo de inferencia (simulado o real) para obtener una traducción
del gesto detectado.

Forma parte del backend del proyecto **SeñaVoz**.
"""

import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.ws_manager import ConnectionManager
from app.frames import decode_jpeg_bytes
from app.inference import infer_from_frame

router = APIRouter()
manager = ConnectionManager()


@router.websocket("/ws/esp32/{device_id}")
async def esp32_ws(websocket: WebSocket, device_id: str):
    """
    Canal WebSocket entre la ESP32-CAM y el backend.

    Args:
        websocket (WebSocket): Conexión WebSocket activa.
        device_id (str): Identificador único del dispositivo.

    Función:
        - Recibe frames JPEG desde la ESP32-CAM.
        - Decodifica los bytes a imagen (usando OpenCV).
        - Pasa la imagen al módulo de inferencia.
        - Envía la traducción resultante a los clientes conectados.
    """
    await manager.connect_esp(device_id, websocket)
    try:
        while True:
            msg = await websocket.receive()

            # Si el mensaje contiene bytes → frame de cámara
            if "bytes" in msg:
                frame_bytes = msg["bytes"]
                frame = decode_jpeg_bytes(frame_bytes)
                label, conf = infer_from_frame(frame)

                payload = {"type": "translation", "text": label, "confidence": conf}
                await manager.broadcast_translation(device_id, payload)

            # Si el mensaje es texto → log simple
            elif "text" in msg:
                print(f"[ESP32] Mensaje texto: {msg['text']}")

    except WebSocketDisconnect:
        await manager.disconnect_esp(device_id)
        print(f"⚠️ ESP32 {device_id} desconectada.")
