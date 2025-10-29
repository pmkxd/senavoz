"""
inference.py
--------------------------------
Módulo de inferencia del proyecto **SeñaVoz**.

Actualmente, esta versión simula el reconocimiento de señas
de la mano usando datos falsos. En una futura integración,
este módulo conectará con un modelo real de visión por computadora
para traducir gestos en texto.

Se utiliza junto con `esp_handler.py` para procesar frames recibidos
desde una cámara ESP32-CAM.
"""

from fastapi import APIRouter
import random

router = APIRouter()


def infer_from_frame(frame):
    """
    Simula la inferencia sobre un frame de video.

    Args:
        frame (np.ndarray): Imagen proveniente de la cámara (simulada).

    Returns:
        tuple[str, float]: Letra o palabra detectada y su nivel de confianza.
    """
    etiquetas = ["A", "E", "I", "O", "U", "Hola", "Gracias", "Sí", "No"]
    etiqueta = random.choice(etiquetas)
    confianza = round(random.uniform(0.8, 0.99), 2)
    return etiqueta, confianza
