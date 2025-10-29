import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav style={{ backgroundColor: "#1976d2", padding: "12px", color: "#fff" }}>
      <h2>SeñaVoz</h2>
      <div style={{ display: "flex", gap: "10px" }}>
        <Link to="/" style={{ color: "white", textDecoration: "none" }}>Inicio</Link>
        <Link to="/practice" style={{ color: "white", textDecoration: "none" }}>Modo práctica</Link>
      </div>
    </nav>
  );
}

export default Navbar;
