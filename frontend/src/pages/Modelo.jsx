// src/pages/Modelo.jsx
import React from "react";
import Esp32Model from "../components/Esp32Model";

// 🧠 Página dedicada al modelo 3D de la ESP32-CAM
// Muestra el componente Esp32Model dentro de un contenedor blanco.

function Modelo() {
  return (
    <div style={{ backgroundColor: "#fff", padding: "20px", borderRadius: "10px" }}>
      <h1>Modelo 3D de la ESP32-CAM</h1>
      <p>Visualiza la placa en 3D con posibilidad de rotación y zoom.</p>
      <Esp32Model />
    </div>
  );
}

export default Modelo;
