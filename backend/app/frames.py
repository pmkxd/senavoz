"""
frames.py — Decodificación y preprocesamiento de imágenes.
"""

import numpy as np
import cv2

def decode_jpeg_bytes(b: bytes):
    """Convierte bytes JPEG en un frame OpenCV."""
    arr = np.frombuffer(b, dtype=np.uint8)
    frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    return frame
