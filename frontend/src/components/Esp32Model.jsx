// src/components/Esp32Model.jsx
import React, { useRef } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Stage } from "@react-three/drei";
import { STLLoader } from "three/examples/jsm/loaders/STLLoader";
import { useLoader } from "@react-three/fiber";
import * as THREE from "three";

// Modelo del ESP32-CAM
function Esp32CamModel() {
  const geometry = useLoader(STLLoader, "/models/esp32-cam.stl");
  const meshRef = useRef();

  // Material tipo metal cepillado con reflejo sutil
  const metalMaterial = new THREE.MeshStandardMaterial({
    color: 0x444444, // gris oscuro profesional
    metalness: 0.8,
    roughness: 0.3,
  });

  // Material negro mate para zonas de cámara
  const blackPlastic = new THREE.MeshStandardMaterial({
    color: 0x111111,
    metalness: 0.3,
    roughness: 0.9,
  });

  // Material plateado brillante (detalles metálicos)
  const silverAccent = new THREE.MeshStandardMaterial({
    color: 0xb0b0b0,
    metalness: 1,
    roughness: 0.2,
  });

  // Material para el lente de cámara (efecto vidrio)
  const lensMaterial = new THREE.MeshPhysicalMaterial({
    color: 0x223344,
    transmission: 0.9,
    roughness: 0.05,
    thickness: 0.5,
    clearcoat: 1,
  });

  return (
    <group ref={meshRef} scale={0.01}>
      {/* Parte principal del módulo */}
      <mesh geometry={geometry} material={metalMaterial} />
      {/* Detalles visuales (fake layering para contraste profesional) */}
      <mesh geometry={geometry} material={blackPlastic} scale={[0.99, 0.99, 0.99]} />
      {/* Bordes metálicos */}
      <mesh geometry={geometry} material={silverAccent} scale={[1.01, 1.01, 1.01]} />
      {/* Simulación del lente */}
      <mesh geometry={geometry} material={lensMaterial} scale={[0.98, 0.98, 0.98]} />
    </group>
  );
}

// Vista completa del modelo
export default function ModelViewer() {
  return (
    <div style={{ width: "100%", height: "80vh", background: "#fff" }}>
      <Canvas camera={{ position: [0.1, 0.1, 0.25], fov: 50 }}>
        {/* Iluminación tipo estudio */}
        <Stage environment={null} intensity={1.2} shadows>
          <Esp32CamModel />
        </Stage>
        <ambientLight intensity={0.5} />
        <directionalLight position={[2, 2, 3]} intensity={1.5} />
        <OrbitControls
          enableZoom={true}
          enablePan={true}
          enableRotate={true}
          target={[0, 0, 0]}
        />
      </Canvas>
    </div>
  );
}
