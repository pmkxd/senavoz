import React, { useState } from "react";
import { Link } from "react-router-dom";

function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <nav style={{
      backgroundColor: "#1976d2",
      padding: "12px",
      color: "#fff",
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      position: "relative"
    }}>
      <h2>SeñaVoz</h2>

      {/* Botón menú */}
      <div style={{ position: "relative" }}>
        <button
          onClick={() => setMenuOpen(!menuOpen)}
          style={{
            background: "none",
            border: "none",
            color: "#fff",
            fontSize: "24px",
            cursor: "pointer"
          }}
        >
          ⋮
        </button>

        {/* Menú desplegable */}
        {menuOpen && (
          <div style={{
            position: "absolute",
            right: 0,
            top: "35px",
            backgroundColor: "#fff",
            color: "#000",
            borderRadius: "5px",
            boxShadow: "0 2px 8px rgba(0,0,0,0.2)",
            display: "flex",
            flexDirection: "column",
            minWidth: "150px",
            zIndex: 1000
          }}>
            <Link to="/" style={{ padding: "10px", textDecoration: "none", color: "#000" }} onClick={() => setMenuOpen(false)}>Inicio</Link>
            <Link to="/practice" style={{ padding: "10px", textDecoration: "none", color: "#000" }} onClick={() => setMenuOpen(false)}>Modo práctica</Link>
            <Link to="/modelo" style={{ padding: "10px", textDecoration: "none", color: "#000" }} onClick={() => setMenuOpen(false)}>Modelo</Link>
            <Link to="/registro" style={{ padding: "10px", textDecoration: "none", color: "#000" }} onClick={() => setMenuOpen(false)}>Registro</Link>
          </div>
        )}
      </div>
    </nav>
  );
}

export default Navbar;
