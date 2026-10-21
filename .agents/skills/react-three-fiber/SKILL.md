---
name: react-three-fiber
description: Build interactive, hardware-accelerated 3D scenes, product viewers, and WebGL animations in React using React Three Fiber (@react-three/fiber), Three.js, and Drei (@react-three/drei). Use this skill whenever the user asks for 3D graphics, GLTF/GLB models, orbit controls, custom shaders, or immersive 3D canvas experiences.
---

# React Three Fiber (R3F)

Declarative, component-driven 3D scenes built on Three.js and React.

## Core Packages

```bash
npm install three @react-three/fiber @react-three/drei
npm install -D @types/three
```

## Architecture Pattern

```tsx
'use client';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Float, ContactShadows, Environment, useGLTF } from '@react-three/drei';
import { Suspense } from 'react';

function Model({ url }: { url: string }) {
  const { scene } = useGLTF(url);
  return <primitive object={scene} scale={2} />;
}

export default function ThreeScene() {
  return (
    <div className="w-full h-[600px] relative">
      <Canvas camera={{ position: [0, 2, 5], fov: 45 }}>
        <ambientLight intensity={0.7} />
        <spotLight position={[10, 10, 10]} angle={0.15} penumbra={1} intensity={1.5} />
        <Suspense fallback={null}>
          <Float speed={2} rotationIntensity={0.5} floatIntensity={1}>
            <Model url="/models/burger.glb" />
          </Float>
          <ContactShadows position={[0, -1, 0]} opacity={0.6} scale={10} blur={2} far={4} />
          <Environment preset="city" />
        </Suspense>
        <OrbitControls enableZoom={false} autoRotate autoRotateSpeed={1.5} />
      </Canvas>
    </div>
  );
}
```

## Performance Best Practices
- Pre-compress 3D models with Draco or Meshopt (`gltf-transform optimize`).
- Use instances (`Instances` or `InstancedMesh`) when rendering repeated items like seeds, fries, or particles.
- Set `dpr={[1, 2]}` on `<Canvas>` to avoid rendering 3x/4x on Retina mobile screens.
