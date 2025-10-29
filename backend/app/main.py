"""
main.py — Punto de entrada del backend de SeñaVoz.
Inicializa FastAPI, registra las rutas WebSocket y REST,
y arranca el servidor principal que recibe y procesa las señas
enviadas por la ESP32-CAM o el frontend.
Se ejecuta con: uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
"""

from fastapi import FastAPI
from app.esp_handler import router as esp_router
from app.client_handler import router as client_router
from app.inference import router as inference_router

# Inicializa la aplicación FastAPI con el nombre oficial del proyecto
app = FastAPI(title="Backend SeñaVoz - Traducción de Señas en Tiempo Real")

# Registro de módulos (routers) que gestionan las distintas áreas del backend
# - esp_handler: conexión con la ESP32-CAM
# - client_handler: comunicación con el frontend (WebSocket)
# - inference: simulación o ejecución del modelo IA
app.include_router(esp_router)
app.include_router(client_router)
app.include_router(inference_router)

@app.get("/")
def root():
    """
    Ruta base del servidor.
    Devuelve un mensaje simple indicando que el backend está activo.
    """
    return {"status": "running", "msg": "Backend SeñaVoz activo"}
