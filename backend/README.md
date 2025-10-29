# Backend TuCuidado (local)
Backend local para traducción de señas desde ESP32-CAM.

## Correr el servidor
1. Instalar dependencias:
   pip install -r requirements.txt
2. Ejecutar el backend:
   uvicorn app.main:app --reload --port 8000
3. ESP32-CAM se conecta a ws://<tu_ip_local>:8000/ws/esp32/esp01
