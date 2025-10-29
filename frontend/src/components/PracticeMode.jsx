import React, { useEffect, useState } from "react";
import { BACKEND_WS } from "../api";

function PracticeMode() {
  const [status, setStatus] = useState("Esperando...");
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const ws = new WebSocket(BACKEND_WS);
    setSocket(ws);
    ws.onmessage = (msg) => {
      const data = JSON.parse(msg.data);
      if (data.type === "result") {
        setStatus(data.correct ? "✅ Correcto" : "❌ Incorrecto");
      }
    };
    return () => ws.close();
  }, []);

  const handleStart = () => {
    socket?.send(JSON.stringify({ action: "start_practice" }));
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Modo práctica ✋</h2>
      <button onClick={handleStart}>Iniciar práctica</button>
      <p>{status}</p>
    </div>
  );
}

export default PracticeMode;
