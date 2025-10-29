import React from "react";
import CameraStream from "../components/CameraStream";

function Home() {
  return (
    <div>
      <h1>Bienvenido a SeñaVoz</h1>
      <p>Esta es la pantalla principal del sistema.</p>
      <CameraStream />
    </div>
  );
}

export default Home;
