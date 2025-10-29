"""
ia_stub.py
--------------------------------
Simula el módulo de inteligencia artificial de SeñaVoz.
Traduce gestos detectados en texto (de forma simulada) hasta que
se integre el modelo real de IA.
"""

import random
import time

# Gestos y frases simuladas (se reemplazarán cuando se integre el modelo real)
GESTOS_SIMULADOS = [
    "A", "B", "C", "D", "E", "Hola", "Gracias", "Por favor", "Sí", "No"
]

# Variables de control interno
_ultimo_resultado = None
_tiempo_ultimo_envio = 0


def procesar_frame(frame):
    """
    Procesa un frame de imagen (simulado).

    Args:
        frame (np.ndarray): Frame de imagen recibido desde la ESP32-CAM.

    Returns:
        str | None: Traducción simulada del gesto o None si no hay cambio.
    """
    global _ultimo_resultado, _tiempo_ultimo_envio

    # Simula una inferencia cada cierto intervalo
    if time.time() - _tiempo_ultimo_envio < 1.5:
        return None

    # Genera una “traducción” aleatoria
    resultado = random.choice(GESTOS_SIMULADOS)

    # Evita repeticiones innecesarias
    if resultado == _ultimo_resultado:
        return None

    _ultimo_resultado = resultado
    _tiempo_ultimo_envio = time.time()

    return resultado


def reiniciar_estado():
    """
    Reinicia el estado interno de la simulación (último resultado y tiempo).
    Ideal para reiniciar sesiones o pruebas.
    """
    global _ultimo_resultado, _tiempo_ultimo_envio
    _ultimo_resultado = None
    _tiempo_ultimo_envio = 0


# Demo rápida si se ejecuta directamente
if __name__ == "__main__":
    import cv2
    import numpy as np

    print("🔹 Demo de SeñaVoz - ia_stub.py iniciada...")
    frame_falso = np.zeros((240, 320, 3), dtype=np.uint8)

    for _ in range(10):
        traduccion = procesar_frame(frame_falso)
        if traduccion:
            print(f"Traducción simulada: {traduccion}")
        time.sleep(0.5)
