---
name: react-bits
description: Implement creative visual animations, canvas effects, text transforms, and interactive 2D/3D components from React Bits (reactbits.dev). Use this skill whenever the user asks for creative visual effects, aurora gradients, spotlight cards, particle explosions, or hyper-modern UI widgets.
---

# React Bits

A curated collection of animated, interactive, and customizable React components for modern digital experiences.

## Popular Categories & Components

1. **Backgrounds**:
   - `Aurora`: Fluid multi-color animated mesh gradient.
   - `Particles`: Configurable interactive particle fields.
   - `Hyperspeed`: Warp-speed star trails and velocity lines.
   - `Squares` / `GridMotion`: Smooth moving geometric backdrops.

2. **Text Animations**:
   - `SplitText`: Smooth staggered words and lines (avoid individual character splitting for Arabic).
   - `BlurText`: Cinematic blur-in with customizable spring curves.
   - `ShinyText`: Dynamic holographic shimmer running across titles.

3. **Components & Micro-interactions**:
   - `SpotlightCard`: Mouse-tracking radial gradient border and illumination.
   - `TiltedCard`: 3D perspective card tilting on hover.
   - `DecryptedText`: Cyberpunk character deciphering effect.

## Usage Guidelines for Arabic & RTL

- When using `SplitText` or staggered text effects, always split by `words` or `lines`, never `chars`, to preserve Arabic ligatures.
- Adjust transform origins and angle calculations when mirroring mouse tracking or spotlight effects in RTL.
- Pair with `Cairo` or `Tajawal` typography and appropriate `line-height` (>= 1.7).
