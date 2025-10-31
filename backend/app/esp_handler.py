"""
esp_handler.py
--------------------------------
Gestión de la conexión WebSocket con la ESP32-CAM y registro de todas las acciones del Arduino.
"""

import json
from datetime import datetime
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.ws_manager import ConnectionManager
from app.frames import decode_jpeg_bytes
from app.inference import infer_from_frame

router = APIRouter()
manager = ConnectionManager()

# ───────────────────────────────
# Logs de acciones del Arduino
# ───────────────────────────────
arduino_logs = []

def log_arduino_event(device_id, event_type, data):
    """Registra un evento del Arduino con timestamp."""
    arduino_logs.append({
        "timestamp": datetime.utcnow().isoformat(),
        "device_id": device_id,
        "event": event_type,
        "data": data
    })
    print(f"[LOG] {device_id} | {event_type}: {data}")


# ───────────────────────────────
# WebSocket ESP32-CAM
# ───────────────────────────────
@router.websocket("/ws/esp32/{device_id}")
async def esp32_ws(websocket: WebSocket, device_id: str):
    """
    Canal WebSocket entre la ESP32-CAM y el backend.
    Recibe frames o mensajes de texto y los registra.
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

                # Registrar la acción
                log_arduino_event(device_id, "frame_received", {"label": label, "confidence": conf})

            # Si el mensaje es texto → log simple
            elif "text" in msg:
                print(f"[ESP32] Mensaje texto: {msg['text']}")
                log_arduino_event(device_id, "text_message", {"text": msg["text"]})

    except WebSocketDisconnect:
        await manager.disconnect_esp(device_id)
        print(f"⚠️ ESP32 {device_id} desconectada.")


# ───────────────────────────────
# Endpoint REST para consultar logs
# ───────────────────────────────
@router.get("/logs")
def get_logs():
    """Devuelve todos los logs del Arduino registrados hasta el momento."""
    return {"logs": arduino_logs}
