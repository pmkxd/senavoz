import React, { useEffect, useState } from "react";

export default function Registro() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/esp32/logs"); // Ajusta según backend

    ws.onopen = () => console.log("Conectado al WebSocket de logs");

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setLogs((prevLogs) => [data, ...prevLogs]); // más recientes arriba
    };

    ws.onclose = () => console.log("Desconectado del WebSocket de logs");

    return () => ws.close();
  }, []);

  const getColor = (type) => {
    switch (type) {
      case "translation":
        return "#0b6e99"; // azul
      case "frame":
        return "#d9534f"; // rojo
      case "text":
        return "#5cb85c"; // verde
      default:
        return "#333"; // gris
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Registro de Arduino</h1>
      <div
        style={{
          background: "#f9f9f9",
          border: "1px solid #ccc",
          padding: "1rem",
          height: "70vh",
          overflowY: "scroll",
        }}
      >
        {logs.length === 0 && <p>No hay eventos aún...</p>}
        <ul style={{ listStyle: "none", padding: 0 }}>
          {logs.map((log, index) => (
            <li
              key={index}
              style={{
                padding: "0.5rem",
                marginBottom: "0.3rem",
                background: getColor(log.type) + "20", // transparente
                borderLeft: `5px solid ${getColor(log.type)}`,
                borderRadius: "3px",
              }}
            >
              <strong>{log.type.toUpperCase()}:</strong>{" "}
              {log.text || log.message}{" "}
              {log.confidence ? `(${log.confidence})` : ""}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
