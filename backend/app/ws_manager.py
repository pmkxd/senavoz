"""
ws_manager.py
------------------------------------
Administrador de conexiones WebSocket para el backend **SeñaVoz**.

Este módulo gestiona la comunicación en tiempo real entre:
- Dispositivos ESP32-CAM (emisores de video y datos)
- Clientes web o móviles (receptores de las traducciones)

Implementa un patrón de publicación/suscripción (pub-sub),
permitiendo que varios clientes escuchen simultáneamente
las traducciones generadas por un mismo dispositivo.
"""

import json


class ConnectionManager:
    def __init__(self):
        # Diccionarios para manejar conexiones activas
        self.esp_connections = {}     # {device_id: websocket}
        self.client_connections = {}  # {user_id: websocket}
        self.subscriptions = {}       # {device_id: [user_ids]}

    # ───────────────────────────────
    # Conexión y desconexión ESP32
    # ───────────────────────────────
    async def connect_esp(self, device_id, websocket):
        """Registra una nueva conexión desde una ESP32."""
        await websocket.accept()
        self.esp_connections[device_id] = websocket
        self.subscriptions.setdefault(device_id, [])
        print(f"[ESP32] ✅ Conectado: {device_id}")

    async def disconnect_esp(self, device_id):
        """Elimina la conexión de una ESP32 desconectada."""
        self.esp_connections.pop(device_id, None)
        self.subscriptions.pop(device_id, None)
        print(f"[ESP32] ❌ Desconectado: {device_id}")

    # ───────────────────────────────
    # Conexión y desconexión Cliente
    # ───────────────────────────────
    async def connect_client(self, user_id, websocket):
        """Registra una conexión de cliente (web/móvil)."""
        await websocket.accept()
        self.client_connections[user_id] = websocket
        print(f"[CLIENTE] ✅ Conectado: {user_id}")

    async def disconnect_client(self, user_id):
        """Elimina una conexión de cliente y lo desuscribe."""
        self.client_connections.pop(user_id, None)
        for subs in self.subscriptions.values():
            if user_id in subs:
                subs.remove(user_id)
        print(f"[CLIENTE] ❌ Desconectado: {user_id}")

    # ───────────────────────────────
    # Suscripciones y transmisión
    # ───────────────────────────────
    async def subscribe(self, user_id, device_id):
        """Suscribe un cliente a un dispositivo ESP32 para recibir traducciones."""
        self.subscriptions.setdefault(device_id, [])
        if user_id not in self.subscriptions[device_id]:
            self.subscriptions[device_id].append(user_id)
        print(f"[SUSCRIPCIÓN] 🔄 {user_id} ahora escucha a {device_id}")

    async def broadcast_translation(self, device_id, payload):
        """
        Envía una traducción a todos los clientes suscritos al dispositivo indicado.

        Args:
            device_id (str): ID del dispositivo origen.
            payload (dict): Datos de la traducción (texto, confianza, etc.).
        """
        users = self.subscriptions.get(device_id, [])
        for uid in users:
            ws = self.client_connections.get(uid)
            if ws:
                try:
                    await ws.send_text(json.dumps(payload))
                except Exception as e:
                    print(f"[ERROR] Falló el envío a {uid}: {e}")
