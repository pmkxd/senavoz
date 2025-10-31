import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Practice from "./pages/Practice";
import Modelo from "./pages/Modelo";
import Registro from "./pages/Registro"; 
import "./styles/global.css";

function App() {
  return (
    <Router>
      <Navbar />
      <div style={{ padding: "20px" }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/practice" element={<Practice />} />
          <Route path="/modelo" element={<Modelo />} />
          <Route path="/registro" element={<Registro />} /> {/* ← nueva ruta */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
