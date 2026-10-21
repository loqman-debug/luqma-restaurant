---
name: motion-primitives
description: Implement micro-interactions, smooth gestural animations, and UI primitives with Motion Primitives and Framer Motion. Use this skill whenever the user asks for motion primitives, spring physics, expandable drawers, magnetic buttons, or smooth layout transitions.
---

# Motion Primitives

Micro-interactions, gestures, and UI primitives built on Framer Motion and Tailwind CSS.

## Key Primitives

1. **Text Morph & Text Loop**:
   Smoothly morph between strings or cycle through keywords with spring physics.
2. **Magnetic Button**:
   Attracts the cursor with realistic gravitational pull and elastic snapping.
3. **Animated Tabs / Sliders**:
   Layout animations using `layoutId` for sliding pill highlights.
4. **Expandable Dialog & Drawer**:
   Expanding cards that morph seamlessly into full detail views or shopping carts.
5. **Cursor Follower / Tooltip**:
   Fluid floating tags and cursor attachments with inertial dampening.

## Integration Example: Magnetic CTA

```tsx
'use client';
import { motion, useMotionValue, useSpring } from 'framer-motion';
import { useRef } from 'react';

export function MagneticCTA({ children }: { children: React.ReactNode }) {
  const ref = useRef<HTMLButtonElement>(null);
  const x = useMotionValue(0);
  const y = useMotionValue(0);

  const springConfig = { damping: 15, stiffness: 150 };
  const smoothX = useSpring(x, springConfig);
  const smoothY = useSpring(y, springConfig);

  const handleMouseMove = (e: React.MouseEvent<HTMLButtonElement>) => {
    if (!ref.current) return;
    const { left, top, width, height } = ref.current.getBoundingClientRect();
    const centerX = left + width / 2;
    const centerY = top + height / 2;
    x.set((e.clientX - centerX) * 0.35);
    y.set((e.clientY - centerY) * 0.35);
  };

  const handleMouseLeave = () => {
    x.set(0);
    y.set(0);
  };

  return (
    <motion.button
      ref={ref}
      style={{ x: smoothX, y: smoothY }}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      className="px-8 py-4 rounded-full bg-amber-500 text-black font-bold shadow-lg transition-colors hover:bg-amber-400"
    >
      {children}
    </motion.button>
  );
}
```
