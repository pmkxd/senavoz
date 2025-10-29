import React, { useEffect, useState } from "react";
import { BACKEND_WS } from "../api";

function CameraStream() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const ws = new WebSocket(BACKEND_WS);
    ws.onopen = () => console.log("✅ Conectado al backend");
    ws.onmessage = (msg) => setMessages((prev) => [...prev, msg.data]);
    ws.onclose = () => console.log("❌ Conexión cerrada");
    return () => ws.close();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>📷 Stream desde ESP32</h2>
      <div style={{ background: "#eee", padding: "10px", borderRadius: "8px" }}>
        {messages.slice(-10).map((m, i) => (
          <p key={i}>{m}</p>
        ))}
      </div>
    </div>
  );
}

export default CameraStream;
